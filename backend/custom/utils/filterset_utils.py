from typing import List
from django.db import models


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
}


def get_model_field_filter(model_field:models.Field) -> list:
    '''Get filter for specified model field'''
    return MODEL_FIELDS_FILTER_MAP.get(model_field.__class__, ['exact'])


def get_model_fields_filters(model_class:models.Model.__class__, prefix:str='', exclude:List[str]=[]) -> dict:
    '''Get filter for specified models.Model subclass fields'''
    return {f'{prefix}{field.name}': get_model_field_filter(field) for field in model_class._meta.get_fields() if field.name not in exclude}
