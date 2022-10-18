from django.urls import re_path, include


urlpatterns: list = [
    re_path(r"api/v1/", include("src.api.v1.urls")),
]
