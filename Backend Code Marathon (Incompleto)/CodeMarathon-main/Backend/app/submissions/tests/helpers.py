import datetime
import tempfile
from submissions.models import Submission


def sample_submission(
        group,
        challenge,
        file="_file",
        status=Submission.STATUS_CREATED,
        output="_output",
        score=0,
        time=datetime.datetime(2000, 1, 1, 0, 0, 0)
    ):
    """
    Creates and saves a new Submission instance, returning it.

    Required arguments:
    - group: Group instance
    - challenge: Challenge instance

    Uses the following default values:
    - file: "_file"
    - status: Submission.STATUS_CREATED
    - output: "_output"
    - score: 0
    - time= Datetime(01/01/2000 00:00:00)
    """
    return Submission.objects.create(
        group=group,
        challenge=challenge,
        file=file,
        status=status,
        output=output,
        score=score,
        time=time
    )


def sample_file(suffix=".py"):
    """
    Creates and returns a temporary file with the given suffix on read mode.

    Suffix defaults to ".py".
    """
    return tempfile.TemporaryFile(mode="r", suffix=suffix)


def mock_test_submission(return_status="", return_output="", score=0):
    class MockGraderOutput:
        def __init__(self):
            self.status = return_status
        def get_log(self):
            return return_output
        def get_score(self):
            return score
    def inner_mock(*args, **kwargs):
        return MockGraderOutput()
    return inner_mock
