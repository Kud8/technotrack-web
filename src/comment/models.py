# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Comment(models.Model):
    text = models.TextField(verbose_name=u'Поле ввода текста')
    post = models.ForeignKey('post.Post', verbose_name=u'Пост', related_name='comments')
    pub_date = models.DateTimeField(verbose_name=u'Дата публикации', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Автор', related_name='comments')
    change_date = models.DateTimeField(verbose_name=u'Дата последнего редактирования', auto_now=True)

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        ordering = ('-pub_date', )

# Create your models here.
