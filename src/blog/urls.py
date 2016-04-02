# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="blog"),
]
