#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^groups/$', views.GroupList.as_view(), name='group-list'),
    url(r'^groups/(?P<pk>\d+)/$', views.GroupDetail.as_view(), name='group-detail'),
]
