# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoryLoss', '0003_auto_20160713_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
