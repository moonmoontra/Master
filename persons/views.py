from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.apps import apps

from home.templatetags.table_tags import delete_objects
from persons.forms import ProviderCreateForm
from persons.models import Provider, Manufacturer, Employee
from persons.services import filter_objects_delete


# Create your views here.

def index(request):
    return render(request, 'persons/index.html')


class ProviderListView(ListView):
    model = Provider
    template_name = 'persons/provider_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['provider_title'] = 'Контрагенти'
        context['headers'] = ['№', 'Назва', 'Місто', 'Адреса', 'Телефон', 'Статус']
        context['fields'] = ['id', 'provider_name', 'city', 'address', 'phone', 'status']
        context['model_name'] = 'Provider'
        return context


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'persons/manufacturer_list.html'
    context_object_name = 'manufacturersList'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manufacturer_title'] = 'Виробники'
        context['headers'] = ['№', "Назва або Ім'я", 'Країна']
        context['fields'] = ['id', 'manufacturer_name', 'country']
        context['model_name'] = 'Manufacturer'
        return context


class EmployeeListView(ListView):
    model = Employee
    template_name = 'persons/employees_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_title'] = 'Працівники'
        context['headers'] = ['№', "Ім'я", 'Прізвище', 'Номер контракту', 'Посада', 'Телефон', 'Адреса', 'Дата прийняття', 'Дата звільнення']
        context['fields'] = ['id', 'first_name', 'last_name', 'contract', 'position', 'phone', 'address', 'start_date', 'end_date']
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


class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'persons/provider_list.html'
    form_class = ProviderCreateForm