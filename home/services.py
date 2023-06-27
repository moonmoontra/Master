import re
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.http import HttpResponse
from django.apps import apps

from persons.models import Manufacturer


# from persons import apps


def get_model_context(model, url_for_edit):
    context = {
        'headers': get_headers_table(model),
        'fields': get_fields_table(model),
        'model_name': model._meta.model_name.capitalize(),
        'url_for_edit': url_for_edit
    }
    return context


def get_fields_table(model):
    # excluded_models = ['ProductRefBook', 'Manufacturer']
    excluded_fields = ['create_date', 'update_date', 'manufacturer_products', 'productrefbook_products']
    return [field.name for field in model._meta.get_fields() if field.name not in excluded_fields]
    # or
    # model._meta.model_name not in excluded_models


def get_headers_table(model):
    print(['№' if field_name == 'id' else model._meta.get_field(field_name).verbose_name
            for field_name in get_fields_table(model)])
    return ['№' if field_name == 'id' else model._meta.get_field(field_name).verbose_name
            for field_name in get_fields_table(model)]


def delete_objects(request):
    try:
        url = request.META.get('HTTP_REFERER')
        model_name = request.POST.get('model_name')
        model = apps.get_model('persons', model_name)
        object_ids = request.POST.getlist('object_ids')

        if model and object_ids:
           filter_objects_delete(model.objects, object_ids)
        return redirect(url)
    except(LookupError, ValueError):
        return HttpResponse("Помилка видалення.")


def filter_objects_delete(objects, object_ids: list, **kwargs):
    return objects.filter(id__in=object_ids, **kwargs).delete()


def object_validation_only_text_field(_object):
    regex = r'^[""\'\'«»a-zA-ZА-Яа-яЁёЇїІіЄєҐґ\s]+$'
    if not re.match(regex, _object):
        raise ValidationError(_('Це поле не може містити цифри!'))

    return _object