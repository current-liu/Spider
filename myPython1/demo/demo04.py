#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/2 0002 下午 5:13

base Info
"""

import sys

import datetime

reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'Administrator'
__version__ = '1.0'

create_time = datetime.datetime.strptime(u"2000-01-01", '%Y-%m-%d')
m = "s"
msg = "fjslkf" + m
print msg






