import re
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


def get_model_context(model, url_string):
    context = {
        'headers': get_headers_table(model),
        'fields': get_fields_table(model),
        'model_name': model._meta.model_name.capitalize(),
        'url': url_string
    }
    return context


def get_fields_table(model):
    excluded_fields = ['create_date', 'update_date']
    return [field.name for field in model._meta.get_fields() if field.name not in excluded_fields]


def get_headers_table(model):
    return [model._meta.get_field(field_name).verbose_name for field_name in get_fields_table(model)]


def filter_objects_delete(objects, person_ids: list, **kwargs):
    return objects.filter(id__in=person_ids, **kwargs).delete()


def object_validation_only_text_field(_object):
    regex = r'^[""\'\'«»a-zA-ZА-Яа-яЁёЇїІіЄєҐґ\s]+$'
    if not re.match(regex, _object):
        raise ValidationError(_('Це поле не може містити цифри!'))

    print(_object)

    return _object
