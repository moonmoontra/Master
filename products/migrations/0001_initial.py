# Generated by Django 4.2.2 on 2023-07-07 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Створено:')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Редаговано:')),
                ('price_name', models.CharField(default=None, max_length=30, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Тип ціни',
                'verbose_name_plural': 'Типи цін',
                'ordering': ['price_name'],
            },
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Створено:')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Редаговано:')),
                ('unit_name', models.CharField(default=None, max_length=15, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Одиниця вимірювання',
                'verbose_name_plural': 'Одиниці вимірювання',
                'ordering': ['unit_name'],
            },
        ),
        migrations.CreateModel(
            name='ProductRefBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Створено:')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Редаговано:')),
                ('articul', models.CharField(default=None, max_length=20, verbose_name='Артикул')),
                ('product_name', models.CharField(default=None, max_length=50, verbose_name='Назва')),
                ('manufacturer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='manufacturer_products', to='persons.manufacturer', verbose_name='Виробник')),
                ('unit_of_measure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='unitofmeasure_products', to='products.unitofmeasure', verbose_name='Од. виміру')),
            ],
            options={
                'verbose_name': 'Довідник товарів',
                'verbose_name_plural': 'Довідники товарів',
                'ordering': ['product_name', 'manufacturer'],
            },
        ),
        migrations.CreateModel(
            name='ProductPriceName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Створено:')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Редаговано:')),
                ('coefficient', models.FloatField(default=0.0, verbose_name='Коефіцієнт')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pricename_products', to='products.pricename', verbose_name='Тип ціни')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productrefbook_products', to='products.productrefbook', verbose_name='Товар')),
                ('unit_of_measure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='unitofmeasure_price_products', to='products.unitofmeasure', verbose_name='Од. виміру')),
            ],
            options={
                'verbose_name': 'Товар та ціна',
                'verbose_name_plural': 'Товари та ціни',
                'ordering': ['product', 'price'],
            },
        ),
    ]
