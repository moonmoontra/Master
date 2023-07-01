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
    provider_id = models.ForeignKey(Provider, default=None, on_delete=models.SET_DEFAULT, verbose_name='Постачальник',
                                    related_name='provider_documents')
    stock_id = models.ForeignKey(Stock, on_delete=models.PROTECT, verbose_name='Склад', related_name='stock_documents')
    price_name_id = models.ForeignKey(PriceName, on_delete=models.PROTECT, verbose_name='Тип ціни',
                                      related_name='pricename_documents')
    valuta_id = models.ForeignKey(Valuta, default=None, on_delete=models.SET_DEFAULT, verbose_name='Валюта',
                                  related_name='valute_documents')
    cash_id = models.ForeignKey(Cash, on_delete=models.PROTECT, verbose_name='Каса', related_name='cash_documents')

    def __str__(self):
        return '[{document_number}] {create_date}'.format(document_number=self.document_number,
                                                          create_date=self.create_date)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документи'
        ordering = ['-document_number', 'provider_id']

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
    product_id = models.ForeignKey(ProductRefBook, on_delete=models.PROTECT, verbose_name='Товар',
                                   related_name='products_in_document')
    count = models.PositiveIntegerField(verbose_name='Кількість')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')

    def __str__(self):
        return '{product_id}[{count}]'.format(product_id=self.product_id,
                                                          count=self.count)
    @property
    def sum(self):
        return self.count * self.price

    class Meta:
        verbose_name = 'Товар в документі'
        verbose_name_plural = 'Товари в документі'


class StockMovementDocument(BaseData):
    stock_start = models.ForeignKey(Stock, default=None, on_delete=models.SET_DEFAULT, verbose_name='Зі складу',
                                    related_name='stock_start_documents')
    stock_end = models.ForeignKey(Stock, default=None, on_delete=models.SET_DEFAULT, verbose_name='На склад',
                                  related_name='stock_end_documents')

    def __str__(self):
        return '[{pk}] {stock_start} -> {stock_end}'.format(pk=self.pk, stock_start=self.stock_start,
                                                            stock_end=self.stock_end)

    class Meta:
        verbose_name = 'Документ переміщення'
        verbose_name_plural = 'Документи переміщення'


class StockMovementDocumentProduct(models.Model):
    product_id = models.ForeignKey(ProductRefBook, on_delete=models.PROTECT, verbose_name='Товар',
                                   related_name='products_in_stock_movement_document')
    count = models.PositiveIntegerField(verbose_name='Кількість')

    def __str__(self):
        return '{product_id}[{count}]'.format(product_id=self.product_id, count=self.count)

    class Meta:
        verbose_name = 'Товар в документі переміщення'
        verbose_name_plural = 'Товари в документі переміщення'