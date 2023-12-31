from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from mapsharing.views import PlaylistViewSet, GeocodePointViewSet, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"playlists", PlaylistViewSet)
router.register(r"geocode-points", GeocodePointViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/account/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "api/account/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/account/register/", RegisterView.as_view(), name="sign_up"),
]
