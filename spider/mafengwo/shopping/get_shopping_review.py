#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/22 0022 上午 10:21

base Info
"""
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
rootPath1 = os.path.split(rootPath)[0]
# 要添加 D:\LiuChao\PycharmProjects\spider\mafengwo
sys.path.append(rootPath1)
from mafengwo.shopping import action
__author__ = 'liuchao'
__version__ = '1.0'


if __name__ == '__main__':
    # 评论无排序，更新存在问题
    # 若获取中断，则中断的店铺无法后续后续信息，需手动处理当前正在爬的id，可将当前id的相关记录全部删除，重新启动
    action.get_shopping_review()
