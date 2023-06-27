from django.contrib import admin

from .models import UnitOfMeasure, Price, ProductRefBook, ProductPrice


@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_filter = ('unit_name',)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_filter = ('price_name',)


@admin.register(ProductRefBook)
class ProductRefBookAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'unitOfMeasure', 'manufacturer')
    list_filter = ('articul',)


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'unitOfMeasure', 'coefficient')
    list_filter = ('price',)