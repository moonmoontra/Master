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
        # for provider in context['providersList']:
        #     if provider.status == 'individual':
        #         context['providersList'][provider].status = 'Фізична особа'
        #     else:
        #         context['providersList'][provider].status = 'Юридична особа'
        context['headers'] = ['№', 'Назва', 'Місто', 'Адреса', 'Телефон', 'Статус']
        context['fields'] = ['id', 'provider_name', 'city', 'address', 'phone', 'status']
        #print(context['providersList'][0].status)
        return context