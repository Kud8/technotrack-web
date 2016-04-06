# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
import views

urlpatterns = [
    url(r'^posts/$', PostList.as_view(), name="post_list"),
    url(r'^create/$', login_required(views.PostCreate.as_view()), name='post_create'),
    url(r'^(?P<pk>\d+)/update/$', views.PostUpdate.as_view(), name='post_update'),
    url(r'^(?P<pk>\d+)/$', PostDialog.as_view(), name="post_detail"),
    url(r'^(?P<pk>\d+)/ajax/$', CommentsWithAjax.as_view(), name="post_comments"),
]
