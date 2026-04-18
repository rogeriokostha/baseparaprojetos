from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from apps.users.auth_views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    RegisterView,
    MeView,
    LogoutView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    path("api/auth/register/", RegisterView.as_view(), name="auth-register"),
    path("api/auth/login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/verify/", CustomTokenVerifyView.as_view(), name="token_verify"),
    path("api/auth/me/", MeView.as_view(), name="auth-me"),
    path("api/auth/logout/", LogoutView.as_view(), name="auth-logout"),
    path("api/", include("apps.users.api_urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)