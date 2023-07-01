from stocks import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^stocks/$', views.StockListView.as_view(), name='stocks'),
    re_path(r'^stocks/stock_edit/(?P<pk>\d+)$', views.StockEditView.as_view(),
            name='stock_edit'),
    re_path(r'^stocks/stock_create/$', views.StockCreateView.as_view(),
            name='stock_create'),
    re_path(r'^delete_stock/$', views.delete_stoks_view, name='delete_stock'),
]