from django.db import models

from persons.models import Manufacturer
from home.models import BaseData


class UnitOfMeasure(BaseData):
    unit_name = models.CharField(max_length=15, default=None, verbose_name='Назва')

    def __str__(self):
        return f"{self.unit_name}"

    class Meta:
        verbose_name = 'Одиниця вимірювання'
        verbose_name_plural = 'Одиниці вимірювання'
        ordering = ['unit_name']


class PriceName(BaseData):
    price_name = models.CharField(max_length=30, default=None, verbose_name='Назва')

    def __str__(self):
        return f"{self.price_name}"

    class Meta:
        verbose_name = 'Тип ціни'
        verbose_name_plural = 'Типи цін'
        ordering = ['price_name']


class ProductRefBook(BaseData):
    articul = models.CharField(max_length=20, default=None, verbose_name='Артикул')
    product_name = models.CharField(max_length=50, default=None, verbose_name='Назва')
    manufacturer = models.ForeignKey(Manufacturer, default=None, on_delete=models.SET_DEFAULT,
                                     verbose_name='Виробник', related_name='manufacturer_products')
    unit_of_measure = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, verbose_name='Од. виміру',
                                      related_name='unitofmeasure_products')

    def __str__(self):
        return '[{articul}] {product_name}'.format(articul=self.articul,product_name=self.product_name)

    class Meta:
        verbose_name = 'Довідник товарів'
        verbose_name_plural = 'Довідники товарів'
        ordering = ['product_name', 'manufacturer']


class ProductPriceName(BaseData):
    product = models.ForeignKey(ProductRefBook, on_delete=models.CASCADE, verbose_name='Товар',
                                related_name='productrefbook_products')
    price = models.ForeignKey(PriceName, on_delete=models.PROTECT, verbose_name='Тип ціни',
                              related_name='pricename_products')
    unit_of_measure = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT, verbose_name='Од. виміру',
                                      related_name='unitofmeasure_price_products')
    coefficient = models.FloatField(default=0.0, verbose_name='Коефіцієнт')

    def __str__(self):
        return '{product} {price}'.format(product=self.product, price=self.price)

    class Meta:
        verbose_name = 'Товар та ціна'
        verbose_name_plural = 'Товари та ціни'
        ordering = ['product', 'price']