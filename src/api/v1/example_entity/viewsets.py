from collections import OrderedDict
from typing import Tuple, Type

from django.db.models import QuerySet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from src.api.core.filters.filters_beckend import FilterBackend
from src.api.core.filters.filters_ordering import OrderingFilter
from src.api.core.viewsets import ReadOnlyModelViewSet
from src.api.v1.example_entity.filters import ExampleModelFilterSet
from src.api.v1.example_entity.serializers import ExampleModelSerializer
from src.core.models import ExampleModel


class ExampleViewSet(ReadOnlyModelViewSet):
    serializer_class = ExampleModelSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)

    filterset_class = ExampleModelFilterSet
    filter_backends: Tuple[Type[OrderingFilter], Type[FilterBackend]] = (
        OrderingFilter,
        FilterBackend,
    )
    ordering_fields: Tuple[str] = (  # type: ignore
        "created_at",
        "updated_at",
    )

    def get_queryset(self) -> QuerySet:
        queryset = ExampleModel.objects.all()
        return queryset

    @action(detail=False, methods=["get"], url_path="meta")
    def meta(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return Response(self.get_metadata())

    def get_metadata(self) -> dict:
        data = OrderedDict(
            {
                "sort_fields": (
                    "created_at",
                    "updated_at",
                ),
                "filter_fields": list(self.filterset_class.Meta.fields),
            }
        )
        return data
