from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import UrlViewSet


app_name = "api"

v1_router = DefaultRouter()
v1_router.register("urls", UrlViewSet, basename="urls")

urlpatterns = [
    path("v1/", include(v1_router.urls)),
]

