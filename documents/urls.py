from documents import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^documents/$', views.DocumentListView.as_view(), name='documents'),
    re_path(r'^documents/document_edit/(?P<pk>\d+)$', views.DocumentEditView.as_view(),
            name='document_edit'),
    re_path(r'^documents/document_create/$', views.DocumentCreateView.as_view(),
            name='document_create'),
    re_path(r'^documents/document_detail/(?P<pk>\d+)$', views.DocumentDetailView.as_view(),
            name='document_detail'),
    re_path(r'^documents/document_product_create/(?P<pk>\d+)$', views.ProductInDocumentCreateView.as_view(),
            name='document_product_create'),
    re_path(r'^documents/document_product_edit/(?P<pk>\d+)$', views.ProductInDocumentEditView.as_view(),
            name='document_product_edit'),
    re_path(r'^documents/document_hold_edit/(?P<pk>\d+)$', views.DocumentHoldEditView.as_view(),
            name='document_hold_edit'),
    re_path(r'^documents/document_paid_edit/(?P<pk>\d+)$', views.DocumentPaidEditView.as_view(),
            name='document_paid_edit'),
    re_path(r'^delete_document/$', views.delete_documents_view, name='delete_document'),
]