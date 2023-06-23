from django.contrib import admin
from django.urls import path, re_path
from persons import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^providers/$', views.ProviderListView.as_view(), name='providers'),
    re_path(r'^manufacturers/$', views.ManufacturerListView.as_view(), name='manufacturers'),
]