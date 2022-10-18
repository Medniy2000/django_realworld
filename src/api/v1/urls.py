from django.urls import re_path, include

urlpatterns: list = [
    re_path(r"", include("src.api.v1.example_entity.urls")),
]
