# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 17:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='blog',
        ),
    ]
