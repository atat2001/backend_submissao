from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.contrib.auth.models import User
from django.contrib.auth.models import Group as auth_Group
from groups.models import Group, Student
from submissions.models import Submission
from challenges.models import Challenge


# Unregister the user stuff
admin.site.unregister([
    User,
    auth_Group
])


# Register all the models
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "group")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "password")


# Actions to edit challenges.
@admin.action(description="Mark as active.")
def make_active(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.action(description="Mark as inactive.")
def make_inactive(modeladmin, request, queryset):
    queryset.update(active=False)


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "type", "active", "value")
    change_list_template = "challenges_admin.html"
    actions = [make_active, make_inactive]

    def get_urls(self):
        urls = super().get_urls()
        extra = [
            path(
                "set_leet_active/",
                self.admin_site.admin_view(self.set_leet_active),
                name="set_leet_active"
            ),
            path(
                "set_leet_inactive/",
                self.admin_site.admin_view(self.set_leet_inactive),
                name="set_leet_inactive"
            ),
            path(
                "set_project_active/",
                self.admin_site.admin_view(self.set_project_active),
                name="set_project_active"
            ),
            path(
                "set_project_inactive/",
                self.admin_site.admin_view(self.set_project_inactive),
                name="set_project_inactive"
            )
        ]
        return extra + urls

    def set_leet_active(self, request):
        self.model.objects.all().filter(type=Challenge.TYPE_LEET).update(
            active=True
        )
        self.message_user(request, "Set all Leet Challenges as ACTIVE.")
        return HttpResponseRedirect("../")

    def set_leet_inactive(self, request):
        self.model.objects.all().filter(type=Challenge.TYPE_LEET).update(
            active=False
        )
        self.message_user(request, "Set all Leet Challenges as INACTIVE.")
        return HttpResponseRedirect("../")

    def set_project_active(self, request):
        self.model.objects.all().filter(type=Challenge.TYPE_PROJECT).update(
            active=True
        )
        self.message_user(request, "Set all Project Challenges as ACTIVE.")
        return HttpResponseRedirect("../")

    def set_project_inactive(self, request):
        self.model.objects.all().filter(type=Challenge.TYPE_PROJECT).update(
            active=False
        )
        self.message_user(request, "Set all Project Challenges as INACTIVE.")
        return HttpResponseRedirect("../")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "challenge", "status", "score")


# Customize the website
admin.site.site_title = "CodeMarathon Admin"
admin.site.site_header = "CodeMarathon 2023"
admin.site.index_title = "Index"
