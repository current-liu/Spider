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

db = pymysql.connect("192.168.1.225", "root", "root", "openrice", charset="utf8mb4")

cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data
print pymysql.paramstyle

__author__ = 'Administrator'
__version__ = '1.0'


def select_shopName():
    results = []
    try:
        sql = """SELECT shopId,shopName FROM openrice_shops """
        cursor.execute(sql)
        results = cursor.fetchall()

    except BaseException, e:
        print e

    return results


def insert_into_text_jb(text111, shopName):
    sql = """INSERT INTO text_jb (text111, shopName) VALUES ('%s', '%s')"""

    try:
        cursor.execute(sql % (text111, shopName))
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


if __name__ == '__main__':
    select_shopName()
    insert_into_text_jb("1","2")
