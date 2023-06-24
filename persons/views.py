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


class ProviderListView(ListView):
    paginate_by = 10
    model = Provider
    template_name = 'persons/provider_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(Provider, 'provider_edit'))
        return context


class ManufacturerListView(ListView):
    paginate_by = 10
    model = Manufacturer
    template_name = 'persons/manufacturer_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(Manufacturer, 'manufacturer_edit'))
        return context


class EmployeeListView(ListView):
    paginate_by = 10
    model = Employee
    template_name = 'persons/employees_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(Employee, 'employee_edit'))
        return context


class ClientListView(ListView):
    paginate_by = 10
    model = Clients
    template_name = 'persons/clients_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(Clients, 'client_edit'))
        return context


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


class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'persons/provider_create.html'
    form_class = ProviderCreateForm
    success_url = '/persons/providers'


class ProviderEditView(UpdateView):
    model = Provider
    success_url = '/persons/providers'
    template_name = 'persons/provider_edit.html'
    form_class = ProviderEditForm


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'persons/employee_create.html'
    form_class = EmployeeCreateForm
    success_url = '/persons/employees'


class EmployeeEditView(UpdateView):
    model = Employee
    template_name = 'persons/employee_edit.html'
    form_class = EmployeeEditForm
    success_url = '/persons/employees'


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    template_name = 'persons/manufacturer_create.html'
    form_class = ManufacturerCreateForm
    success_url = '/persons/manufacturers'


class ManufacturerEditView(UpdateView):
    model = Manufacturer
    success_url = '/persons/manufacturers'
    template_name = 'persons/manufacturer_edit.html'
    form_class = ManufacturerEditForm


class ClientCreateView(CreateView):
    model = Clients
    template_name = 'persons/client_create.html'
    form_class = ClientCreateForm
    success_url = '/persons/clients'


class ClientEditView(UpdateView):
    model = Clients
    success_url = '/persons/clients'
    template_name = 'persons/client_edit.html'
    form_class = ClientEditForm