from django.db import models

from persons.models import Manufacturer


class BaseData(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Створено:')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Редаговано:')

    class Meta:
        abstract = True


class UnitOfMeasure(BaseData):
    unit_name = models.CharField(max_length=15, default=None, verbose_name='Назва')

    def __str__(self):
        return f"{self.unit_name}"

    class Meta:
        verbose_name = 'Одиниця вимірювання'
        verbose_name_plural = 'Одиниці вимірювання'
        ordering = ['unit_name']


class Price(BaseData):
    price_name = models.CharField(max_length=30, default=None, verbose_name='Назва')

    def __str__(self):
        return f"{self.price_name}"

    class Meta:
        verbose_name = 'Тип ціни'
        verbose_name_plural = 'Типи цін'
        ordering = ['price_name']


class GoodRefBook(BaseData):
    articul = models.CharField(max_length=20, default=None, verbose_name='Артикул')
    good_name = models.CharField(max_length=50, default=None, verbose_name='Назва')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Виробник')
    unitOfMeasure = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, verbose_name='Од. виміру')

    def __str__(self):
        return '{articul} {good_name}'.format(first_name=self.articul, last_name=self.good_name)

    class Meta:
        verbose_name = 'Довідник товарів'
        verbose_name_plural = 'Довідники товарів'
        ordering = ['good_name', 'manufacturer']


class GoodPrice(BaseData):
    good = models.ForeignKey(GoodRefBook, on_delete=models.CASCADE, verbose_name='Назва')
    price = models.ForeignKey(Price, on_delete=models.CASCADE, verbose_name='Ціна')
    unitOfMeasure = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, verbose_name='Од. виміру')
    coefficient = models.FloatField(verbose_name='Коефіцієнт')

    def __str__(self):
        return '{good} {price}'.format(first_name=self.good, last_name=self.price)

    class Meta:
        verbose_name = 'Товар та ціна'
        verbose_name_plural = 'Товари та ціни'
        ordering = ['good', 'price']