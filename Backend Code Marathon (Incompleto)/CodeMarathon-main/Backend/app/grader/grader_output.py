import json


class GraderOutput:
    """
    GraderOutput class.

    This class is used to hold information from running the grader. This
    information can be serialized and deserialized into a string to be passed
    trough the docker container logs.

    The data_dict argument should consists of the following:
    - "submission_id": (int) the submission's ID.
    - "tests": (dict[string: string]) the tests ran on the submission.
    - "status" (string) single char (Submission class status).
    - "results": (list[string]) list of the outputs for the specific test.
    """
    SEPARATOR = "------------------------------------------------------------"
    VALID_EXT = ["py", "js", "c", "cpp", "java"]
    INVALID_EXT = "The file provided has an invalid extension."
    # Status
    STATUS_FINISHED = "F"
    STATUS_TIMED_OUT = "T"
    STATUS_EXCEPTION = "E"

    def __init__(self, data_dict: dict):
        self.submission_id = data_dict["submission_id"]
        self.tests = data_dict["tests"]
        self.status = data_dict["status"]
        self.results = data_dict["results"]
        self.exception = ""

    def get_data(self) -> dict:
        """Returns this instance's data as a dictionary."""
        return {
            "submission_id": self.submission_id,
            "tests": self.tests,
            "status": self.status,
            "results": self.results
        }

    def serialize(self) -> str:
        """Returns this instance's data as a json serialized string."""
        serialized_data = json.dumps(self.get_data())
        print(serialized_data)  # Print the serialized data
        return serialized_data

    @staticmethod
    def from_serialization(serialized_data: str):
        """
        Returns a GraderOutput instance parsed from the serialized data.

        The serialized data should be in json format.
        """
        return GraderOutput(json.loads(serialized_data))

    def get_score(self) -> int:
        """Returns the number of tests passed."""
        score = 0
        for i, output in enumerate(self.tests.values()):
            if output == self.results[i]:
                score += 1
        return score

    def get_tests_count(self) -> int:
        """Returns the number of tests."""
        return len(self.tests)

    def set_exception(self, exception_string: str):
        """
        Sets an exception on this instance, changing the status and saving the
        exception as a string.
        """
        self.exception = exception_string
        self.status = self.STATUS_EXCEPTION

    def get_exception(self) -> str:
        """
        Returns the saved exception ("" if none).

        Attention: This isn't an exception raised during a test, but during
        the execution of the grader itself.
        """
        return self.exception

    def get_log(self) -> str:
        """Returns a "pretty print" log for this instance's data."""
        output = []
        output.append(f"GRADER SUBMISSION {self.submission_id}")
        output.append(self.SEPARATOR)
        keys = list(self.tests.keys())
        values = list(self.tests.values())
        for i in range(self.get_tests_count()):
            output.append(f"TEST {i+1}")
            output.append(f"IN: {keys[i]}")
            output.append(f"EXPECTED: {values[i]}")
            output.append(f"OUT: {self.results[i]}")
            output.append(self.SEPARATOR)
        output.append(
            f"FINAL RESULT: {self.get_score()}/{self.get_tests_count()}"
        )
        output.append(f"STATUS: {self.status}")
        if self.exception:
            output.append(self.SEPARATOR)
            output.append(f"EXCEPTION: {self.exception}")
        return "\n".join(output)

    def __eq__(self, __o: object) -> bool:
        if not type(__o) == GraderOutput:
            raise ValueError(
                "GraderOutput can only be compared to another GraderOutput "
                "object."
            )
        return self.get_data() == __o.get_data()
