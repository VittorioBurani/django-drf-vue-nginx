from typing import List
from django.db import models
from django_filters import rest_framework as filters


MODEL_FIELDS_FILTER_MAP = {
    # Relational fields:
    models.ForeignKey:      ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.ManyToManyField: ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.OneToOneField:   ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    # String related fields:
    models.CharField: ['exact', 'iexact', 'in', 'contains', 'icontains', 'regex', 'iregex'],
    models.TextField: ['exact', 'iexact', 'in', 'contains', 'icontains', 'regex', 'iregex'],
    # Integer related fields:
    models.IntegerField:              ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.PositiveIntegerField:      ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.SmallIntegerField:         ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.PositiveSmallIntegerField: ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.BigIntegerField:           ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.PositiveBigIntegerField:   ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.AutoField:                 ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.SmallAutoField:            ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.BigAutoField:              ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    # Floating point related fields:
    models.FloatField:   ['exact', 'gt', 'gte', 'lt', 'lte'],
    models.DecimalField: ['exact', 'gt', 'gte', 'lt', 'lte'],
    # DateTime related fields:
    models.DateTimeField: ['exact', 'gt', 'gte', 'lt', 'lte'],
    models.DateField:     ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    models.TimeField:     ['exact', 'in', 'gt', 'gte', 'lt', 'lte'],
    # Boolean Field:
    models.BooleanField: ['exact'],
    # JSON, Array, Dict Field:
    models.JSONField: [],
    # File Field:
    # set to empy list just to temporarily neutralize the issue:
    # https://github.com/carltongibson/django-filter/discussions/1506
    # https://github.com/carltongibson/django-filter/discussions/1478
    models.FileField: [],
}


def get_model_field_filter(model_field:models.Field) -> list:
    '''Get filter for specified model field'''
    return MODEL_FIELDS_FILTER_MAP.get(model_field.__class__, ['exact'])


def get_model_fields_filters(model_class:models.Model.__class__, prefix:str='', exclude:List[str]=[]) -> dict:
    '''Get filter for specified models.Model subclass fields'''
    return {f'{prefix}{field.name}': get_model_field_filter(field) for field in model_class._meta.get_fields() if field.name not in exclude}


class CommonModelFilter(filters.FilterSet):
    # This filter accepts a number but doesn't filter on a model field directly.
    # Instead, it calls the method 'filter_by_limit'.
    limit = filters.NumberFilter(method='filter_by_limit', label='Limit number of results')

    def filter_by_limit(self, queryset, name, value):
        """
        Orders the queryset by the 'id' field in descending order to get the
        latest objects, and then limits the result set to the number
        specified in the 'limit' query parameter.
        """
        # Ensure value is an integer before slicing
        try:
            limit = int(value)
        except (ValueError, TypeError):
            # If the value is invalid, just return the original queryset
            return queryset
        # `order_by('-id')` is a reliable way to get the "latest" objects.
        # You could also use a timestamp field like '-created_at'.
        return queryset.order_by('-id')[:limit]
