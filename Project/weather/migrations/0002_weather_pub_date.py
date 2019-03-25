# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 12:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 15, 12, 37, 23, 766707, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]