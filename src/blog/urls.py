# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^posts/$', PostList.as_view(), name="post_list"),
    url(r'^(?P<post>\d+)/$', show_post),
]
