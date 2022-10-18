from django_filters import rest_framework as filters


class FilterSet(filters.FilterSet):
    class Meta:
        fields = ()
