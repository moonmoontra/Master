from django.contrib import admin

from .models import UnitOfMeasure, Price, GoodRefBook, GoodPrice


@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_filter = ('unit_name',)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_filter = ('price_name',)


@admin.register(GoodRefBook)
class GoodRefBookAdmin(admin.ModelAdmin):
    list_display = ('good_name', 'unitOfMeasure')
    list_filter = ('articul', 'manufacturer')


@admin.register(GoodPrice)
class GoodPriceAdmin(admin.ModelAdmin):
    list_display = ('good', 'unitOfMeasure', 'coefficient')
    list_filter = ('price',)