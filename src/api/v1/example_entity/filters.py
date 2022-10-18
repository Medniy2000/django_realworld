from src.api.core.filters.filters_sets import FilterSet
from django_filters import rest_framework as filters

from src.core.models import ExampleModel


class ExampleModelFilterSet(FilterSet):
    created_at_max = filters.UUIDFilter(lookup_expr="lte", field_name="created_at")

    class Meta:
        model = ExampleModel
        fields = ["example_field"]
