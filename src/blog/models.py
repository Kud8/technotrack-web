from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

# Create your models here.
