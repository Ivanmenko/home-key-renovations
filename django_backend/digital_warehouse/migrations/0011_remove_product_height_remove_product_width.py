# Generated by Django 4.0.4 on 2022-04-30 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digital_warehouse', '0010_remove_product_pricing_productvariation_base_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='width',
        ),
    ]
