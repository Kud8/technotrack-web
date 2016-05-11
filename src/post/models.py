# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=140)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Тэг'
        verbose_name_plural = u'Тэги'
        ordering = ('name',)

class Post(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=140)
    text = models.TextField(verbose_name=u'Текст')
    pub_date = models.DateTimeField(verbose_name=u'Дата публикации', auto_now_add=True)
    change_date = models.DateTimeField(verbose_name=u'Дата последнего редактирования', auto_now=True)
    blog = models.ForeignKey('blog.Blog', verbose_name=u'Блог', related_name='post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор', related_name='posts')
    is_published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
        ordering = ('-pub_date', )

    def get_cent_answers_channel_name(self):
        return "post_%d"%self.id
# Create your models here.
