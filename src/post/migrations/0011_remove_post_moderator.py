# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-27 14:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20160427_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='moderator',
        ),
    ]
