from django import template
register = template.Library()


@register.inclusion_tag('home/table.html')
def show_table(object_list):
    return {'object_list': object_list}