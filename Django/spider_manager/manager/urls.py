#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/31 0031 上午 9:03

base Info
"""
from django.conf.urls import url
from . import views, service

__author__ = 'liuchao'
__version__ = '1.0'

app_name = "manager"
# urlpatterns = [url(r'^$', views.index, name="index")]
urlpatterns = [url(r'^$', views.IndexView.as_view(), name='index'),
                url(r'^get_projects/$', service.get_projects, name='get_projects'),
                url(r'^get_spiders_in_project/$', service.get_spiders_in_project, name='get_spiders_in_project'),
                url(r'^get_project/$', service.get_project, name='get_project'),
                url(r'^get_spider/$', service.get_spider, name='get_spider'),
                url(r'^get_spiderstatus/$', service.get_spiderstatus, name='get_spiderstatus'),
                url(r'^get_spiderstatus_today/$', service.get_spiderstatus_today, name='get_spiderstatus_today'),
                url(r'^get_spiderstatus_last/$', service.get_spiderstatus_last, name='get_spiderstatus_last'),
                url(r'^ajax/$', service.ajax, name='ajax'),

               ]
