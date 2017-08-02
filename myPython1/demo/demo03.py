#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/2 0002 上午 9:04

base Info
"""

import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'Administrator'
__version__ = '1.0'
today = datetime.date.today()
now_str = today.strftime("%Y-%m-%d")
fo = open(r"D:\download_error\download_error_'%s'.txt"%now_str ,"wb")
fo.write("hello")
fo.close()


