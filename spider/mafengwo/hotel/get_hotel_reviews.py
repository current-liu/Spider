#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/15 0015 上午 11:18

base Info
"""

__author__ = 'Administrator'
__version__ = '1.0'
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
rootPath1 = os.path.split(rootPath)[0]
# 要添加 D:\LiuChao\PycharmProjects\spider\mafengwo
sys.path.append(rootPath1)
import action

if __name__ == '__main__':
    # 评论无法按时间排序，后期更新存在问题
    action.get_hotel_review()
