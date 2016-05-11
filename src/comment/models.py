# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from adjacent import Client
from django.dispatch import receiver
from django.template.defaultfilters import date as _date
from datetime import datetime

class Comment(models.Model):
    text = models.TextField(verbose_name=u'Текст')
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

    def as_compact_dict(self):
        return {"author": self.author.pk, "text": self.text, "pub_date": _date(self.pub_date, 'd b Y г. H:i'), "change_date": _date(self.change_date, 'd b Y г. H:i')}

    # def get_cent_answers_channel_name(self):
    #     return "%d"%self.id

@receiver(models.signals.post_save, sender=Comment)
def on_answer_creation(sender, instance, *args, **kwargs):
    if kwargs.get('created'):
        comment = instance
        from .tasks import send_email_notification
        send_email_notification.delay(
            'mitya-kudr@mail.ru',
            'New answer to question "{}"'.format(comment.post.title),
            'You got answer with the text: "{}"'.format(comment.text)
        )

        client = Client()
        client.publish(comment.post.get_cent_answers_channel_name(), comment.as_compact_dict())
        response = client.send()
        print('sent to channel {}, got response from centrifugo: {}'.format(comment.post.get_cent_answers_channel_name(),
                                                                            response))
