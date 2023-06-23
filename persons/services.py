from django import forms

from persons.models import Provider


def filter_objects_delete(objects, list, **kwargs):
    return objects.filter(id__in=list, **kwargs).delete()


def get_fields_table(model):
    excluded_fields = ['create_date', 'update_date']
    return [field.name for field in model._meta.get_fields() if field.name not in excluded_fields]


def get_headers_table(model):
    return [model._meta.get_field(field_name).verbose_name for field_name in get_fields_table(model)]