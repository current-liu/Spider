#!/usr/bin/env python
# coding=utf-8
"""
Created on 2017/9/21 23:03

base Info
"""
import sys
from wsgiref.simple_server import make_server
from hello import application

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'liuchao'
__version__ = '1.0'

httpd = make_server("", 8000, application)
print "Serving HTTP on port 8000..."
httpd.serve_forever()