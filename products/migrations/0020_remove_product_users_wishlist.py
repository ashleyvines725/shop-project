# Generated by Django 3.2 on 2023-01-11 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_product_users_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users_wishlist',
        ),
    ]