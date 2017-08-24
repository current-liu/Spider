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

print 1|0


lis = [1,2,3,4]


for n in range(3):
    x = len(lis)
    y = lis.__len__()
    print next(lis)
