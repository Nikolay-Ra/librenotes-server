from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("notes", views.NoteViewSet)
router.register("tags", views.TagViewSet)
router.register("sync", views.SyncViewSet, basename="Sync")

urlpatterns = [
    path("", include(router.urls)),
]
