from django.contrib import admin

from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_type', 'stock_id', 'price_name_id', 'valuta_id', 'cash_id')
    list_filter = ('provider_id',)