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

app_name = "shops"
# urlpatterns = [url(r'^$', views.index, name="index")]
urlpatterns = [url(r'^$', views.IndexView.as_view(), name='index'),

                url(r'^ajax/$', service.ajax, name='ajax'),
                url(r'^selete_shop_all/$',service.selete_shop_all,name='selete_shop_all'),
                url(r'^get_dp_shops/$', service.get_dp_shops, name='get_dp_shops'),
                url(r'get_dp_star/$',service.get_dp_star ,name='get_dp_star'),
                url(r'selete_shop_all_star/$',service.selete_shop_all_star ,name='selete_shop_all_star'),

               ]
