from django.contrib import admin

from .models import UnitOfMeasure, PriceName, ProductRefBook, ProductPriceName


@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_filter = ('unit_name',)


@admin.register(PriceName)
class PriceAdmin(admin.ModelAdmin):
    list_filter = ('price_name',)


@admin.register(ProductRefBook)
class ProductRefBookAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'unitOfMeasure', 'manufacturer')
    list_filter = ('articul',)


@admin.register(ProductPriceName)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'unitOfMeasure', 'coefficient')
    list_filter = ('price',)