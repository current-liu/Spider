#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/10 0010 下午 3:01

base Info
"""
from bs4 import BeautifulSoup

__author__ = 'Administrator'
__version__ = '1.0'


def get_hotel_list(doc):
    soup = BeautifulSoup(doc, "lxml")

