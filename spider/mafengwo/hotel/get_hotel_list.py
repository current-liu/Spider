#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/10 0010 下午 4:32

base Info
"""
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
rootPath1 = os.path.split(rootPath)[0]
# 要添加 D:\LiuChao\PycharmProjects\spider\mafengwo
sys.path.append(rootPath1)
import action
__author__ = 'Administrator'
__version__ = '1.0'

# TODO log文件名带上方法名
if __name__ == '__main__':
    action.get_hotel_list()
