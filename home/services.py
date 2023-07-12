import re

from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.http import HttpResponse
from django.apps import apps

from documents.models import Document
from product_balance.models import BalanceProduct

"""get_model_context - метод возвращающий словарь контекста во views.py...
    model - модель, для которой нужно получить контекст
    url_for_edit - url для редактирования объекта, например: 'manufacturer_edit'
    url_for_delete - url для удаления объекта, например: 'manufacturer_delete'
    url_for_create - url для создания объекта, например: 'manufacturer_create'
    exclude - исключить определенные поля из контекста, по умолчанию True"""


def get_model_context(model, url_for_edit: str, url_for_delete: str,
                      url_for_create: str, title: str, exclude: bool = True) -> dict:
    context = {
        'headers': get_headers_table(model, exclude),
        'fields': get_fields_table(model, exclude),
        'model_name': model._meta.model_name.capitalize(),
        'url_for_edit': url_for_edit,
        'url_for_delete': url_for_delete,
        'url_for_create': url_for_create,
        'title': title,
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
    excluded_fields_related_name = get_all_related_names()
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


"""get_all_related_names - метод для получения всех связанных полей...
    related_names - список связанных полей
    all_models - список всех моделей"""


def get_all_related_names():
    related_names = []
    all_models = apps.get_models()
    for model in all_models:
        for field in model._meta.get_fields():
            if hasattr(field, 'related_name') and field.related_name:
                related_names.append(field.related_name)
    return related_names


"""update_object - метод для обновления объекта...
    model - модель, для которой нужно обновить объект
    object_id - id объекта, который нужно обновить
    kwargs - дополнительные параметры для обновления объекта
    (например, если в модели Document нужно обновить поле update_date,
    то в kwargs передаем update_date=timezone.now()
    полный пример вызова: update_object(Document, 1, update_date=timezone.now()))"""


def update_object(model, object_id: int, **kwargs: dict):
    return model.objects.filter(id=object_id).update(**kwargs)


""" get_all_sum_document - метод для получения общей цены товаров в документе...
    _object - объект, для которого нужно получить общую цену товаров
    sum - общая цена товаров в документе
    product_in_document.sum - цена товара в документе
    _object.products_in_document.all() - все товары в документе"""


def get_all_sum_document(_object: object) -> Sum:
    return sum([product_in_document.sum for product_in_document in _object.products_in_document.all()])


def product_balancing(document: Document, hold: bool) -> None:
    products = document.products_in_document.all()
    for product in products:
        if hold:
            BalanceProduct.objects.create(document=document, product_in_document=product,
                                          stock=document.stock, count=product.count)
        else:
            BalanceProduct.objects.filter(document=document, product_in_document=product).delete()


def holding_accept(document: Document) -> None:
    products = document.products_in_document.all()
    count_in_stock = 0
    for product in products:
        balance_products = BalanceProduct.objects.filter(product_in_document=product)
        for balance_product in balance_products:
            count_in_stock += balance_product.count

    print(count_in_stock)