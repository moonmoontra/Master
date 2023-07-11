from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView
from django.apps import apps
from home.base_view import BaseListView, BaseCreateEditView
from cashes.forms import CashForm, ValutaForm, RateForm
from cashes.models import Cash, Valuta, Rate
from home.services import delete_objects
from home.set_htmx_or_django_template import CustomHtmxMixin


class BaseCashView:
    template_name = None
    model = None
    form_class = None
    success_url = '/cashes/'

    def get_success_url(self):
        if self.model.__name__ == 'Cash':
            return self.success_url + self.model.__name__.lower() + 'es'
        else:
            return self.success_url + self.model.__name__.lower() + 's'


class BaseCreateView(BaseCreateEditView, BaseCashView, CreateView):
    pass


class BaseEditView(BaseCreateEditView, BaseCashView, UpdateView):
    pass


class CashListView(CustomHtmxMixin, BaseListView, BaseCashView):
    template_name = 'cash/cash_list.html'
    edit_view_name = 'cash_edit'
    delete_view_name = 'delete_cash'
    create_view_name = 'cash_create'
    title = 'Каси'
    model = Cash


class CashCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = CashForm
    template_name = 'cash/cash_create.html'
    model = Cash


class CashEditView(CustomHtmxMixin, BaseEditView):
    form_class = CashForm
    template_name = 'cash/cash_edit.html'
    model = Cash


class ValutaListView(CustomHtmxMixin, BaseListView, BaseCashView):
    template_name = 'cash/valuta_list.html'
    edit_view_name = 'valuta_edit'
    delete_view_name = 'delete_cash'
    create_view_name = 'valuta_create'
    title = 'Валюти'
    model = Valuta


class ValutaCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = ValutaForm
    template_name = 'cash/valuta_create.html'
    model = Valuta


class ValutaEditView(CustomHtmxMixin, BaseEditView):
    form_class = ValutaForm
    template_name = 'cash/valuta_edit.html'
    model = Valuta


class RateListView(CustomHtmxMixin, BaseListView, BaseCashView):
    template_name = 'cash/rate_list.html'
    edit_view_name = 'rate_edit'
    delete_view_name = 'delete_cash'
    create_view_name = 'rate_create'
    title = 'Курси валют'
    model = Rate


class RateCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = RateForm
    template_name = 'cash/rate_create.html'
    model = Rate


class RateEditView(CustomHtmxMixin, BaseEditView):
    form_class = RateForm
    template_name = 'cash/rate_edit.html'
    model = Rate


@require_POST
def delete_cash_view(request):
    model_name = request.POST.get('model_name')
    model = apps.get_model('cashes', model_name)
    return delete_objects(request, model)