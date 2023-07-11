from django.db import models

from documents.models import Document, ProductInDocument
from home.models import BaseData
from products.models import ProductRefBook
from stocks.models import Stock


class BalanceProduct(BaseData):
    document = models.ForeignKey(Document, on_delete=models.CASCADE,
                                 verbose_name='Документ', related_name='balance_products_in_document')
    product_in_document = models.ForeignKey(ProductInDocument, on_delete=models.CASCADE, verbose_name='Товар',
                                related_name='balance_products_in_product_in_document')
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT,
                              verbose_name='Склад', related_name='balance_products_in_stock')
    count = models.IntegerField(verbose_name='Кількість')

    @property
    def sum(self):
        return self.count * self.product_in_document.price

    def __str__(self):
        return '[{document}] Товар: {product_name} в кількісті {count}'.format(
                                                        document=self.document,
                                                        product_name=self.product_in_document.product.product_name,
                                                        count=self.count)

    class Meta:
        verbose_name = 'Залишок'
        verbose_name_plural = 'Залишки'