from django.db import models


class BaseData(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Створено:')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Редаговано:')

    class Meta:
        abstract = True


class Stock(BaseData):
    stock_name = models.CharField(max_length=30, default=None, verbose_name='Назва')
    stock_address = models.CharField(max_length=50, default=None, verbose_name='Адреса')

    def __str__(self):
        return f"{self.stock_name}"

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склади'
        ordering = ['stock_name']