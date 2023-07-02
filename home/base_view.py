from django.views.generic import ListView

from home.services import get_model_context


class BaseListView(ListView):
    paginate_by = 10
    edit_view_name = None
    delete_view_name = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.model._meta.model_name == 'productpricename':
            context.update(get_model_context(self.model, self.edit_view_name, self.delete_view_name, False))
        elif self.model._meta.model_name == 'document':
            context.update(get_model_context(self.model, self.edit_view_name, self.delete_view_name, False))
        else:
            context.update(get_model_context(self.model, self.edit_view_name, self.delete_view_name))
        return context