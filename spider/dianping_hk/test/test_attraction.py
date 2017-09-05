#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/7 0007 下午 3:05

base Info
"""

import sys
from unittest import TestCase

from dianping_hk import main

reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'Administrator'
__version__ = '1.0'


class Test_attraction(TestCase):
    def test_get_attraction_list(self):
        main.get_attraction_list(2)
