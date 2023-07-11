from django.db import models

from documents.models import Document
from home.models import BaseData
from stocks.models import Stock


class BalanceProduct(BaseData):
    document = models.ForeignKey(Document, on_delete=models.CASCADE,
                                 verbose_name='Документ', related_name='balance_products_in_document')
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT,
                                 verbose_name='Склад', related_name='balance_products_in_stock')
    count = models.IntegerField(verbose_name='Кількість')
    sum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сума')