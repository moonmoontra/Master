from products import views
from django.urls import path, re_path

urlpatterns = [
    re_path('products_ref_book/', views.ProductRefBookListView.as_view(), name='products_ref_book')
]