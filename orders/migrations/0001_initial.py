# Generated by Django 2.1.14 on 2020-01-27 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20200126_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_qty', models.IntegerField()),
                ('order_first_name', models.CharField(max_length=50)),
                ('order_last_name', models.CharField(max_length=50)),
                ('order_phone_number', models.CharField(max_length=20)),
                ('order_country', models.CharField(max_length=40)),
                ('order_postcode', models.CharField(blank=True, max_length=20)),
                ('order_city', models.CharField(max_length=40)),
                ('order_street_address_1', models.CharField(max_length=40)),
                ('order_street_address_2', models.CharField(max_length=40)),
                ('order_county', models.CharField(max_length=40)),
                ('order_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]