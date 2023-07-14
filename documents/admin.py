from django.contrib import admin

from .models import Document, ProductInDocument


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_type', 'provider', 'stock', 'price_name', 'valuta', 'cash')
    list_filter = ('provider',)


@admin.register(ProductInDocument)
class ProductInDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'document', 'product', 'count', 'price')
    list_filter = ('document',)