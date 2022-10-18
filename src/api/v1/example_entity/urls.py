from django.urls import re_path, include
from rest_framework.routers import SimpleRouter

from src.api.v1.example_entity.viewsets import ExampleViewSet

router = SimpleRouter(trailing_slash=True)

router.register("example-entities", ExampleViewSet, basename="example-entities")

urlpatterns: list = [
    re_path("", include(router.urls)),
]
