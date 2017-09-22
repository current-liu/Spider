#!/usr/bin/env python
# coding=utf-8
"""
Created on 2017/9/21 22:58

base Info
"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'liuchao'
__version__ = '1.0'


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print environ['PATH_INFO']
    return '<h1>Hello,World! Welcome,%s</h1>' % (environ['PATH_INFO'][1:])

