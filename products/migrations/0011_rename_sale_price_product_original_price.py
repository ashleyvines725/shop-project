# Generated by Django 3.2 on 2022-11-23 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20221123_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sale_price',
            new_name='original_price',
        ),
    ]