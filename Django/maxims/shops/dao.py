#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/11 0011 上午 11:23

base Info
"""

import sys
import pymysql
from maxims import config

reload(sys)
sys.setdefaultencoding("utf8")

__author__ = 'Administrator'
__version__ = '1.0'

conf = config.DB_CONFIG_cafedecoral_analysis
conn = pymysql.connect(**conf)
curs = conn.cursor()


def get_all_id(shop_id):
    """没有的平台，id返回0"""
    # sql = """SELECT id, o_r , mfw,ta, dp FROM view_shop_relation where id = %s"""
    sql = """SELECT id,(CASE WHEN o_r IS NOT NULL THEN o_r ELSE 0 END) o_r ,(CASE WHEN mfw IS NOT NULL THEN mfw ELSE 0 END) mfw,(CASE WHEN ta IS NOT NULL THEN ta ELSE 0 END) ta, (CASE WHEN dp IS NOT NULL THEN dp ELSE 0 END) dp
                      FROM view_shop_relation where id = %s"""
    try:
        curs.execute(sql, shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results


def selete_shop_all():
    sql = """SELECT id,shopName,(CASE WHEN o_r IS NOT NULL THEN 1 ELSE 0 END) o_r ,(CASE WHEN mfw IS NOT NULL THEN 1 ELSE 0 END) mfw,(CASE WHEN ta IS NOT NULL THEN 1 ELSE 0 END) ta, (CASE WHEN dp IS NOT NULL THEN 1 ELSE 0 END) dp
FROM view_shop_relation"""
    try:
        curs.execute(sql)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results


def selete_shop_all_info(shop_id):
    sql = """SELECT id,shopName,shopAddr,shopTelFix FROM view_shop_relation where id = %s """
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def selete_dp_pic(shop_id):
    sql = """SELECT pic FROM shops_dpshop where shopId = %s """
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def selete_ta_pic(shop_id):
    sql = """SELECT pic FROM shops_tashop where shopId = %s """
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def selete_or_pic(shop_id):
    sql = """SELECT pic FROM shops_orshop where shopId = %s """
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def selete_mfw_pic(shop_id):
    sql = """SELECT pic FROM shops_mfwshop where shopId = %s """
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results