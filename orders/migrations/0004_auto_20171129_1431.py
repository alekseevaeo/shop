# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20171129_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverymethod',
            name='delivery_time',
            field=models.CharField(blank=True, default=None, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='deliverymethod',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='deliverymethod',
            name='remark',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='commission',
            field=models.CharField(blank=True, default=None, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='remark',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
