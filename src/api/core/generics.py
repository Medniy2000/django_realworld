from rest_framework import generics as drf_generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView as drf_APIView

from src.api.core import mixins
from src.api.core.filters import filters_sets, filters_ordering, filters_beckend


class GenericAPIView(drf_generics.GenericAPIView):
    filterset_class = filters_sets.FilterSet
    filter_backends = (
        filters_ordering.OrderingFilter,
        filters_beckend.FilterBackend,
    )
    ordering_fields = ()
    lookup_field = "uuid"

    def get_metadata(self) -> dict:
        return {
            "allowed_fields": getattr(getattr(self.serializer_class, "Meta", {}), "fields", ()),
            "ordering_fields": self.ordering_fields,
            "filter_fields": self.filterset_class.Meta.fields or (),
        }


class APIView(drf_APIView):
    pass


class CreateAPIView(mixins.CreateModelMixin, GenericAPIView):
    """
    APIView for creating a model instance.
    """

    def post(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.create(request, *args, **kwargs)


class ListAPIView(mixins.ListModelMixin, GenericAPIView):
    """
    APIView for listing a queryset.
    """

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.list(request, *args, **kwargs)


class RetrieveAPIView(mixins.RetrieveModelMixin, GenericAPIView):
    """
    APIView for retrieving a model instance.
    """

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.retrieve(request, *args, **kwargs)


class DestroyAPIView(mixins.DestroyModelMixin, GenericAPIView):
    """
    APIView for deleting a model instance.
    """

    def delete(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.destroy(request, *args, **kwargs)


class UpdateAPIView(mixins.UpdateModelMixin, GenericAPIView):
    """
    APIView for updating a model instance.
    """

    def put(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.partial_update(request, *args, **kwargs)


class ListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    """
    APIView for listing a queryset or creating a model instance.
    """

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.create(request, *args, **kwargs)


class RetrieveUpdateAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    """
    APIView for retrieving, updating a model instance.
    """

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.partial_update(request, *args, **kwargs)


class RetrieveDestroyAPIView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    """
    APIView for retrieving or deleting a model instance.
    """

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.destroy(request, *args, **kwargs)


class RetrieveUpdateDestroyAPIView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    """
    APIView for retrieving, updating or deleting a model instance.
    """

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return self.destroy(request, *args, **kwargs)
