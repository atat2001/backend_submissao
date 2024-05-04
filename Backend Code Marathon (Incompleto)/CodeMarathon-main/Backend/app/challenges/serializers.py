from rest_framework import serializers
from challenges.models import Challenge


class ChallengeListSerializer(serializers.ModelSerializer):
    """Serializer for Challenges when presented in a list."""
    class Meta:
        model = Challenge
        fields = ("id", "name")


class ChallengeDetailSerializer(serializers.ModelSerializer):
    """Serializer for Challenges when presented as a detailed view."""
    class Meta:
        model = Challenge
        fields = ("id", "name", "question")
