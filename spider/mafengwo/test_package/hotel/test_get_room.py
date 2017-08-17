#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/16 0016 上午 11:04

base Info
"""
from unittest import TestCase
from mafengwo.hotel import action
from mafengwo import html_download
from mafengwo.hotel import h_parser
from mafengwo.hotel.action import fo_log

__author__ = 'Administrator'
__version__ = '1.0'


class TestInit_room_url_list(TestCase):
    def test_init_room_url_list(self):
        url1 = "http://server.mafengwo.cn/hotel/ajax.php?sJsonCallBack=jQuery18109789543989958343_1502861850903&sAction=getRealPrice&iMddId=10189&iPoiId=7317932&sOta=youyu_pkg&sCheckIn=2017-08-17&sCheckOut=2017-08-18&iAdultsNum=2&iChildrenNum=0&sChildrenAge=&_=1502862132197"
        url2 = "http://server.mafengwo.cn/hotel/ajax.php?sJsonCallBack=jQuery18109789543989958343_1502861850902&sAction=getRealPrice&iMddId=10189&iPoiId=36273&sOta=hotels&sCheckIn=2017-08-24&sCheckOut=2017-08-25&iAdultsNum=2&iChildrenNum=0&sChildrenAge=&_=1502862132199"
        doc1 = html_download.downloadPage_without_proxy(url1,fo_log)
        doc2 = html_download.downloadPage_without_proxy(url2,fo_log)
        h_parser.get_room((doc1[0], doc2[0]))
