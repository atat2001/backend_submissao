import json
from pathlib import Path
from django.test import TestCase
from ddt import ddt, data
from unittest import skipIf
from unittest.mock import patch
import docker
from grader import GraderOutput, test_submission
from submissions.models import Submission


BASE_PATH = Path(__file__).parent
SAMPLE_PROGRAMS = BASE_PATH/"sample_programs"
DOCKER_CLIENT = docker.from_env(timeout=100)
DOCKER_ENABLED = True
try:
    DOCKER_CLIENT.ping()
except:
    DOCKER_ENABLED = False


class GraderOutputTests(TestCase):
    """Test the GraderOutput class."""
    # Sample data for a submission that scores 3/3
    TESTS = {
        "_input_1": "_output_1",
        "_input_2": "_output_2",
        "_input_3": "_output_3"
        }
    INPUTS = {
        "submission_id": 0,
        "tests": TESTS,
        "status": Submission.STATUS_FINISHED,
        "results": list(TESTS.values())
    }

    def test_serialization(self):
        """Test serializing a GraderOutput object."""
        instance = GraderOutput(self.INPUTS)
        self.assertEqual(json.loads(instance.serialize()), self.INPUTS)

    def test_from_serialization(self):
        """Test creating a GraderOutput object from serialization."""
        serialized = json.dumps(self.INPUTS)
        instance = GraderOutput.from_serialization(serialized)
        self.assertEqual(instance.get_data(), self.INPUTS)

    def test_score(self):
        """Test the score output of a GraderOutput."""
        instance = GraderOutput(self.INPUTS)
        self.assertEqual(instance.get_score(), 3)
        self.assertEqual(instance.get_tests_count(), 3)

    def test_log(self):
        """Test the log output of a GraderOutput."""
        instance = GraderOutput(self.INPUTS)
        log = instance.get_log()
        keys = list(self.TESTS.keys())
        values = list(self.TESTS.values())
        self.assertEqual(log, (
            f"GRADER SUBMISSION {self.INPUTS['submission_id']}\n"
            f"{GraderOutput.SEPARATOR}\n"
            "TEST 1\n"
            f"IN: {keys[0]}\n"
            f"EXPECTED: {values[0]}\n"
            f"OUT: {values[0]}\n"
            f"{GraderOutput.SEPARATOR}\n"
            "TEST 2\n"
            f"IN: {keys[1]}\n"
            f"EXPECTED: {values[1]}\n"
            f"OUT: {values[1]}\n"
            f"{GraderOutput.SEPARATOR}\n"
            "TEST 3\n"
            f"IN: {keys[2]}\n"
            f"EXPECTED: {values[2]}\n"
            f"OUT: {values[2]}\n"
            f"{GraderOutput.SEPARATOR}\n"
            f"FINAL RESULT: {instance.get_score()}/" #...
            f"{instance.get_tests_count()}\n"
            f"STATUS: {instance.status}"
        ))

    def test_set_exception(self):
        """Test the set_exception function."""
        instance = GraderOutput(self.INPUTS)
        # First test without setting it
        self.assertEqual(instance.get_exception(), "")
        # Then set it and test
        exception = "EXCEPTION"
        instance.set_exception(exception)
        self.assertEqual(instance.get_exception(), exception)
        self.assertEqual(instance.status, Submission.STATUS_EXCEPTION)
        # Test the get_log()
        log = instance.get_log().split("\n")
        self.assertEqual(log[-1], f"EXCEPTION: {exception}")

    def test_finished(self):
        """Test a submission that runs correctly and finishes."""
        instance = GraderOutput(self.INPUTS)
        self.assertEqual(instance.get_data(), self.INPUTS)

    def test_wrong_answer(self):
        """Test a submissions that has an incorrect answer."""
        inputs = self.INPUTS.copy()
        inputs["results"][0] = "_wrong_answer"
        instance = GraderOutput(inputs)
        self.assertEqual(instance.get_score(), 2)
        self.assertEqual(instance.get_tests_count(), 3)


@skipIf(not DOCKER_ENABLED, "Docker engine not running.")
@ddt
class GraderTests(TestCase):
    """
    Test the grader function to run and test files.

    The programs submited are simple: they receive an integer and print that
    same integer + 1.

    Ex:
        Input: 10
        Output: 11
    """
    EXTENSIONS = GraderOutput.VALID_EXT

    @data(*EXTENSIONS)
    def test_success(self, ext):
        """Test submitting numbers to the test program."""
        # Sample test case; first two tests pass, last fails.
        tests = {"3": "4", "5": "6", "7":"0"}
        tests_str = json.dumps(tests)
        file_path = SAMPLE_PROGRAMS/f"program.{ext}"
        output = test_submission(file_path, tests_str, 0)
        self.assertEqual(output.status, Submission.STATUS_FINISHED)
        self.assertEqual(output.get_tests_count(), 3)
        self.assertEqual(output.get_score(), 2)

    @data(*EXTENSIONS)
    def test_exception(self, ext):
        """Test submitting a letter to the program."""
        # Sample test case; first two tests pass, last raises exception.
        tests = {"3": "4", "5": "6", "A": "B"}
        tests_str = json.dumps(tests)
        file_path = SAMPLE_PROGRAMS/f"program.{ext}"
        output = test_submission(file_path, tests_str, 0)
        self.assertEqual(output.status, Submission.STATUS_EXCEPTION)
        self.assertEqual(output.get_tests_count(), 3)
        self.assertEqual(output.get_score(), 2)
        # Make sure the exception is shown
        self.assertNotEqual(output.results[0], "")

    # Mock the time sleep so the start time is much much lower than the
    # current time and force a timeout.
    @patch(
        "grader.src.time.time_ns",
        side_effect=[0, 10**100]*len(EXTENSIONS)
    )
    @data(*EXTENSIONS)
    def test_timeout(self, ext, mock):
        """Test a simple program that will timeout on it's execution."""
        # Sample tests; don't matter since it will timeout
        tests = {"1": "2"}
        tests_str = json.dumps(tests)
        file_path = SAMPLE_PROGRAMS/f"program.{ext}"
        output = test_submission(file_path, tests_str, 0)
        self.assertEqual(output.status, Submission.STATUS_TIMED_OUT)
        self.assertEqual(output.get_tests_count(), 1)
        self.assertEqual(output.get_score(), 0)
        self.assertEqual(output.results[0], "")

    def test_invalid_extension(self):
        """Test using a file with an unsopported extension."""
        file_path = SAMPLE_PROGRAMS/"program.txt"
        output = test_submission(file_path, "{}", 0)
        self.assertEqual(output.status, Submission.STATUS_EXCEPTION)
        self.assertEqual(output.get_exception(), GraderOutput.INVALID_EXT)

    @data(*EXTENSIONS)
    def test_multiline_input_output(self, ext):
        """Test using multi input lines and expecting multiple output."""
        file_path = SAMPLE_PROGRAMS/f"multiline.{ext}"
        output = test_submission(file_path, """
            {
                "3\\n4": "7\\n12"
            }
            """,
            0
        )
        self.assertEqual(output.status, Submission.STATUS_FINISHED)
        self.assertEqual(output.get_score(), 1)
