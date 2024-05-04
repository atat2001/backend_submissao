from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from challenges.models import Challenge
from challenges.serializers import (
    ChallengeListSerializer,
    ChallengeDetailSerializer
)


class ChallengeList(ListAPIView):
    """ApiView to list available Challenges"""
    queryset = Challenge.objects.filter(active=True)
    serializer_class = ChallengeListSerializer


class ChallengeDetail(RetrieveAPIView):
    """ApiView to retrieve a Challenge's details."""
    queryset = Challenge.objects.filter(active=True)
    serializer_class = ChallengeDetailSerializer

    def get_object(self):
        return get_object_or_404(self.queryset, pk=self.kwargs["pk"])
