# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-10 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_main', '0008_auto_20181010_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='plains',
            name='plain_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
