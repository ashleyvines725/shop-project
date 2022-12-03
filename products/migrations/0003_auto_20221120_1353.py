# Generated by Django 3.2 on 2022-11-20 13:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.subcategory', verbose_name='subcategory title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.TextField(help_text='format: reqd, max_length=2500', max_length=2500, verbose_name='Brand description'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(help_text='format: required, max_length=100', max_length=100, unique=True, verbose_name='Brand slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='format: required, max_length=100', max_length=100, unique=True, verbose_name='Category title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='format: required, max_length=150', max_length=150, unique=True, verbose_name='Category slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(help_text='format: reqd, max_length=2500', max_length=2500, verbose_name='Product description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='how_to_use',
            field=models.TextField(help_text='format: reqd, max_length=2500', max_length=2500, verbose_name='How to use'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.TextField(help_text='format: reqd, max_length=2500', max_length=2500, verbose_name='Product ingredients'),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_quantity',
            field=models.IntegerField(verbose_name='Product quantity'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(help_text='format: required, max_length=150', max_length=150, unique=True, verbose_name='Subcategory slug'),
        ),
    ]