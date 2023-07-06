from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from home.base_view import BaseListView
from home.services import delete_objects
from home.set_htmx_or_django_template import CustomHtmxMixin
from stocks.forms import StockForm
from stocks.models import Stock
from django.apps import apps


class BaseStockView:
    template_name = None
    model = None
    form_class = None
    success_url = '/stocks/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower() + 's'


class BaseCreateView(BaseStockView, CreateView):
    pass


class BaseEditView(BaseStockView, UpdateView):
    pass


class StockListView(CustomHtmxMixin, BaseListView, BaseStockView):
    model = Stock
    template_name = 'stock/stocks_list.html'
    edit_view_name = 'stock_edit'
    delete_view_name = 'delete_stock'
    create_view_name = 'stock_create'


class StockEditView(BaseEditView):
    form_class = StockForm
    template_name = 'stock/stock_edit.html'
    model = Stock


class StockCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = StockForm
    template_name = 'stock/stock_create.html'
    model = Stock


def delete_stocks_view(request):
    model_name = request.POST.get('model_name')
    model = apps.get_model('stocks', model_name)
    return delete_objects(request, model)
