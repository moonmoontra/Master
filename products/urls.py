from products import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^productrefbooks/$', views.ProductRefBookListView.as_view(), name='product_ref_books'),
    re_path(r'^productrefbooks/product_ref_book_edit/(?P<pk>\d+)$', views.ProductRefBookEditView.as_view(),
            name='product_ref_book_edit'),
    re_path(r'^productrefbooks/product_ref_book_create/$', views.ProductRefBookCreateView.as_view(),
            name='product_ref_book_create'),
    re_path(r'^productprices/$', views.ProductPriceNameListView.as_view(), name='product_prices'),
    re_path(r'^productprices/product_price_create/$', views.ProductPriceNameCreateView.as_view(), name='product_price_create'),
    re_path(r'^productprices/product_price_edit/(?P<pk>\d+)$', views.ProductPriceNameEditView.as_view(), name='product_price_edit'),
    re_path(r'^unitofmeasures/$', views.UnitOfMeasureListView.as_view(), name='unit_of_measure'),
    re_path(r'^unitofmeasures/unit_of_measure_create/$', views.UnitOfMeasureCreateView.as_view(), name='unit_of_measure_create'),
    re_path(r'^unitofmeasures/unit_of_measure_edit/(?P<pk>\d+)$', views.UnitOfMeasureEditView.as_view(), name='unit_of_measure_edit'),
    re_path(r'^pricenames/$', views.PriceNameListView.as_view(), name='price_names'),
    re_path(r'^pricenames/price_name_create/$', views.PriceNameCreateView.as_view(), name='price_name_create'),
    re_path(r'^pricenames/price_name_edit/(?P<pk>\d+)$', views.PriceNameEditView.as_view(), name='price_name_edit'),
    re_path(r'^delete_product/$', views.delete_products_view, name='delete_product'),
]