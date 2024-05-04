from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.static import serve


def protected_media(request, path, document_root=None, show_indexes=False):
    if not request.user.is_superuser:
        return HttpResponse(status=401)
    return serve(request, path, document_root, show_indexes)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/submissions/", include("submissions.urls")),
    path("api/challenges/", include("challenges.urls")),
    path(
        f"{settings.MEDIA_URL[1:]}<path:path>",
        protected_media,
        {'document_root': settings.MEDIA_ROOT}
    )
]
