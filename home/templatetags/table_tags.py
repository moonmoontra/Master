from django import template
register = template.Library()


@register.inclusion_tag('home/table.html')
def show_table(object_list, headers, fields):
    return {'object_list': object_list,  'headers': headers, 'fields': fields}

@register.filter()
def get_attr(object, attr):
    return getattr(object, attr)
