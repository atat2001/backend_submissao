from pyexpat import model
from django.db import models


class Group(models.Model):
    """The Group model."""
    number = models.PositiveIntegerField(unique=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f"Group {self.name} | {self.number}"


class Student(models.Model):
    """The Student model."""
    name = models.CharField(max_length=64)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.group}"
