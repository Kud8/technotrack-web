from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey('blog.Post')
    pub_date = models.DateTimeField(auto_now_add=True)

# Create your models here.
