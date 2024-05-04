from django.db import models
from groups.models import Group
from challenges.models import Challenge


def submission_filename(instance, filename):
    """Returns a submission's filename in the system."""
    ext = filename.split(".")[-1]
    return f"Group{instance.group.number}_Submission{instance.id}.{ext}"


class Submission(models.Model):
    """The Submission model."""

    # Status
    STATUS_CREATED = "C"
    STATUS_RUNNING = "R"
    STATUS_FINISHED = "F"
    STATUS_TIMED_OUT = "T"
    STATUS_EXCEPTION = "E"
    STATUS_NONE = "N"
    STATUS_OPTIONS = [
        (STATUS_CREATED, "Created"),
        (STATUS_RUNNING, "Running"),
        (STATUS_FINISHED, "Finished"),
        (STATUS_TIMED_OUT, "Timed out"),
        (STATUS_EXCEPTION, "Exception"),
        (STATUS_NONE, "None")
    ]

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    file = models.FileField(upload_to=submission_filename)
    original_file_name = models.TextField(default="_no_name")
    status = models.CharField(
        max_length=1,
        choices=STATUS_OPTIONS,
        default=STATUS_CREATED
    )
    output = models.TextField()
    score = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Overwrite save in case the challenge is a project."""
        if self.challenge.type == Challenge.TYPE_PROJECT:
            self.status = self.STATUS_NONE
            self.output = ""
            self.score = 0
        return super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Submission {self.id} | Group {self.group.number} | "
            f"{self.challenge} | {self.time}"
        )
