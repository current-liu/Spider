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
                url(r'^get_spiders/$', service.get_spiders, name='get_spiders'),
                url(r'^get_spiderstatus/$', service.get_spiderstatus, name='get_spiderstatus'),
                url(r'^get_spiderstatus_today/$', service.get_spiderstatus_today, name='get_spiderstatus_today'),
                url(r'^get_spiderstatus_last/$', service.get_spiderstatus_last, name='get_spiderstatus_last'),
                url(r'^get_spider_group_on_status/$', service.get_spider_group_on_status, name='get_spider_group_on_status'),
                url(r'^get_spider_on_date/$', service.get_spider_on_date, name='get_spider_on_date'),
                url(r'^get_error_spider_on_date/$', service.get_error_spider_on_date, name='get_error_spider_on_date'),
                url(r'^get_spider_on_month_every_day/$', service.get_spider_on_month_every_day, name='get_spider_on_month_every_day'),
                url(r'^get_spider_on_year_every_month/$', service.get_spider_on_year_every_month, name='get_spider_on_year_every_month'),
                url(r'^get_spider_on_day_every_hour/$', service.get_spider_on_day_every_hour, name='get_spider_on_day_every_hour'),
                url(r'^get_operation_time_last_n_days/$', service.get_operation_time_last_n_days, name='get_operation_time_last_n_days'),


                url(r'^ajax/$', service.ajax, name='ajax'),

               ]
