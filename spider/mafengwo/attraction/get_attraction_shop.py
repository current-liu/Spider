#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/18 0018 上午 11:57

base Info
"""
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
rootPath1 = os.path.split(rootPath)[0]
# 要添加 D:\LiuChao\PycharmProjects\spider\mafengwo
sys.path.append(rootPath1)
from mafengwo.attraction import action
__author__ = 'liuchao'
__version__ = '1.0'


if __name__ == '__main__':
    action.get_attraction_shop()
