from django.db.models import fields


def _get_field_arg(cls):
    if cls in [fields.CharField, fields.TextField]:
        return ['icontains', 'exact']
    elif cls in [fields.PositiveSmallIntegerField,
                 fields.PositiveIntegerField]:
        return ['lt', 'gt', 'exact']
    else:
        return ['exact']


def get_filterset_fields(model):
    fields = model._meta.fields
    filterset_fields = dict()
    for field in fields:
        filterset_fields.update({field.name: _get_field_arg(field.__class__)})
    return filterset_fields
