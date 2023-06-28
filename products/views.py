from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView

from home.services import get_model_context, delete_objects
from products.forms import *
from products.models import *
from django.apps import apps

def index(request):
    return render(request, 'products/product_ref_book_list.html') + 's'


class BaseProductView:
    template_name = None
    model = None
    form_class = None
    success_url = '/products/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower()


class BaseListView(BaseProductView, ListView):
    paginate_by = 10
    edit_view_name = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(self.model, self.edit_view_name))
        return context


class BaseCreateView(BaseProductView, CreateView):
    pass


class BaseEditView(BaseProductView, UpdateView):
    pass


class ProductRefBookListView(BaseListView):
    model = ProductRefBook
    template_name = 'products/product_ref_book_list.html'
    edit_view_name = 'product_ref_book_edit'


class ProductRefBookEditView(BaseEditView):
    form_class = ProductRefBookForm
    model = ProductRefBook
    template_name = 'products/product_ref_book_edit.html'


class ProductRefBookCreateView(BaseCreateView):
    form_class = ProductRefBookForm
    model = ProductRefBook
    template_name = 'products/product_ref_book_create.html'


class ProductPriceListView(BaseListView):
    model = ProductPrice
    template_name = 'products/product_price_list.html'
    edit_view_name = 'manufacturer_edit'


def delete_products_view(request):
    model_name = request.POST.get('model_name')
    model = apps.get_model('products', model_name)
    return delete_objects(request, model)

