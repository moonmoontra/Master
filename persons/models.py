from django.db import models


class BaseData(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Створено:')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Редаговано:')

    class Meta:
        abstract = True


class Provider(BaseData):
    STATUS = (
        ('individual', 'Фізична особа'),
        ('legal', 'Юридична особа'),
    )
    provider_name = models.CharField(max_length=30, default=None, verbose_name="Назва або Ім'я")
    city = models.CharField(max_length=30, default=None, verbose_name="Місто")
    address = models.CharField(max_length=30, default=None, verbose_name="Адреса")
    phone = models.CharField(max_length=15, default=None, verbose_name="Телефон")
    status = models.CharField(max_length=15, choices=STATUS, default=None, verbose_name="Статус")

    def __str__(self):
        return f"{self.provider_name}"

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенти'
        ordering = ['provider_name', 'city']


class Manufacturer(BaseData):
    manufacturer_name = models.CharField(max_length=30, default=None, verbose_name="Назва або Ім'я")
    country = models.CharField(max_length=30, default=None, verbose_name='Країна')

    def __str__(self):
        return f"{self.manufacturer_name}"

    class Meta:
        verbose_name = 'Виробник'
        verbose_name_plural = 'Виробники'
        ordering = ['country']


class Employee(BaseData):
    first_name = models.CharField(max_length=30, default=None, verbose_name="Ім'я")
    last_name = models.CharField(max_length=30, default=None, verbose_name='Прізвище')
    contract = models.CharField(max_length=30, default=None, verbose_name='Номер контракту')
    position = models.CharField(max_length=30, default=None, verbose_name='Посада')
    phone = models.CharField(max_length=15, default=None, verbose_name='Телефон')
    address = models.CharField(max_length=30, default=None, verbose_name='Адреса')
    start_date = models.DateField(verbose_name='Дата прийняття')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата звільнення')


    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)

    class Meta:
        verbose_name = 'Працівник'
        verbose_name_plural = 'Працівники'
        ordering = ['position']


class Clients(BaseData):
    client_name = models.CharField(max_length=30, default=None, verbose_name="Ім'я")
    phone = models.CharField(max_length=30, default=None, verbose_name="Телефон")
    birthday_date = models.DateField(default=None, verbose_name="Дата народження")

    def __str__(self):
        return "{client_name} [{birthday_date}]".format(client_name=self.client_name, birthday_date=self.birthday_date)

    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'
        ordering = ['birthday_date']