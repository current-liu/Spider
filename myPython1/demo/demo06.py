#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/17 0017 下午 2:21

base Info
"""
import datetime
__author__ = 'Administrator'
__version__ = '1.0'


today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")
print "%s" % today
