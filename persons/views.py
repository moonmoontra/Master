from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView
from django.apps import apps

from persons.forms import *
from persons.models import Provider, Manufacturer, Employee
from persons.services import filter_objects_delete, get_model_context


def index(request):
    return render(request, 'persons/index.html')


class BaseListView(ListView):
    paginate_by = 10
    edit_view_name = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(self.model, self.edit_view_name))
        return context


class BaseCreateView(CreateView):
    template_name = None
    success_url = '/persons/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower() + 's'


class BaseEditView(UpdateView):
    template_name = None
    success_url = '/persons/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower() + 's'


class ProviderListView(BaseListView):
    model = Provider
    template_name = 'persons/provider_list.html'
    edit_view_name = 'provider_edit'


class ManufacturerListView(BaseListView):
    model = Manufacturer
    template_name = 'persons/manufacturer_list.html'
    edit_view_name = 'manufacturer_edit'


class EmployeeListView(BaseListView):
    model = Employee
    template_name = 'persons/employees_list.html'
    edit_view_name = 'employee_edit'


class ClientListView(BaseListView):
    model = Clients
    template_name = 'persons/clients_list.html'
    edit_view_name = 'client_edit'


class ProviderCreateView(BaseCreateView):
    model = Provider
    form_class = ProviderCreateForm
    template_name = 'persons/provider_create.html'


class ProviderEditView(BaseEditView):
    model = Provider
    form_class = ProviderEditForm
    template_name = 'persons/provider_edit.html'


class EmployeeCreateView(BaseCreateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'persons/employee_create.html'


class EmployeeEditView(BaseEditView):
    model = Employee
    form_class = EmployeeEditForm
    template_name = 'persons/employee_edit.html'


class ManufacturerCreateView(BaseCreateView):
    model = Manufacturer
    form_class = ManufacturerCreateForm
    template_name = 'persons/manufacturer_create.html'


class ManufacturerEditView(BaseEditView):
    model = Manufacturer
    form_class = ManufacturerEditForm
    template_name = 'persons/manufacturer_edit.html'


class ClientCreateView(BaseCreateView):
    model = Clients
    form_class = ClientCreateForm
    template_name = 'persons/client_create.html'


class ClientEditView(BaseEditView):
    model = Clients
    form_class = ClientEditForm
    template_name = 'persons/client_edit.html'


@require_POST
def delete_persons_view(request):
    try:
        url = request.META.get('HTTP_REFERER')
        model_name = request.POST.get('model_name')
        model = apps.get_model('persons', model_name)
        person_ids = request.POST.getlist('person_ids')

        if model and person_ids:
            filter_objects_delete(model.objects, person_ids=person_ids)
        return redirect(url)
    except (LookupError, ValueError):
        return HttpResponse("Помилка видалення.")