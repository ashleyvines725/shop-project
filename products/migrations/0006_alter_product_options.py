# Generated by Django 3.2 on 2022-11-22 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20221120_2034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['sku'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]