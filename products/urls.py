from products import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^productrefbooks/$', views.ProductRefBookListView.as_view(), name='products_ref_book'),
    re_path(r'^productrefbooks/product_ref_book_edit/(?P<pk>\d+)$', views.ProductRefBookEditView.as_view(),
            name='product_ref_book_edit'),
    re_path(r'^productrefbooks/product_ref_book_create/$', views.ProductRefBookCreateView.as_view(),
            name='product_ref_book_create'),
    re_path(r'^products_price/$', views.ProductPriceListView.as_view(), name='products_price'),
    re_path(r'^unit_of_measure/$', views.UnitOfMeasureListView.as_view(), name='unit_of_measure'),
    re_path(r'^delete_products/$', views.delete_products_view, name='delete_products'),
]