from django import template

from persons.services import DeleteObjectService

register = template.Library()


@register.inclusion_tag('home/table.html')
def show_table(object_list, title, headers, fields, model_name):
    return {'object_list': object_list, 'title': title, 'headers': headers, 'fields': fields, 'model_name': model_name}

@register.filter()
def get_attr(object, attr):
    return getattr(object, attr)

@register.simple_tag
def delete_objects(model, object_ids):
    delete_objects_service = DeleteObjectService()
    delete_objects_service.execute(model=model, object_ids=object_ids)