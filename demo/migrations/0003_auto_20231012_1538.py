# Generated by Django 3.2.12 on 2023-10-12 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Категория товара', 'verbose_name_plural': 'Категории товара'},
        ),
    ]
