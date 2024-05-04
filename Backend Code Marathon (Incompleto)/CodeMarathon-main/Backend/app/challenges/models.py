import json
from django.db import models


class Challenge(models.Model):
    """The Challenge model."""

    # Challenge types
    TYPE_PROJECT = "P"
    TYPE_LEET = "L"
    TYPE_OPTIONS = [
        (TYPE_PROJECT, "Project"),
        (TYPE_LEET, "Leet Code")
    ]

    name = models.CharField(max_length=255, unique=True)
    question = models.TextField() # HTML
    tests = models.TextField(blank=True) # JSON
    type = models.CharField(
        max_length=1,
        choices=TYPE_OPTIONS,
        default=TYPE_LEET
    )
    active = models.BooleanField(default=False)
    value = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        """Make sure that the tests field is valid json before saving."""
        try:
            if self.type == self.TYPE_LEET:
                json.loads(self.tests)
            else:
                self.tests = ""
            super(Challenge, self).save(*args, **kwargs)
        except json.decoder.JSONDecodeError:
            raise ValueError("Invalid tests: not JSON formatted.")

    def get_num_tests(self):
        """Return the number of tests designated to this challenge."""
        tests = json.loads(self.tests)
        return len(tests)

    def __str__(self):
        return f"({self.id}) Challenge \"{self.name}\""
