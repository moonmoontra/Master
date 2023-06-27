from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView

from home.services import get_model_context
from products.models import *


def index(request):
    return render(request, 'products/product_ref_book_list.html')


class ProductRefBookListView(ListView):
    model = ProductRefBook
    template_name = 'products/product_ref_book_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_model_context(self.model, 'manufacturer_edit'))
        return context


