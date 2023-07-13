from django import template

register = template.Library()

"""get_attr - пользовательский тег, который позволяет получить значение атрибута объекта по его имени.
Использование: {{ object|get_attr:"attr_name" }}"""


@register.filter()
def get_attr(obj, attr):
    return getattr(obj, attr)


"""has_get_absolute_url - пользовательский тег, который проверяет есть ли у атрибута метод get_absolute_url
Использование: {{ object|has_get_absolute_url:"attr_name" }}"""


@register.filter()
def has_get_absolute_url(obj, attr):
    attr_value = getattr(obj, attr, None)
    if attr_value and hasattr(attr_value, 'get_absolute_url'):
        return attr_value.get_absolute_url()
