from django.db import transaction
from rest_framework import mixins as drf_mixins
from rest_framework import serializers as drf_serializers
from rest_framework.request import Request

from rest_framework.response import Response


class CreateModelAtomicMixin(drf_mixins.CreateModelMixin):
    """
    Create a instance atomic.
    """

    @transaction.atomic
    def create(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super(CreateModelAtomicMixin, self).create(request, *args, **kwargs)


class CreateModelMixin(drf_mixins.CreateModelMixin):
    """
    Create a instance.
    """

    def create(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super(CreateModelMixin, self).create(request, *args, **kwargs)


class ListModelMixin(drf_mixins.ListModelMixin):
    """
    List a QuerySet.
    """

    pass


class RetrieveModelMixin(drf_mixins.RetrieveModelMixin):
    """
    Retrieve a model instance.
    """

    pass


class UpdateModelAtomicMixin(drf_mixins.UpdateModelMixin):
    """
    Update a model instance atomic.
    """

    @transaction.atomic
    def update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super(UpdateModelAtomicMixin, self).update(request, *args, **kwargs)


class UpdateModelMixin(drf_mixins.UpdateModelMixin):
    """
    Update a model instance.
    """

    def update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super(UpdateModelMixin, self).update(request, *args, **kwargs)


class DestroyModelMixin(drf_mixins.DestroyModelMixin):
    """
    Destroy a model instance.
    """

    pass


class PartialUpdateModelAtomicMixin(drf_mixins.UpdateModelMixin):
    """
    Update a model instance partial atomic.
    """

    @transaction.atomic
    def update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer: drf_serializers.Serializer) -> None:
        serializer.save()

    def partial_update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        kwargs["partial"] = True  # type: ignore
        return self.update(request, *args, **kwargs)


class PartialUpdateModelMixin(drf_mixins.UpdateModelMixin):
    """
    Update a model instance.
    """

    def update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        partial = False
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer: drf_serializers.Serializer) -> None:
        serializer.save()

    def partial_update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        kwargs["partial"] = True  # type: ignore
        return self.update(request, *args, **kwargs)
