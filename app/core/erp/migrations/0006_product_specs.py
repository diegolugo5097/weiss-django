# Generated by Django 3.1.3 on 2020-11-10 01:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_auto_20201109_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specs',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Especificaciónes'),
        ),
    ]
