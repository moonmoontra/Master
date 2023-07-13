from django import template

register = template.Library()


@register.filter()
def get_attr(obj, attr):
    return getattr(obj, attr)


@register.filter()
def has_get_absolute_url(obj, attr):
    attr_value = getattr(obj, attr, None)
    if attr_value and hasattr(attr_value, 'get_absolute_url') and callable(attr_value.get_absolute_url):
        return attr_value.get_absolute_url()
    else:
        return attr_value