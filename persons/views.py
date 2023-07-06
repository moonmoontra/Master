from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView
from django.apps import apps
from home.base_view import BaseListView
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


class BaseCreateView(BasePersonView, CreateView):
    pass


class BaseEditView(BasePersonView, UpdateView):
    pass


class CustomHtmxMixin(BasePersonView):
    def dispatch(self, request, *args, **kwargs):
        self.template_htmx = self.template_name
        if not self.request.META.get('HTTP_HX_REQUEST'):
            self.template_name = 'home/include_base_block.html'
        return super().dispatch(request, *args, **kwargs)


class ProviderListView(CustomHtmxMixin, BaseListView, BasePersonView):
    template_name = 'persons/provider_list.html'
    edit_view_name = 'provider_edit'
    delete_view_name = 'delete_person'
    create_view_name = 'provider_create'
    model = Provider


class ManufacturerListView(CustomHtmxMixin, BaseListView, BasePersonView):
    template_name = 'persons/manufacturer_list.html'
    edit_view_name = 'manufacturer_edit'
    delete_view_name = 'delete_person'
    create_view_name = 'manufacturer_create'
    model = Manufacturer


class EmployeeListView(CustomHtmxMixin, BaseListView, BasePersonView):
    template_name = 'persons/employees_list.html'
    edit_view_name = 'employee_edit'
    delete_view_name = 'delete_person'
    create_view_name = 'employee_create'
    model = Employee


class ClientListView(CustomHtmxMixin, BaseListView, BasePersonView):
    template_name = 'persons/clients_list.html'
    edit_view_name = 'client_edit'
    delete_view_name = 'delete_person'
    create_view_name = 'client_create'
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
