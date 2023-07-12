from product_balance import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^balance_product/$', views.BalanceProductListView.as_view(), name='balance_product'),
]