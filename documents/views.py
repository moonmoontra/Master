from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView, DetailView
from django.apps import apps
from home.base_view import BaseListView
from documents.forms import DocumentForm, ProductInDocumentForm
from documents.models import Document, ProductInDocument
from home.services import delete_objects, update_object, get_all_sum_document
from home.set_htmx_or_django_template import CustomHtmxMixin


class BaseDocumentView:
    template_name = None
    model = None
    form_class = None
    success_url = '/documents/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower() + 's'


class BaseCreateView(BaseDocumentView, CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_htmx'] = self.template_htmx
        return context


class BaseEditView(BaseDocumentView, UpdateView):
    pass


class DocumentListView(CustomHtmxMixin, BaseListView, BaseDocumentView):
    template_name = 'documents/document_list.html'
    edit_view_name = 'document_detail'
    delete_view_name = 'delete_document'
    create_view_name = 'document_create'
    title = 'Документи'
    model = Document


class DocumentCreateView(CustomHtmxMixin, BaseCreateView):
    form_class = DocumentForm
    template_name = 'documents/document_create.html'
    model = Document


class DocumentEditView(BaseEditView):
    form_class = DocumentForm
    template_name = 'documents/document_edit.html'
    model = Document


class DocumentDetailView(DetailView):
    form_class = DocumentForm
    template_name = 'documents/document_detail.html'
    model = Document

    def get_all_sum(self):
        print(self.object)
        return get_all_sum_document(self.object)


class ProductInDocumentCreateView(CreateView):
    model = ProductInDocument
    form_class = ProductInDocumentForm
    template_name = 'documents/document_product_create.html'

    def get_document(self):
        return get_object_or_404(Document, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document'] = self.get_document()
        return context

    def get_initial(self):
        return {'document': self.get_document()}

    def form_valid(self, form):
        self.object = form.save()
        update_object(Document, self.kwargs['pk'], update_date=datetime.now())
        return super().form_valid(form)

    def get_success_url(self):
        url = '/documents/documents/document_detail/' + str(self.object.document.id)
        return url


# class ProductInDocumentEditView(BaseEditView):
#     form_class = ProductInDocumentForm
#     template_name = 'documents/document_edit.html'
#     model = ProductInDocument


@require_POST
def delete_documents_view(request):
    model_name = request.POST.get('model_name')
    model = apps.get_model('documents', model_name)
    return delete_objects(request, model)
