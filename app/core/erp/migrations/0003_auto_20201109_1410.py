# Generated by Django 3.1.3 on 2020-11-09 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': ' Categoria ', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': ' Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='product',
            name='register_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Registro/Modificiación'),
        ),
    ]
