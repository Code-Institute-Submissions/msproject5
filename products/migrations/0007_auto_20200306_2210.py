# Generated by Django 2.1.14 on 2020-03-06 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200224_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_category_id',
            new_name='product_category',
        ),
    ]
