#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/11 0011 上午 11:23

base Info
"""
import pymysql
import re
import sys
import traceback

reload(sys)
sys.setdefaultencoding("utf8")

db = pymysql.connect("192.168.1.166", "root", "keystone", "kst_mafengwo", charset="utf8mb4")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data
print pymysql.paramstyle

__author__ = 'Administrator'
__version__ = '1.0'


def select_shopid_and_reviewnum(table):
    results = []
    try:
        sql = """SELECT shopId,reviewNum
                        FROM %s""" % table
        cursor.execute(sql)
        results = cursor.fetchall()

    except BaseException, e:
        print e

    return results


def select_shopid(table):
    results = []
    try:
        sql = """SELECT shopId
                        FROM %s""" % table
        cursor.execute(sql)
        results = cursor.fetchall()

    except BaseException, e:
        print e

    return results