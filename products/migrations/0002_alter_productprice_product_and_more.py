# Generated by Django 4.2.2 on 2023-06-27 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0014_alter_manufacturer_country'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprice',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productrefbook_products', to='products.productrefbook'),
        ),
        migrations.AlterField(
            model_name='productrefbook',
            name='manufacturer',
            field=models.ForeignKey(on_delete=models.SET('Unknown'), related_name='manufacturer_products', to='persons.manufacturer', verbose_name='Виробник'),
        ),
        migrations.AlterField(
            model_name='productrefbook',
            name='unitOfMeasure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='unit_of_measure', to='products.unitofmeasure', verbose_name='Од. виміру'),
        ),
    ]
