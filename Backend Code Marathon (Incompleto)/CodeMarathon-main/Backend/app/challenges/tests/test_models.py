from django.test import TestCase
from challenges.tests.helpers import sample_challenge


class ChallengeModelTests(TestCase):
    """Test the Challenge model."""

    def test_string(self):
        """Test the Challenge's string representation."""
        challenge = sample_challenge()
        self.assertEqual(
            str(challenge),
            f"({challenge.id}) Challenge \"{challenge.name}\""
        )

    def test_name_unique(self):
        """Test that a Challenge's name is unique."""
        challenge = sample_challenge()
        with self.assertRaises(Exception):
            sample_challenge(name=challenge.name)

    def test_validate_tests(self):
        """Test that tests is formatted as JSON."""
        with self.assertRaises(Exception):
            sample_challenge(tests="Invalid JSON")

    def test_get_num_tests(self):
        """Test getting the number of tests designated for the challenges."""
        challenge = sample_challenge(tests='{"aaa": "bbb"}')
        self.assertEqual(challenge.get_num_tests(), 1)
