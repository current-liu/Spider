#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/16 0016 下午 3:15

base Info
"""
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
rootPath1 = os.path.split(rootPath)[0]
# 要添加 D:\LiuChao\PycharmProjects\spider\mafengwo
sys.path.append(rootPath1)

from mafengwo.member import action

__author__ = 'Administrator'
__version__ = '1.0'

if __name__ == '__main__':
    # 中断时当前member需要手动处理
    # TODO给member_path.memberId 建索引
    # 主键为id，判断重复的后面需完善。可以在更新时，查询之前的足迹的最后时间，带入paser逻辑
    action.get_member_path()
