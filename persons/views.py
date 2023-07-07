from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView, ListView
from django.apps import apps
from home.base_view import BaseListView, BaseCreateEditMixin
from home.set_htmx_or_django_template import CustomHtmxMixin
from persons.forms import *
from persons.models import Provider, Manufacturer, Employee
from home.services import delete_objects


class BasePersonView:
    template_name = None
    model = None
    form_class = None
    success_url = '/persons/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower() + 's'


class BaseCreateView(BaseCreateEditMixin, BasePersonView, CreateView):
    pass


class BaseEditView(BaseCreateEditMixin, BasePersonView, UpdateView):
    pass


class ProviderListView(CustomHtmxMixin, BaseListView, BasePersonView):
    template_name = 'persons/provider_list.html'
    edit_view_name = 'provider_edit'
    delete_view_name = 'delete_person'
    create_view_name = 'provider_create'
    title = 'Контрагенти'
    model = Provider


class ManufacturerListView(CustomHtmxMixin, BaseListView, BasePersonView):
    template_name = 'persons/manufacturer_list.html'
    edit_view_name = 'manufacturer_edit'
    delete_view_name = 'delete_person'
    create_view_name = 'manufacturer_create'
    title = 'Виробники'
    model = Manufacturer


class EmployeeListView (CustomHtmxMixin, BaseListView, BasePersonView):
    template_name = 'persons/employees_list.html'
    edit_view_name = 'employee_edit'
    delete_view_name = 'delete_person'
    create_view_name = 'employee_create'
    title = 'Працівники'
    model = Employee


class ClientListView(CustomHtmxMixin, BaseListView, BasePersonView):
    template_name = 'persons/clients_list.html'
    edit_view_name = 'client_edit'
    delete_view_name = 'delete_person'
    create_view_name = 'client_create'
    title = 'Клієнти'
    model = Client


class ProviderCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = ProviderForm
    template_name = 'persons/provider_create.html'
    model = Provider


class ProviderEditView(CustomHtmxMixin, BaseEditView):
    form_class = ProviderForm
    template_name = 'persons/provider_edit.html'
    model = Provider


class EmployeeCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = EmployeeForm
    template_name = 'persons/employee_create.html'
    model = Employee


class EmployeeEditView(CustomHtmxMixin, BaseEditView):
    form_class = EmployeeForm
    template_name = 'persons/employee_edit.html'
    model = Employee


class ManufacturerCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = ManufacturerForm
    template_name = 'persons/manufacturer_create.html'
    model = Manufacturer


class ManufacturerEditView(CustomHtmxMixin, BaseEditView):
    form_class = ManufacturerForm
    template_name = 'persons/manufacturer_edit.html'
    model = Manufacturer


class ClientCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = ClientForm
    template_name = 'persons/client_create.html'
    model = Client


class ClientEditView(CustomHtmxMixin, BaseEditView):
    form_class = ClientForm
    template_name = 'persons/client_edit.html'
    model = Client


@require_POST
def delete_persons_view(request):
    model_name = request.POST.get('model_name')
    model = apps.get_model('persons', model_name)
    return delete_objects(request, model)
