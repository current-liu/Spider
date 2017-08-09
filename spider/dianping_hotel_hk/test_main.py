#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/7 0007 上午 9:58

base Info
"""

import sys
from unittest import TestCase

from dianping_hotel_hk import main

reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'Administrator'
__version__ = '1.0'


class TestMain(TestCase):
    def test_get_review_on_page(self):
        main.get_hotel_review_on_page(2576827, 69)
