from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView, DetailView
from django.apps import apps
from home.base_view import BaseListView
from documents.forms import DocumentForm, ProductInDocumentForm
from documents.models import Document, ProductInDocument
from home.services import delete_objects


class BaseDocumentView:
    template_name = None
    model = None
    form_class = None
    success_url = '/documents/'

    def get_success_url(self):
        return self.success_url + self.model.__name__.lower() + 's'


class BaseCreateView(BaseDocumentView, CreateView):
    pass


class BaseEditView(BaseDocumentView, UpdateView):
    pass


class DocumentListView(BaseListView, BaseDocumentView):
    template_name = 'documents/document_list.html'
    edit_view_name = 'document_detail'
    delete_view_name = 'delete_document'
    model = Document


class DocumentCreateView(BaseCreateView):
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


class ProductInDocumentCreateView(BaseCreateView):
    form_class = ProductInDocumentForm
    template_name = 'documents/document_product_create.html'
    model = ProductInDocument

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
