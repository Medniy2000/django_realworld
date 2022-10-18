from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from src.api.core import generics
from src.api.core import mixins


class GenericViewSet(ViewSetMixin, generics.GenericAPIView):
    """
    The GenericViewSet class does not provide any actions by default,
    but does include the base set of generic view behavior, such as
    the `get_object` and `get_queryset` methods.
    """

    @action(detail=False, methods=["get"], url_path="meta")
    def meta(self, request: Request) -> Response:
        """
        Get meta information
        """
        data = self.get_metadata()
        return Response(data)


class ReadOnlyModelViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    """
    A ViewSet that provides default `list()` and `retrieve()` actions.
    """

    pass


class XModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    A ViewSet that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """

    pass


class ListCreateUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    A ViewSet that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()` and `list()` actions.
    """

    pass


class ListCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    pass
