from django.urls import path
from rest_framework.routers import DefaultRouter
from .api_views import UserViewSet, ProfileDetailView
router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("profile/", ProfileDetailView.as_view(), name="profile-detail"),
]

urlpatterns += router.urls