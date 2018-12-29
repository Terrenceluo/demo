#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:group-detail')

    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    groups = serializers.HyperlinkedRelatedField(many=True, view_name='api:group-detail', queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
