import time
import json
import traceback
import docker
from distutils.dir_util import copy_tree as copy_folder_contents
from distutils.file_util import copy_file
from pathlib import Path
from tempfile import TemporaryDirectory
from grader.grader_output import GraderOutput
from submissions.models import Submission


# Globals --------------------------------------------------------------------
DOCKER_CLIENT = docker.from_env(timeout=100)
SCRIPT_DIR = Path(__file__).parents[0]
DEFAULT_TIMEOUT = 5 * 60 # 5 minutes
DEFAULT_UPDATE_RATE = 2 # Interval in seconds to check for timeout


# Exceptions -----------------------------------------------------------------
class DockerException(Exception):
    """Exception raised when something goes wrong with docker"""
    def __init__(self, exception):
        self.exception = exception

    def __str__(self):
        return f"DOCKER_EXCEPTION: {self.exception}"


class ContainerTimedOutException(Exception):
    """Exception raised when a submission times out."""
    pass


# Main code ------------------------------------------------------------------
def run_container(folder, timeout_seconds=0, submission_id=0) -> str:
    """
    Runs the docker container in the specified folder.

    Returns the exit code and the output.

    If timeout_seconds is set, the container execution will be stopped once
    timeout_seconds seconds passes and ContainerTimedOutException will be
    raised.
    """
    name = f"codewars_submission_{submission_id}"
    image = None
    container = None

    # Calculate timeout stuff
    initial_time = time.time_ns()
    timeout_ns = timeout_seconds * 10**9
    end_time = initial_time + timeout_ns

    # Create the image and run the container
    try:
        print("Building image")
        image = DOCKER_CLIENT.images.build(
            path=str(folder),
            tag=name,
            rm=True
        )[0]
        print("Running container")
        container = DOCKER_CLIENT.containers.run(
                image=image,
                name=name,
                command="python main.py",
                environment={"SUBMISSION": submission_id},
                detach=True
            )
    except Exception as e:
        print(f"Exception: {str(e)}")
        if image:
            DOCKER_CLIENT.images.remove(name, force=True)
        if container:
            container.stop(timeout=0)
            container.remove(force=True)
        raise DockerException(e)
    print("Container running")
    # Handle Excecution
    try:
        while True:
            container.reload()
            if container.status == "exited":
                break
            elif timeout_seconds and time.time_ns() > end_time:
                # Force close and raise timeout
                container.stop(timeout=0)
                raise ContainerTimedOutException()
            time.sleep(DEFAULT_UPDATE_RATE)
        # Finished - let's return the logs
        output = container.logs(stdout=True, stderr=False)
        print(f"Container output: {output}")
        print("here")
        output = output.decode("utf-8").split("\n")[0]
        print("here")
        if not output:
            raise ValueError("No output from container")
        try:
            print("here")
            print(json.loads(output))
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON output from container")
        return output
    except ContainerTimedOutException as ctoe:
        raise ctoe
    except Exception as e:
        raise DockerException(e)
    finally:
        DOCKER_CLIENT.images.remove(name, force=True)
        container.remove(force=True)


def test_submission(
            submission_file,
            tests_string,
            submission_id,
            original_name=""
        ) -> GraderOutput:
    """
    Runs the submission on a new docker container and run the tests. Returns
    a GraderOutput object.

    Arguments:
    - submission_file: The path to the submitted file
    - tests_string: The tests to be applied, as a JSON-formatted string
    """

    # Create a temporary folder to work with
    folder = TemporaryDirectory()
    folder_path = Path(folder.name)

    # SETUP THE CONTAINER
    # Copy the container files to it
    copy_folder_contents(str(SCRIPT_DIR/"container"), str(folder_path))
    # Copy the grader_output.py file to it to; this is the module that
    # contains the class responsible for communication.
    module = "grader_output.py"
    copy_file(str(SCRIPT_DIR/module), str(folder_path/"app"/module))
    # Save the tests
    tests = json.loads(tests_string)
    with open(folder_path/"app"/"tests.json", "w+") as tests_file:
        tests_file.write(tests_string)
    # Copy the submission file
    ext = str(submission_file).split(".")[-1]
    if ext not in GraderOutput.VALID_EXT:
        instance = GraderOutput({
                "submission_id": submission_id,
                "tests": tests,
                "status": Submission.STATUS_FINISHED,
                "results": ["" for _ in tests]
            })
        instance.set_exception(GraderOutput.INVALID_EXT)
        return instance
    if ext != "java":
        copy_file(str(submission_file), str(folder_path/"app"/f"input.{ext}"))
    else:
        # Java needs a special case as the file name matters.
        copy_file(str(submission_file), str(folder_path/"app"/original_name))
    # Run the container
    try:
        output = run_container(folder_path, DEFAULT_TIMEOUT, submission_id)
        return GraderOutput.from_serialization(output)
    except ContainerTimedOutException:
        print("desserialization failed: timeout")
        return GraderOutput({
            "submission_id": submission_id,
            "tests": tests,
            "status": Submission.STATUS_TIMED_OUT,
            "results": ["" for _ in tests]
        })
    except Exception as e:
        print("desserialization failed")
        # print(output)
        print(f"Exception: {str(e)}")
        traceback_ext = traceback.format_exc()
        try:
            instance = GraderOutput.from_serialization(output)
            instance.set_exception(traceback_ext)
            return instance
        except:
            instance = GraderOutput({
                "submission_id": submission_id,
                "tests": tests,
                "status": Submission.STATUS_FINISHED,
                "results": ["" for _ in tests]
            })
            instance.set_exception(
                f"Original Exception:\n{traceback_ext}\n"
                f"New Exception:\n{traceback.format_exc()}"
            )
            return instance
