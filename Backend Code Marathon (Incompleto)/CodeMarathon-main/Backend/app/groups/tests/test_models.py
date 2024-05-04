from django.test import TestCase
from groups.tests.helpers import sample_group, sample_student


class GroupModelTests(TestCase):
    """Test the Group model."""

    def test_string(self):
        """Test the Group's string representation."""
        group = sample_group()
        self.assertEqual(str(group), f"Group {group.name} | {group.number}")

    def test_number_unique(self):
        """Test that a Group's number is unique."""
        group = sample_group()
        with self.assertRaises(Exception):
            sample_group(number=group.number)


class StudentModelTests(TestCase):
    """Test the Student model."""

    def setUp(self):
        self.group = sample_group()

    def test_string(self):
        """Test the Student's string representation."""
        student = sample_student(self.group)
        self.assertEqual(
            str(student),
            f"{student.name} | {student.group}"
        )
