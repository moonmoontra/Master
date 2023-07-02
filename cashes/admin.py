from django.contrib import admin
from .models import Cash, Valuta, Rate


@admin.register(Cash)
class CashAdmin(admin.ModelAdmin):
    list_display = ('summa', 'valuta')


@admin.register(Valuta)
class ValutaAdmin(admin.ModelAdmin):
    list_display = ('valuta_name', 'valuta_short')


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('valuta', 'rate_value')
    list_filter = ('rate_date',)