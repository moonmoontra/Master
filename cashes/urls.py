from cashes import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^valutas/$', views.ValutaListView.as_view(), name='valutas'),
    re_path(r'^valutas/valuta_edit/(?P<pk>\d+)$', views.ValutaEditView.as_view(), name='valuta_edit'),
    re_path(r'^valutas/valuta_create/$', views.ValutaCreateView.as_view(), name='valuta_create'),
    re_path(r'^cashes/$', views.CashListView.as_view(), name='cashes'),
    re_path(r'^cashes/cash_edit/(?P<pk>\d+)$', views.CashEditView.as_view(), name='cash_edit'),
    re_path(r'^cashes/cash_create/$', views.CashCreateView.as_view(), name='cash_create'),
    re_path(r'^rates/$', views.RateListView.as_view(), name='rates'),
    re_path(r'^rates/rate_edit/(?P<pk>\d+)$', views.RateEditView.as_view(), name='rate_edit'),
    re_path(r'^rates/rate_create/$', views.RateCreateView.as_view(), name='rate_create'),
    re_path(r'^delete_cash/$', views.delete_cash_view, name='delete_cash'),
]