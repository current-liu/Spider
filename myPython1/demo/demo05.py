#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/4 0004 下午 2:03

base Info
"""

import sys

import datetime

import re

reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'Administrator'
__version__ = '1.0'

today = datetime.date.today()
today_str = today.strftime("%Y%m%d")
filename = today_str+".md"
fo_log = open(filename, "a")
fo_log.write("nihao")

# today_int = int(re.sub(r'\D', "", today_str))
# fo_log = open("'%s'.txt" % today_str, "a")


