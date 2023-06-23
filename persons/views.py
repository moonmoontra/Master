from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView
from django.apps import apps

from persons.forms import ProviderCreateForm
from persons.models import Provider, Manufacturer, Employee
from persons.services import filter_objects_delete, get_model_context


def index(request):
    return render(request, 'persons/index.html')


class ProviderListView(ListView):
    model = Provider
    template_name = 'persons/provider_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(Provider))
        return context


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'persons/manufacturer_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(Manufacturer))
        return context


class EmployeeListView(ListView):
    model = Employee
    template_name = 'persons/employees_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(Manufacturer))
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
