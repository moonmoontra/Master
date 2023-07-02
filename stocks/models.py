from django.db import models
from home.models import BaseData


class Stock(BaseData):
    stock_name = models.CharField(max_length=30, default=None, verbose_name='Назва')
    stock_address = models.CharField(max_length=50, default=None, verbose_name='Адреса')

    def __str__(self):
        return f"{self.stock_name}"

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склади'
        ordering = ['stock_name']