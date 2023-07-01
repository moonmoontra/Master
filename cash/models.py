from django.db import models


class BaseData(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Створено:')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Редаговано:')

    class Meta:
        abstract = True


class Valuta(models.Model):
    valuta_name = models.CharField(max_length=15, default=None, verbose_name='Назва')
    valuta_short = models.CharField(max_length=5, default=None, verbose_name='Скорочено')

    def __str__(self):
        return '[{valuta_short}] {valuta_name}'.format(valuta_short=self.valuta_short, valuta_name=self.valuta_name)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюти'


class Rate(models.Model):
    valuta = models.ForeignKey(Valuta, on_delete=models.CASCADE, verbose_name='Валюта',
                               related_name='valuta_rates')
    rate_date = models.DateField(auto_now_add=True, verbose_name='Дата курсу')
    rate_value = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Курс')

    def __str__(self):
        return '[{valuta}] {rate_value}'.format(valuta=self.valuta, rate_value=self.rate_value)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курси'


class Cash(BaseData):
    summa = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Сума')
    valuta = models.ForeignKey(Valuta, on_delete=models.PROTECT, verbose_name='Валюта', related_name='valuta_cash')

    def __str__(self):
        return '{summa} {valuta}'.format(summa=self.summa, valuta=self.valuta)

    class Meta:
        verbose_name = 'Каса підприємства'
        verbose_name_plural = 'Каси підприємства'


class CashDocuments(BaseData):
    cash_id = models.ForeignKey(Cash, on_delete=models.PROTECT, verbose_name='Каса', related_name='cash_documents')
    cash_document_date = models.DateField(auto_now_add=True, verbose_name='Дата документа')
    document_id = models.ForeignKey('Document', on_delete=models.CASCADE, verbose_name='Номер документа',
                                         related_name='cash_documents')
    cash_document_description = models.CharField(blank=True, max_length=50, default=None, verbose_name='Опис документа')

    def __str__(self):
        return '[{document_id}] {cash_document_date}'.format(document_id=self.document_id,
                                                          cash_document_date=self.cash_document_date)

    class Meta:
        verbose_name = 'Документ каси'
        verbose_name_plural = 'Документи каси'
        ordering = ['cash_document_date', 'document_id']