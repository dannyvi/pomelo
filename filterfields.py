from django.db.models import fields
from django.db.models.fields import related


def _get_field_arg(field):
    kw = []
    if isinstance(field, (fields.CharField, fields.TextField)):
        kw = ['icontains', 'exact', 'isnull']
    elif isinstance(field, (fields.PositiveSmallIntegerField, fields.PositiveIntegerField,
                   fields.DateTimeField, fields.DateField, fields.TimeField)):
        kw =  ['lt', 'gt', 'exact', 'lte', 'gte']
    #elif isinstance(field, (related.ForeignKey, related.ManyToManyField)):
    #    return ['isnull']
    else:
        kw = ['exact']
    if field.null:
        kw.append('isnull')
    return kw


def get_filterset_fields(model):
    fields = model._meta.fields
    filterset_fields = dict()
    for field in fields:
        filterset_fields.update({field.name: _get_field_arg(field)})
    for m in model._meta.many_to_many:
        filterset_fields.update({m.name: _get_field_arg(m)})

    return filterset_fields
