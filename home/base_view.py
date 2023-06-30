# class BaseView:
#     template_name = None
#     model = None
#     form_class = None
#     success_url = None
#
#     def __init__(self, success_url:str):
#         self.success_url = success_url
#     def get_success_url(self):
#         return self.success_url + self.model.__name__.lower() + 's'
from home.services import get_model_context


# class BaseView():
#     paginate_by = 10
#     edit_view_name = None
#     delete_view_name = None
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update(get_model_context(self.model, self.edit_view_name, self.delete_view_name))
#         return context

