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