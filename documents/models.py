from django.db import models

from persons.models import Provider
from products.models import PriceName, ProductRefBook
from stocks.models import Stock
from cash.models import Valuta, Cash


class BaseData(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Створено:')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Редаговано:')

    class Meta:
        abstract = True


class Document(BaseData):
    TYPE_DOCUMENT = (
        ('receipt', 'Прихід'),
        ('expense', 'Витрата'),
    )

    document_number = models.AutoField()
    document_type = models.CharField(max_length=10, choices=TYPE_DOCUMENT, verbose_name='Тип документу')
    provider_id = models.ForeignKey(Provider, on_delete=models.PROTECT, verbose_name='Постачальник',
                                    related_name='provider_documents')
    stck_id = models.ForeignKey(Stock, on_delete=models.PROTECT, verbose_name='Склад', related_name='stock_documents')
    price_name_id = models.ForeignKey(PriceName, on_delete=models.PROTECT, verbose_name='Тип ціни',
                                      related_name='pricename_documents')
    valuta_id = models.ForeignKey(Valuta, on_delete=models.PROTECT, verbose_name='Валюта',
                                  related_name='valute_documents')
    cash_id = models.ForeignKey(Cash, on_delete=models.PROTECT, verbose_name='Каса', related_name='cash_documents')

    def save(self, *args, **kwargs):
        if not self.pk:
            last_object = Document.objects.order_by('-id').first()
            if last_object:
                last_id = int(last_object.id)
                new_id = str(last_id + 1).zfill(9)
                self.document_number = new_id
            else:
                self.document_number = '000000001'
        super().save(args, **kwargs)


class ProductInDocument(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Документ', related_name='documents')
    product_id = models.ForeignKey(ProductRefBook, on_delete=models.CASCADE, verbose_name='Товар',
                                   related_name='products_in_document')
    count = models.PositiveIntegerField(verbose_name='Кількість')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')

    @property
    def sum(self):
        return self.count * self.price


class StockMovementDocument(BaseData):
    stock_start = models.ForeignKey(Stock, on_delete=models.PROTECT, verbose_name='Зі складу',
                                    related_name='stock_start_documents')
    stock_end = models.ForeignKey(Stock, on_delete=models.PROTECT, verbose_name='На склад',
                                  related_name='stock_end_documents')


class StockMovementDocumentProduct(models.Model):
    product_id = models.ForeignKey(ProductRefBook, on_delete=models.CASCADE, verbose_name='Товар',
                                   related_name='products_in_stock_movement_document')
    count = models.PositiveIntegerField(verbose_name='Кількість')