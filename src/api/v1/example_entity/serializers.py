from src.api.core.serializers import Serializer
from rest_framework import serializers as drf_serializers

from src.core.models import ExampleModel


class ExampleModelSerializer(Serializer):
    uuid = drf_serializers.CharField()
    created_at = drf_serializers.DateTimeField()
    updated_at = drf_serializers.DateTimeField()
    example_field = drf_serializers.CharField()

    class Meta:
        model = ExampleModel
        fields = ("uuid", "created_at", "updated_at", "example_field")
