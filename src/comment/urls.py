# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
import views

urlpatterns = [
    url(r'^create/$', login_required(views.CommentCreate.as_view()), name='comment_create'),
]
