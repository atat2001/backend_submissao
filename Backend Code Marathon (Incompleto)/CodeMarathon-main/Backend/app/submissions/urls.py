from django.urls import path
from submissions.views import (
    SubmissionList,
    SubmissionSubmit,
    SubmissionResults,
    SubmissionFinalResults
)


app_name = "submissions"


urlpatterns = [
    path("list", SubmissionList.as_view(), name="list"),
    path("results", SubmissionResults.as_view(), name="results"),
    path(
        "final_results",
        SubmissionFinalResults.as_view(),
        name="final-results"
    ),
    path("", SubmissionSubmit.as_view(), name="submit")
]
