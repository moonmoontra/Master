from django.contrib import admin
from .models import BalanceProduct


@admin.register(BalanceProduct)
class BalanceProductAdmin(admin.ModelAdmin):
    list_display = ('document', 'stock', 'count', 'sum')