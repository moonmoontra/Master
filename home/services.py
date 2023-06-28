import re
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.http import HttpResponse

"""get_model_context - метод возвращающий словарь контекста во views.py...
   model - модель, для которой нужно получить контекст
   url_for_edit - url для редактирования объекта, например: 'manufacturer_edit'
   exclude - исключить определенные поля из контекста, по умолчанию True"""


def get_model_context(model, url_for_edit: str, url_for_delete: str, exclude: bool = True) -> dict:
    context = {
        'headers': get_headers_table(model, exclude),
        'fields': get_fields_table(model, exclude),
        'model_name': model._meta.model_name.capitalize(),
        'url_for_edit': url_for_edit,
        'url_for_delete': url_for_delete,
    }
    return context


"""get_fields_table - метод возвращающий список полей модели...
    model - модель, для которой нужно получить список полей
    exclude - исключить определенные поля из списка, по умолчанию True
    excluded_models_date - список полей модели, которые нужно исключить из списка
    excluded_fields_related_name - список полей модели,
     которые нужно исключить из списка (related_name(связанные поля))"""


def get_fields_table(model, exclude: bool = True) -> list:
    excluded_models_date = ['create_date', 'update_date']
    excluded_fields_related_name = ['manufacturer_products', 'productrefbook_products', 'unitofmeasure_products',
                                    'unitofmeasure_price_products', 'pricename_products']
    if exclude:
        return [field.name for field in model._meta.get_fields()
                if field.name not in excluded_fields_related_name and field.name not in excluded_models_date]
    else:
        return [field.name for field in model._meta.get_fields()
                if field.name not in excluded_fields_related_name]


"""get_headers_table - метод возвращающий список заголовков таблицы...
    model - модель, для которой нужно получить список заголовков таблицы
    exclude - исключить определенные поля из списка, по умолчанию True"""


def get_headers_table(model, exclude: bool) -> list:
    return ['№' if field_name == 'id' else model._meta.get_field(field_name).verbose_name
            for field_name in get_fields_table(model, exclude)]


"""delete_objects - метод для удаления нескольких или одного объектов...
    model_name - название модели, для которой нужно удалить объекты
    object_ids - список id объектов, которые нужно удалить
    model - модель, для которой нужно удалить объекты"""


def delete_objects(request, model):
    try:
        url = request.META.get('HTTP_REFERER')
        object_ids = request.POST.getlist('object_ids')

        print(object_ids, model)

        if model and object_ids:
            filter_objects_delete(model.objects, object_ids)
        return redirect(url)
    except(LookupError, ValueError):
        return HttpResponse("Помилка видалення.")


"""filter_objects_delete - метод для фильтрации и удаления объектов...
    objects - менеджер модели, для которой нужно удалить объекты
    object_ids - список id объектов, которые нужно удалить
    kwargs - дополнительные параметры для фильтрации объектов"""


def filter_objects_delete(objects, object_ids: list, **kwargs):
    return objects.filter(id__in=object_ids, **kwargs).delete()


"""object_validation_only_text_field - метод для валидации текстовых полей...
    _object - объект, который нужно валидировать"""


def object_validation_only_text_field(_object):
    regex = r'^[""\'\'«»a-zA-ZА-Яа-яЁёЇїІіЄєҐґ\s]+$'
    if not re.match(regex, _object):
        raise ValidationError(_('Це поле не може містити цифри!'))

    return _object
