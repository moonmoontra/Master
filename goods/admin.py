from django.contrib import admin

from .models import UnitOfMeasure, Price


@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_filter = ('unit_name',)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_filter = ('price_name',)
