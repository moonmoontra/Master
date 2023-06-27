from django.db import models


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