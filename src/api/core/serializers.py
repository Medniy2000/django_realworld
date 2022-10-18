from __future__ import unicode_literals

from rest_framework import serializers as drf_serializers


class HyperlinkedRelatedField(drf_serializers.HyperlinkedIdentityField):
    pass


class Serializer(drf_serializers.Serializer):
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super(Serializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")
        self.user = getattr(self.request, "user", None)


class ModelSerializer(drf_serializers.ModelSerializer):
    serializer_url_field = HyperlinkedRelatedField

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super(ModelSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")
        self.user = getattr(self.request, "user", None)


class HyperlinkedModelSerializer(ModelSerializer):
    """
    A type of `ModelSerializer` that uses hyperlinked relationships instead
    of primary key relationships. Specifically:

    * A 'url' field is included instead of the 'id' field.
    * Relationships to other instances are hyperlinks, instead of primary keys.
    """

    pass
