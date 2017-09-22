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

app_name = "reviews"
# urlpatterns = [url(r'^$', views.index, name="index")]
urlpatterns = [url(r'^$', views.IndexView.as_view(), name='index'),

                url(r'^ajax/$', service.ajax, name='ajax'),
               # url(r'^get_dp_reviewNum/$',service.get_dp_reviewNum,name='get_dp_reviewNum'),
               # url(r'^get_ta_reviewNum/$',service.get_ta_reviewNum,name='get_ta_reviewNum'),
               # url(r'^get_or_reviewNum/$',service.get_or_reviewNum,name='get_or_reviewNum'),
               # url(r'^get_mfw_reviewNum/$',service.get_mfw_reviewNum,name='get_mfw_reviewNum'),
               url(r'^get_all_id/$',service.get_all_id,name='get_all_id'),
               url(r'^get_ta_review/$',service.get_ta_review,name='get_ta_review'),
               url(r'^get_or_review/$',service.get_or_review,name='get_or_review'),
               url(r'^get_dp_review/$',service.get_dp_review,name='get_dp_review'),
               url(r'^get_mfw_review/$',service.get_mfw_review,name='get_mfw_review'),
               url(r'^get_all_reviewNum/$',service.get_all_reviewNum,name='get_all_reviewNum'),
               ]
