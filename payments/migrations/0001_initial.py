# Generated by Django 5.1.2 on 2024-10-29 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice', '0006_remove_invoice_discount_amount_and_more'),
        ('vendor', '0002_rename_experience_vendor_estd_year_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=300, null=True)),
                ('payment_amount', models.FloatField(blank=True, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_note', models.TextField(blank=True, null=True)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='invoice.invoice')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]
