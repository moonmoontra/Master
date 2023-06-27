from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView
from django.apps import apps

from persons.forms import *
from persons.models import Provider, Manufacturer, Employee
from home.services import filter_objects_delete, get_model_context, delete_objects


class BasePersonView:
    template_name = None
    model = None
    form_class = None
    success_url = '/persons/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower() + 's'


class BaseListView(BasePersonView, ListView):
    paginate_by = 10
    edit_view_name = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(self.model, self.edit_view_name))
        return context


class BaseCreateView(BasePersonView, CreateView):
    pass


class BaseEditView(BasePersonView, UpdateView):
    pass


class ProviderListView(BaseListView):
    template_name = 'persons/provider_list.html'
    edit_view_name = 'provider_edit'
    model = Provider


class ManufacturerListView(BaseListView):
    template_name = 'persons/manufacturer_list.html'
    edit_view_name = 'manufacturer_edit'
    model = Manufacturer


class EmployeeListView(BaseListView):
    template_name = 'persons/employees_list.html'
    edit_view_name = 'employee_edit'
    model = Employee


class ClientListView(BaseListView):
    template_name = 'persons/clients_list.html'
    edit_view_name = 'client_edit'
    model = Client


class ProviderCreateView(BaseCreateView):
    form_class = ProviderForm
    template_name = 'persons/provider_create.html'
    model = Provider


class ProviderEditView(BaseEditView):
    form_class = ProviderForm
    template_name = 'persons/provider_edit.html'
    model = Provider


class EmployeeCreateView(BaseCreateView):
    form_class = EmployeeForm
    template_name = 'persons/employee_create.html'
    model = Employee


class EmployeeEditView(BaseEditView):
    form_class = EmployeeForm
    template_name = 'persons/employee_edit.html'
    model = Employee


class ManufacturerCreateView(BaseCreateView):
    form_class = ManufacturerForm
    template_name = 'persons/manufacturer_create.html'
    model = Manufacturer


class ManufacturerEditView(BaseEditView):
    form_class = ManufacturerForm
    template_name = 'persons/manufacturer_edit.html'
    model = Manufacturer


class ClientCreateView(BaseCreateView):
    form_class = ClientForm
    template_name = 'persons/client_create.html'
    model = Client


class ClientEditView(BaseEditView):
    form_class = ClientForm
    template_name = 'persons/client_edit.html'
    model = Client


@require_POST
def delete_persons_view(request):
    model_name = request.POST.get('model_name')
    model = apps.get_model('persons', model_name)
    return delete_objects(request, model)