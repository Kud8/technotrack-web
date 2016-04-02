# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=140)
    text = models.TextField(verbose_name=u'Поле ввода текста')
    pub_date = models.DateTimeField(verbose_name=u'Дата публикации', auto_now_add=True)
    change_date = models.DateTimeField(verbose_name=u'Дата последнего редактирования', auto_now=True)
    blog = models.ForeignKey('blog.Blog', verbose_name=u'Блог', related_name='post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор', related_name='posts')
    moderator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Модератор', related_name='published_posts')
    is_published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
        ordering = ('-pub_date', )

# Create your models here.
