# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from post.models import *
from blog.models import *
from comment.models import *

import random

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        b = []
        p = []
        c = []
        for _ in range(10):
            b.append(Blog.objects.create())
        for i in range(100):
            t = Post(author=random.choice(users), title = u'title {}'.format(i),
                     text = u'text {}'.format(i), is_published = True,
                     blog=random.choice(b))
            p.append(t)
            t.save()
            Tag.objects.create(name='tag{}'.format(i))
        for i in range(1000):
            com = Comment(author = random.choice(users), post = random.choice(p),
                           text=u'text {}'.format(i))
            c.append(com)
            com.save()