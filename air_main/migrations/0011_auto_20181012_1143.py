# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-12 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_main', '0010_airports_port_name_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plains',
            name='plain_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
