from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView

from home.services import get_model_context, delete_objects
from products.forms import UnitOfMeasureForm, ProductRefBookForm, ProductPriceNameForm, PriceNameForm
from products.models import PriceName, ProductPriceName, UnitOfMeasure, ProductRefBook
from django.apps import apps


class BaseProductView:
    template_name = None
    model = None
    form_class = None
    success_url = '/products/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower() + 's'


class BaseListView(BaseProductView, ListView):
    paginate_by = 10
    edit_view_name = None
    delete_view_name = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(self.model, self.edit_view_name, self.delete_view_name))
        return context


class BaseCreateView(BaseProductView, CreateView):
    pass


class BaseEditView(BaseProductView, UpdateView):
    pass


class ProductRefBookListView(BaseListView):
    model = ProductRefBook
    template_name = 'products/product_ref_book_list.html'
    edit_view_name = 'product_ref_book_edit'
    delete_view_name = 'delete_product'


class ProductRefBookEditView(BaseEditView):
    form_class = ProductRefBookForm
    model = ProductRefBook
    template_name = 'products/product_ref_book_edit.html'


class ProductRefBookCreateView(BaseCreateView):
    form_class = ProductRefBookForm
    model = ProductRefBook
    template_name = 'products/product_ref_book_create.html'


class ProductPriceNameListView(BaseListView):
    model = ProductPriceName
    template_name = 'products/product_price_list.html'
    edit_view_name = 'product_price_edit'
    delete_view_name = 'delete_product'


class ProductPriceNameCreateView(BaseCreateView):
    form_class = ProductPriceNameForm
    model = ProductPriceName
    template_name = 'products/product_price_create.html'


class ProductPriceNameEditView(BaseEditView):
    form_class = ProductPriceNameForm
    model = ProductPriceName
    template_name = 'products/product_price_edit.html'


class UnitOfMeasureListView(BaseListView):
    model = UnitOfMeasure
    template_name = 'products/unit_of_measure_list.html'
    edit_view_name = 'unit_of_measure_edit'
    delete_view_name = 'delete_product'


class UnitOfMeasureCreateView(BaseCreateView):
    form_class = UnitOfMeasureForm
    model = UnitOfMeasure
    template_name = 'products/unit_of_measure_create.html'


class UnitOfMeasureEditView(BaseEditView):
    form_class = UnitOfMeasureForm
    model = UnitOfMeasure
    template_name = 'products/unit_of_measure_edit.html'


class PriceNameListView(BaseListView):
    model = PriceName
    template_name = 'products/price_name_list.html'
    edit_view_name = 'price_name_edit'
    delete_view_name = 'delete_product'


class PriceNameCreateView(BaseCreateView):
    form_class = PriceNameForm
    model = PriceName
    template_name = 'products/price_name_create.html'


class PriceNameEditView(BaseEditView):
    form_class = PriceNameForm
    model = PriceName
    template_name = 'products/price_name_edit.html'


def delete_products_view(request):
    model_name = request.POST.get('model_name')
    model = apps.get_model('products', model_name)
    return delete_objects(request, model)

