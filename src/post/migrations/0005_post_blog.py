# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('post', '0004_remove_post_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.Blog'),
            preserve_default=False,
        ),
    ]
