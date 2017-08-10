#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/10 0010 下午 3:01

base Info
"""
from mafengwo import html_download
import h_parser

__author__ = 'Administrator'
__version__ = '1.0'


def get_hotel_list():
    url = "http://www.mafengwo.cn/hotel/10189/?sFrom=mdd#avl=0&distance=10000&price=-&feature=0&fav=0&sort=comment-DESC&page=1"
    doc, msg = html_download.downloadPage_without_proxy(url)
    if msg != "ok":
        pass
    res = h_parser.get_hotel_list(doc)
    pass
