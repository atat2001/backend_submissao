from challenges.models import Challenge


def sample_challenge(
        name="_name",
        question="<p>_question</p>",
        tests="{}",
        type=Challenge.TYPE_LEET,
        active=True,
        value=1
    ):
    """
    Creates and saves a new Challenge instance, returning it.

    Uses the following default values:
    - name: "_name"
    - question: "<p>_question</p>"
    - tests: "{}"
    - active: True
    - value: 1
    """
    return Challenge.objects.create(
        name=name,
        question=question,
        tests=tests,
        type=type,
        active=active,
        value=value
    )
