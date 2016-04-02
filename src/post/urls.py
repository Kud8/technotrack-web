# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
import views

urlpatterns = [
    url(r'^$', PostList.as_view(), name="post_list"),
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name="post_detail"),
    url(r'^(?P<pk>\d+)/ajax/$', CommentsWithAjax.as_view(), name="post_comments"),
    #url(r'^create/$', login_required(views.QuestionCreate.as_view()), name='question_create'),
]
