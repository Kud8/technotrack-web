# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 18:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0005_auto_20160327_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='change_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 27, 18, 34, 26, 430374, tzinfo=utc), verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f'),
            preserve_default=False,
        ),
    ]