from django.shortcuts import render
from django.views.generic import ListView
from persons.models import Provider
# Create your views here.

def index(request):
    return render(request, 'persons/index.html')


class ProviderListView(ListView):
    model = Provider
    template_name = 'provider_list.html'
    context_object_name = 'providersList'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headers'] = ['№', 'Назва', 'Місто', 'Адреса', 'Телефон', 'Статус']
        context['fields'] = ['id', 'provider_name', 'city', 'address', 'phone', 'status']
        return context
