#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/16 0016 下午 3:15

base Info
"""
from mafengwo.member import action

__author__ = 'Administrator'
__version__ = '1.0'


if __name__ == '__main__':
    table = "hotel_review"
    action.get_member(table)
