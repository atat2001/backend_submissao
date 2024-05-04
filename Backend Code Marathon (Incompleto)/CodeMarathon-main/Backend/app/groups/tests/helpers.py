from groups.models import Group, Student


def sample_group(number=1, password="ABCDEF"):
    """
    Creates and saves a new Group instance, returning it.

    Uses the following default values:
    - number: 1
    - password: "_password"
    """
    return Group.objects.create(number=number, password=password)


def sample_student(group, name="_name"):
    """
    Creates and saves a new Student instance, returning it.

    Required arguments:
    - group: Group instance

    Uses the following default values:
    - name: "_name"
    """
    return Student.objects.create(name=name, group=group)
