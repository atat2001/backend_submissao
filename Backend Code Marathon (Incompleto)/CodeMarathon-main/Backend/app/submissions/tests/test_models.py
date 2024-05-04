from django.test import TestCase
from groups.tests.helpers import sample_group
from challenges.tests.helpers import sample_challenge
from challenges.models import Challenge
from submissions.tests.helpers import sample_submission
from submissions.models import Submission, submission_filename


class SubmissionModelTests(TestCase):
    """Test the Submission model."""

    def test_string(self):
        """Test the Submission's string representation."""
        group = sample_group()
        challenge = sample_challenge()
        submission = sample_submission(group, challenge)
        self.assertEqual(
            str(submission),
            (f"Submission {submission.id} | Group {submission.group.number} "
            f"| {submission.challenge} | {submission.time}")
        )

    def test_project_submission(self):
        """
        Test that creating a Submission for a project challenge results in
        status STATUS_NONE and empty output.
        """
        group = sample_group()
        challenge = sample_challenge(type=Challenge.TYPE_PROJECT)
        submission = sample_submission(group, challenge)
        self.assertEqual(submission.status, Submission.STATUS_NONE)
        self.assertEqual(submission.output, "")
        self.assertEqual(submission.score, 0)

    def test_filepath(self):
        """Test the Submission's auto-generated file path."""
        group = sample_group()
        challenge = sample_challenge()
        submission = sample_submission(group, challenge)
        ext = "py"
        filename = submission_filename(submission, f"file.{ext}")
        self.assertEqual(
            filename,
            f"Group{group.number}_Submission{submission.id}.{ext}"
        )
