# Generated by Django 3.1.3 on 2020-11-10 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0013_carousel_personal_sport'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='image',
            field=models.ImageField(null=True, upload_to='sport/%Y/%m/%d', verbose_name='Imagen'),
        ),
    ]
