#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/7 0007 上午 9:17

base Info
"""

import sys
from unittest import TestCase

reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'Administrator'
__version__ = '1.0'

import dianping_hotel_hk.dao

class TestDao(TestCase):
    def test_select_shopid_and_reviewnum(self):
        res = dianping_hotel_hk.dao.select_shopid_and_reviewnum("hotel_shops")
        print res
