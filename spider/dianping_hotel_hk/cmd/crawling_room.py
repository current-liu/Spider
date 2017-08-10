#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/10 0010 下午 4:55

base Info
"""
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from dianping_hotel_hk import main



__author__ = 'Administrator'
__version__ = '1.0'


if __name__ == '__main__':
    pass
    main.crawling_room()
