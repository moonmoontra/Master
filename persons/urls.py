from django.contrib import admin
from django.urls import path, re_path
from persons import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^providers/$', views.ProviderListView.as_view(), name='providers'),
    re_path(r'^manufacturers/$', views.ManufacturerListView.as_view(), name='manufacturers'),
    re_path(r'^employees/$', views.EmployeeListView.as_view(), name='employees'),
    re_path(r'^delete_person/$', views.delete_persons_view, name='delete_person'),
    re_path(r'^providers/provider_create/$', views.ProviderCreateView.as_view(), name='provider_create'),
    re_path(r'^providers/provider_edit/(?P<pk>\d+)$', views.ProviderEditView.as_view(), name='provider_edit'),
    re_path(r'^employees/employee_create/$', views.EmployeeCreateView.as_view(), name='employee_create'),
    re_path(r'^manufacturers/manufacturer_create/$', views.ManufacturerCreateView.as_view(), name='manufacturer_create'),
    re_path(r'^manufacturer_edit/(?P<pk>\d+)$', views.ManufacturerEditView.as_view(), name='manufacturer_edit'),
]