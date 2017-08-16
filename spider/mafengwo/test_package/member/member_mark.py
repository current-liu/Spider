#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/16 0016 下午 3:33

base Info
"""
from unittest import TestCase

from pymysql import NULL

from mafengwo.member import dao
__author__ = 'Administrator'
__version__ = '1.0'


class TestUpdate_member_mark(TestCase):
    def test_update_member_mark(self):
        dao.update_member_mark("hotel_review", 1, 124269)
