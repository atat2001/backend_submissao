from django.urls import path
from challenges.views import ChallengeList, ChallengeDetail


app_name = "challenges"


urlpatterns = [
    path("", ChallengeList.as_view(), name="list"),
    path("<int:pk>", ChallengeDetail.as_view(), name="detail")
]
