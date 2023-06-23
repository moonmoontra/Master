from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.apps import apps

from persons.forms import ProviderCreateForm
from persons.models import Provider, Manufacturer, Employee
from persons.services import filter_objects_delete, get_fields_table, get_headers_table


# Create your views here.

def index(request):
    return render(request, 'persons/index.html')


class ProviderListView(ListView):
    model = Provider
    template_name = 'persons/provider_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контрагенти'
        context['headers'] = get_headers_table(Provider)
        context['fields'] = get_fields_table(Provider)
        context['model_name'] = 'Provider'
        return context


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'persons/manufacturer_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Виробники'
        context['headers'] = get_headers_table(Manufacturer)
        context['fields'] = get_fields_table(Manufacturer)
        context['model_name'] = 'Manufacturer'
        return context


class EmployeeListView(ListView):
    model = Employee
    template_name = 'persons/employees_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Працівники'
        context['headers'] = get_headers_table(Employee)
        context['fields'] = get_fields_table(Employee)
        context['model_name'] = 'Employee'
        return context


def delete_persons_view(request):
    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        model_name = request.POST.get('model_name')
        model = apps.get_model('persons', model_name)
        person_ids = request.POST.getlist('person_ids')
        filter_objects_delete(model.objects, list=person_ids)
        return redirect(url)
    else:
        return HttpResponse("Метод запроса не поддерживается.")


class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'persons/provider_create.html'
    form_class = ProviderCreateForm
    success_url = '/persons/providers'
