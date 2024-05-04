from rest_framework import serializers
from submissions.models import Submission


class SubmissionListSerializer(serializers.ModelSerializer):
    """Serializer for Submissions when presented in a list."""
    class Meta:
        model = Submission
        fields = ("id", "challenge", "status", "time")
