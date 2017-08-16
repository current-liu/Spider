#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/16 0016 上午 11:04

base Info
"""
from unittest import TestCase
from mafengwo.hotel import action
__author__ = 'Administrator'
__version__ = '1.0'


class TestInit_room_url_list(TestCase):
    def test_init_room_url_list(self):
        action.init_room_url_list()
