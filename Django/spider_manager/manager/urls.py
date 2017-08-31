#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/31 0031 上午 9:03

base Info
"""
from django.conf.urls import url
from . import views

__author__ = 'liuchao'
__version__ = '1.0'

app_name = "manager"
# urlpatterns = [url(r'^$', views.index, name="index")]
urlpatterns = [url(r'^$', views.IndexView.as_view(), name='index'),
               url(r'^ajax/$', views.ajax, name='ajax')]
