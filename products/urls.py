from products import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='products')
]