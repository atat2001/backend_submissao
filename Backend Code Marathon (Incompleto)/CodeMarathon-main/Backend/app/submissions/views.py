from django.db.models import Q
from rest_framework import status, permissions, authentication
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from groups.models import Group
from challenges.models import Challenge
from submissions.models import Submission
from submissions.serializers import SubmissionListSerializer
from grader import test_submission


class ErrorResponses:
    INVALID_GROUP = "Invalid group."
    INVALID_CREDENTIALS = "Invalid credentials."
    INVALID_CHALLENGE = "Invalid challenge."
    INVALID_FILE = "Invalid file."
    THROTTLED = "Submission throttled because another one is still running."

class Results:
    PASSED = "P"
    INCOMPLETE = "I"
    NOT_SUBMITTED = "N"


class SubmissionList(APIView):
    """ApiView to list a Group's Submissions."""
    queryset = Submission.objects.all()
    http_method_names = ["post"]

    def post(self, *args, **kwargs):
        """
        Make sure the group credentials are correct and return the list of
        Submissions.
        """
        try:
            number = self.request.data.get("group")
            group = Group.objects.get(number=number)
        except:
            return Response(
                data=ErrorResponses.INVALID_GROUP,
                status=status.HTTP_400_BAD_REQUEST
            )
        password = self.request.data.get("password")
        if password != group.password:
            return Response(
                data=ErrorResponses.INVALID_CREDENTIALS,
                status=status.HTTP_401_UNAUTHORIZED
            )
        submissions = self.queryset.filter(group=group)
        data = SubmissionListSerializer(submissions, many=True)
        return Response(data.data, status=status.HTTP_200_OK)


class SubmissionResults(APIView):
    """ApiView to get all of a group's LeetCode results."""
    http_method_names = ["post"]

    def post(self, *args, **kwargs):
        """
        Return all the results for the leet code submissions given a group's
        credentials.
        """
        try:
            number = self.request.data.get("group")
            group = Group.objects.get(number=number)
        except:
            return Response(
                data=ErrorResponses.INVALID_GROUP,
                status=status.HTTP_400_BAD_REQUEST
            )
        password = self.request.data.get("password")
        if password != group.password:
            return Response(
                data=ErrorResponses.INVALID_CREDENTIALS,
                status=status.HTTP_401_UNAUTHORIZED
            )
        # Calculate the results
        retval = []
        challenges = Challenge.objects.filter(
            type=Challenge.TYPE_LEET,
            active=True
        )
        for challenge in challenges:
            submissions = Submission.objects.filter(
                ~Q(status=Submission.STATUS_RUNNING),
                group=group,
                challenge=challenge
            )
            if not submissions.exists():
                retval.append({
                    "challenge": challenge.id,
                    "result": Results.NOT_SUBMITTED
                })
                continue
            high = 0
            for submission in submissions:
                high = max(high, submission.score)
            retval.append({
                "challenge": challenge.id,
                "result": (
                    Results.PASSED if high == challenge.get_num_tests()
                    else Results.INCOMPLETE
                )
            })
        return Response(data=retval, status=status.HTTP_200_OK)


class SubmissionFinalResults(APIView):
    """
    ApiView to get all results from all challenges and all groups as a list.
    """
    http_method_names = ["get"]
    permission_classes = [permissions.IsAdminUser]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "final_results.html"

    def get(self, *args, **kwargs):
        """
        Return a list of all the groups with all the results for each
        challenge.
        """
        retval = []
        for group in Group.objects.all():
            group_data = {
                "group": group.id,
                "name": group.name,
                "number": group.number,
            }
            results = []
            score = 0
            for challenge in Challenge.objects.filter(
                    type=Challenge.TYPE_LEET
            ):
                group_submissions = Submission.objects.filter(
                    ~Q(status=Submission.STATUS_RUNNING),
                    group=group,
                    challenge=challenge
                )
                if not group_submissions.exists():
                    results.append({
                        "challenge": challenge.id,
                        "result": Results.NOT_SUBMITTED
                    })
                    continue
                high = 0
                for submission in group_submissions:
                    high = max(high, submission.score)
                if high == challenge.get_num_tests():
                    score += challenge.value
                    results.append({
                        "challenge": challenge.id,
                        "result": Results.PASSED
                    })
                else:
                    results.append({
                        "challenge": challenge.id,
                        "result": Results.INCOMPLETE
                    })
            group_data.update({"results": results})
            group_data.update({"total_score": score})
            retval.append(group_data)
        # Oder retval according to the score
        retval.sort(key=lambda el: el["total_score"], reverse=True)
        # Must return a dict for the renderer
        return Response(data={"data": retval}, status=status.HTTP_200_OK)


class SubmissionSubmit(APIView):
    """ApiView to create a new submission."""
    http_method_names = ["post"]

    def post(self, *args, **kwargs):
        """
        Add a new submission to the database. This will run the submission
        trough the grader and return the interpreted results.
        """
        # Authenticate the group
        try:
            number = self.request.data.get("group")
            group = Group.objects.get(number=number)
        except:
            return Response(
                data=ErrorResponses.INVALID_GROUP,
                status=status.HTTP_400_BAD_REQUEST
            )
        password = self.request.data.get("password")
        if password != group.password:
            return Response(
                data=ErrorResponses.INVALID_CREDENTIALS,
                status=status.HTTP_401_UNAUTHORIZED
            )
        # Get the challenge
        try:
            challenge_id = self.request.data.get("challenge")
            challenge = Challenge.objects.get(id=challenge_id)
        except:
            return Response(
                data=ErrorResponses.INVALID_CHALLENGE,
                status=status.HTTP_400_BAD_REQUEST
            )
        # Check if there's a submission running already
        existent = Submission.objects.filter(
            group=group,
            challenge=challenge,
            status=Submission.STATUS_RUNNING
        ).exists()
        if existent:
            return Response(
                data=ErrorResponses.THROTTLED,
                status=status.HTTP_400_BAD_REQUEST
            )
        # Get the file
        file = self.request.FILES.get("file")
        if not file:
            return Response(
            data=ErrorResponses.INVALID_FILE,
            status=status.HTTP_400_BAD_REQUEST
        )
        # Create the submission
        submission = Submission.objects.create(
            group=group,
            challenge=challenge,
            original_file_name=file.name
        )
        # Associate the file
        submission.file = file
        submission.save()
        # In case it's a leet code submission... test it!
        if challenge.type != Challenge.TYPE_PROJECT:
            submission_grader_output = test_submission(
                submission.file.path,
                submission.challenge.tests,
                submission.id,
                submission.original_file_name
            )
            # Save the results and return the response
            submission.status = submission_grader_output.status
            submission.output = submission_grader_output.get_log()
            score = submission.score = submission_grader_output.get_score()
            submission.save()
            result = (
                Results.PASSED if score == challenge.get_num_tests()
                else Results.INCOMPLETE
            )
            return Response(
                data={
                    "id": submission.id,
                    "status": submission.status,
                    "result": result
                },
                status=status.HTTP_200_OK
            )
        return Response(
            data={"id": submission.id, "status": submission.status},
            status=status.HTTP_200_OK
        )
