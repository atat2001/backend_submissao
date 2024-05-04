from unittest.mock import patch
from tempfile import TemporaryDirectory
from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from groups.tests.helpers import sample_group
from challenges.tests.helpers import sample_challenge
from challenges.models import Challenge
from submissions.tests.helpers import (
    sample_submission,
    sample_file,
    mock_test_submission
)
from submissions.models import Submission
from submissions.views import ErrorResponses, Results
from submissions.serializers import SubmissionListSerializer


class SubmissionListApiTests(TestCase):
    """Test retrieving a Group's Submissions."""
    URL = reverse("submissions:list")

    def setUp(self):
        self.group = sample_group()
        self.challenge = sample_challenge()
        self.submission = sample_submission(self.group, self.challenge)
        self.client = APIClient()

    def test_get_success(self):
        """Test successfully getting the list of Submissions."""
        payload = {
            "group": self.group.number,
            "password": self.group.password
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = SubmissionListSerializer(
            [self.submission],
            many=True
        )
        self.assertEqual(res.data, serializer.data)

    def test_get_submissions_group_only(self):
        """
        Test that getting the Submissions list retrieves Submissions for
        that group only.
        """
        other_group = sample_group(number=2)
        other_submission = sample_submission(other_group, self.challenge)
        payload = {
            "group": self.group.number,
            "password": self.group.password
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = SubmissionListSerializer(other_submission)
        self.assertNotIn(serializer.data, res.data)

    def test_wrong_password(self):
        """
        Test that retrieving with the wrong password returns a 401 error.
        """
        payload = {
            "group": self.group.number,
            "password": ""
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res.data, ErrorResponses.INVALID_CREDENTIALS)

    def test_invalid_group(self):
        """
        Test that getting the Submission's list of a non-existent group fails.
        """
        payload = {
            "group": "",
            "password": self.group.password,
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, ErrorResponses.INVALID_GROUP)


class SubmissionsSubmitApiTests(TestCase):
    """Test submitting new Submissions."""
    URL = reverse("submissions:submit")
    TEMP_FOLDER = TemporaryDirectory()

    def setUp(self):
        self.group = sample_group()
        self.challenge = sample_challenge()
        self.client = APIClient()

    @patch(
        "submissions.views.test_submission",
        side_effect=mock_test_submission(
            Submission.STATUS_FINISHED,
            "_output"
        )
    )
    @override_settings(MEDIA_ROOT=TEMP_FOLDER.name)
    def test_submit_successful_leet(self, mock):
        """Test making a successful submission."""
        file = sample_file()
        payload = {
            "group": self.group.number,
            "challenge": self.challenge.id,
            "password": self.group.password,
            "file": file
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # Check the saved status
        submission_id = res.data["id"]
        submission = Submission.objects.get(id=submission_id)
        expected = mock.side_effect()
        self.assertEqual(submission.status, expected.status)
        self.assertEqual(submission.output, expected.get_log())
        # Check that the score was correct
        self.assertEqual(submission.score, self.challenge.get_num_tests())
        self.assertEqual(res.data["result"], Results.PASSED)
        # Check that the mock was called correctly
        self.assertTrue(mock.called)
        self.assertEqual(
            mock.call_args.args,
            (
                submission.file.path,
                self.challenge.tests,
                submission_id,
                submission.original_file_name
            )
        )

    @patch(
        "submissions.views.test_submission",
        side_effect=mock_test_submission()
    )
    @override_settings(MEDIA_ROOT=TEMP_FOLDER.name)
    def test_submit_successful_project(self, mock):
        """
        Test making the submission of a project; the difference is that a
        project submission should not be tested and graded.
        """
        challenge = sample_challenge(
            name="Project",
            type=Challenge.TYPE_PROJECT
        )
        file = sample_file()
        payload = {
            "group": self.group.number,
            "challenge": challenge.id,
            "password": self.group.password,
            "file": file
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # Check the saved status
        submission_id = res.data["id"]
        submission = Submission.objects.get(id=submission_id)
        self.assertEqual(submission.status, Submission.STATUS_NONE)
        self.assertEqual(submission.output, "")
        # Make sure that results are not presend
        self.assertNotIn("results", res.data)
        # Check that the mock was called correctly
        self.assertFalse(mock.called)

    def test_wrong_password(self):
        """
        Test that a submission with the wrong password returns a 401 error.
        """
        file = sample_file()
        payload = {
            "group": self.group.number,
            "challenge": self.challenge.id,
            "password": "",
            "file": file
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res.data, ErrorResponses.INVALID_CREDENTIALS)

    def test_invalid_group(self):
        """Test that a submission to a non-existent group fails."""
        file = sample_file()
        payload = {
            "group": "",
            "challenge": self.challenge.id,
            "password": self.group.password,
            "file": file
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, ErrorResponses.INVALID_GROUP)

    def test_invalid_challenge(self):
        """Test that a submission to a non-existent challenge fails."""
        file = sample_file()
        payload = {
            "group": self.group.number,
            "challenge": "",
            "password": self.group.password,
            "file": file
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, ErrorResponses.INVALID_CHALLENGE)

    def test_invalid_file(self):
        """Test that a submission with an invalid file fails."""
        payload = {
            "group": self.group.number,
            "challenge": self.challenge.id,
            "password": self.group.password,
            "file": ""
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, ErrorResponses.INVALID_FILE)

    @override_settings(MEDIA_ROOT=TEMP_FOLDER.name)
    def test_throttle(self):
        """
        Test that submissions are throttled.

        A submission can't be made if another submission is still being
        graded.
        """
        # Create a submission
        sample_submission(
            self.group,
            self.challenge,
            status=Submission.STATUS_RUNNING
        )
        file = sample_file()
        payload = {
            "group": self.group.number,
            "challenge": self.challenge.id,
            "password": self.group.password,
            "file": file
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, ErrorResponses.THROTTLED)

    @patch(
        "submissions.views.test_submission",
        side_effect=mock_test_submission(
            Submission.STATUS_FINISHED,
            "_output"
        )
    )
    @override_settings(MEDIA_ROOT=TEMP_FOLDER.name)
    def test_throttle_group_only(self, mock):
        """Test that throttle is applied by group."""
        other = sample_group(number=2)
        sample_submission(
            other,
            self.challenge,
            status=Submission.STATUS_RUNNING
        )
        file = sample_file()
        payload = {
            "group": self.group.number,
            "challenge": self.challenge.id,
            "password": self.group.password,
            "file": file
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class SubmissionResultsApiTests(TestCase):
    """Test retrieving a Group's results."""
    URL = reverse("submissions:results")

    def setUp(self):
        self.group = sample_group()
        self.challenges = [sample_challenge(name=str(i)) for i in range(3)]
        self.client = APIClient()

    @patch(
        "challenges.models.Challenge.get_num_tests",
        side_effect=lambda *args, **kwargs: 1
    )
    def test_get_success(self, mock):
        """Test successfully getting the results for all challenges."""
        # Create random Submissions for some of the challenges
        sample_submission(self.group, self.challenges[0], score=1)
        sample_submission(self.group, self.challenges[1], score=0)
        payload = {
            "group": self.group.number,
            "password": self.group.password
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, [
            {
                "challenge": self.challenges[0].id,
                "result": Results.PASSED
            },
            {
                "challenge": self.challenges[1].id,
                "result": Results.INCOMPLETE
            },
            {
                "challenge": self.challenges[2].id,
                "result": Results.NOT_SUBMITTED
            }
        ])

    @patch(
        "challenges.models.Challenge.get_num_tests",
        side_effect=lambda *args, **kwargs: 1
    )
    def test_get_results_group_only(self, mock):
        """
        Test that getting the Submissions results retrieves Submissions for
        that group only.
        """
        other_group = sample_group(number=2)
        sample_submission(other_group, self.challenges[0], score=1)
        payload = {
            "group": self.group.number,
            "password": self.group.password
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, [
            {
                "challenge": challenge.id,
                "result": Results.NOT_SUBMITTED
            } for challenge in self.challenges
        ])


    def test_get_results_leet_only(self):
        """Test that project Challenges are not listed for results."""
        sample_challenge(type=Challenge.TYPE_PROJECT)
        payload = {
            "group": self.group.number,
            "password": self.group.password
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, [
            {
                "challenge": challenge.id,
                "result": Results.NOT_SUBMITTED
            } for challenge in self.challenges
        ])

    def test_get_results_active_only(self):
        """Test that inactive Challenges are not listed for results."""
        sample_challenge(active=False)
        payload = {
            "group": self.group.number,
            "password": self.group.password
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, [
            {
                "challenge": challenge.id,
                "result": Results.NOT_SUBMITTED
            } for challenge in self.challenges
        ])

    def test_get_results_excludes_running(self):
        """
        Test that a submission that is set to "running" is not accounted for.
        """
        sample_submission(
            self.group,
            self.challenges[0],
            status=Submission.STATUS_RUNNING
        )
        payload = {
            "group": self.group.number,
            "password": self.group.password
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, [
            {
                "challenge": challenge.id,
                "result": Results.NOT_SUBMITTED
            } for challenge in self.challenges
        ])


    @patch(
        "challenges.models.Challenge.get_num_tests",
        side_effect=lambda *args, **kwargs: 3
    )
    def test_get_results_best_submission(self, mock):
        """Test that only the best submission's result is retrieved."""
        sample_submission(self.group, self.challenges[0], score=1)
        sample_submission(self.group, self.challenges[0], score=3)
        sample_submission(self.group, self.challenges[0], score=2)
        payload = {
            "group": self.group.number,
            "password": self.group.password
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, [
            {
                "challenge": self.challenges[0].id,
                "result": Results.PASSED
            },
            {
                "challenge": self.challenges[1].id,
                "result": Results.NOT_SUBMITTED
            },
            {
                "challenge": self.challenges[2].id,
                "result": Results.NOT_SUBMITTED
            }
        ])

    def test_wrong_password(self):
        """
        Test that retrieving with the wrong password returns a 401 error.
        """
        payload = {
            "group": self.group.number,
            "password": ""
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res.data, ErrorResponses.INVALID_CREDENTIALS)

    def test_invalid_group(self):
        """
        Test that getting the Submission's results of a non-existent group
        fails.
        """
        payload = {
            "group": "",
            "password": self.group.password,
        }
        res = self.client.post(self.URL, data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data, ErrorResponses.INVALID_GROUP)


class FinalResultsApiTests(TestCase):
    """Test the admin get results endpoint."""
    URL = reverse("submissions:final-results")


    def setUp(self):
        self.user = User.objects.create_superuser(
            "admin", "", "password"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_authentication_required(self):
        self.client.logout()
        res = self.client.get(self.URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    @patch(
        "challenges.models.Challenge.get_num_tests",
        side_effect=lambda *args, **kwargs: 3
    )
    def test_success(self, mock):
        # Create some sample data
        group1 = sample_group(number=1)
        group2 = sample_group(number=2)
        group3 = sample_group(number=3)
        challenge1 = sample_challenge(name="c1")
        challenge2 = sample_challenge(name="c2")
        # Group1 submits three times to challenge1, getting two incompletes
        # and one pass, and no submissions to challenge2.
        sample_submission(group1, challenge1, score=3)
        sample_submission(group1, challenge1, score=2)
        sample_submission(group1, challenge1, score=1)
        # Group2 submits once to each challenge, getting an incomplete on the
        # first one and a pass on the second one.
        sample_submission(group2, challenge1, score=2)
        sample_submission(group2, challenge2, score=3)
        # Group3 will have no submissions.

        res = self.client.get(self.URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        expected = {"data": [
            {
                "group": group1.id,
                "name": None,
                "number": group1.number,
                "total_score": 1,
                "results": [
                    {
                        "challenge": challenge1.id,
                        "result": Results.PASSED
                    },
                    {
                        "challenge": challenge2.id,
                        "result": Results.NOT_SUBMITTED
                    }
                ]
            },
            {
                "group": group2.id,
                "name": None,
                "number": group2.number,
                "total_score": 1,
                "results": [
                    {
                        "challenge": challenge1.id,
                        "result": Results.INCOMPLETE
                    },
                    {
                        "challenge": challenge2.id,
                        "result": Results.PASSED
                    }
                ]
            },
            {
                "group": group3.id,
                "name": None,
                "number": group3.number,
                "total_score": 0,
                "results": [
                    {
                        "challenge": challenge1.id,
                        "result": Results.NOT_SUBMITTED
                    },
                    {
                        "challenge": challenge2.id,
                        "result": Results.NOT_SUBMITTED
                    }
                ]
            },
        ]}
        self.assertEqual(res.data, expected)

    def test_get_results_leet_only(self):
        """Test that project Challenges are not listed for results."""
        group = sample_group()
        sample_challenge(type=Challenge.TYPE_PROJECT)
        res = self.client.get(self.URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {"data": [{
            "group": group.id,
            "name": None,
            "number": group.number,
            "total_score": 0,
            "results": []
        }]})

    @patch(
        "challenges.models.Challenge.get_num_tests",
        side_effect=lambda *args, **kwargs: 3
    )
    def test_get_results_sorted(self, mock):
        """Test that the results are returned sorted."""
        group1 = sample_group(number=1)
        group2 = sample_group(number=2)
        challenge = sample_challenge(name="c1")
        # Group2 will have one score and Group1 will have zero score
        sample_submission(group1, challenge, score=0)
        sample_submission(group2, challenge, score=3)
        res = self.client.get(self.URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["data"][0]["group"], group2.id)
        self.assertEqual(res.data["data"][1]["group"], group1.id)

    @patch(
        "challenges.models.Challenge.get_num_tests",
        side_effect=lambda *args, **kwargs: 3
    )
    def test_get_results_value(self, mock):
        """Test that results account for the problem's value."""
        group = sample_group()
        challenge = sample_challenge(value=3)
        sample_submission(group, challenge, score=3)
        res = self.client.get(self.URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["data"][0]["total_score"], 3)
