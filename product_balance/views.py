from django.shortcuts import render

from home.base_view import BaseListView
from home.set_htmx_or_django_template import CustomHtmxMixin
from product_balance.models import BalanceProduct


class BaseBalanceProductView:
    template_name = None
    model = None
    form_class = None
    success_url = '/balance_product/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower() + 's'


class BalanceProductListView(CustomHtmxMixin, BaseListView, BaseBalanceProductView):
    template_name = 'product_balance/product_balance_list.html'
    title = 'Залишки'
    model = BalanceProduct
