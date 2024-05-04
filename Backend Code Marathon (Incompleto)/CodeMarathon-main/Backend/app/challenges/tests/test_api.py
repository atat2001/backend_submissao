from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from challenges.tests.helpers import sample_challenge
from challenges.serializers import ChallengeListSerializer


class ChallengeListApiTests(TestCase):
    """Test retrieving the list of Challenges."""
    URL = reverse("challenges:list")

    def setUp(self):
        self.client = APIClient()

    def test_get_success(self):
        """Test successfully getting the list of Challenges."""
        # Create some sample challenges
        challenge_1 = sample_challenge(name="_name1", active=True)
        challenge_2 = sample_challenge(name="_name2", active=True)
        res = self.client.get(self.URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = ChallengeListSerializer(
            (challenge_1, challenge_2),
            many=True
        )
        self.assertEqual(res.data, serializer.data)

    def test_inactive_challenges_not_in(self):
        """Test that inactive challenges are not retrieved."""
        challenge = sample_challenge(active=False)
        res = self.client.get(self.URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = ChallengeListSerializer(challenge)
        self.assertNotIn(serializer.data, res.data)


class ChallengeDetailApiTests(TestCase):
    """Test retrieving the details of a Challenge."""

    def setUp(self):
        self.client = APIClient()
        self.challenge = sample_challenge()
        self.url = reverse("challenges:detail", args=[self.challenge.id])

    def test_get_success(self):
        """Test successfully getting the details of a Challenge."""
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["question"], self.challenge.question)

    def test_inactive_fails(self):
        """Test that retrieving the details of an inactive Challenge fails."""
        self.challenge.active = False
        self.challenge.save()
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
