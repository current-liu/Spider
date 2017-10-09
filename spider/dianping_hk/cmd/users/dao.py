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
from cafedecoralcn import config
from cafedecoralcn import DBManager

reload(sys)
sys.setdefaultencoding("utf8")



__author__ = 'Administrator'
__version__ = '1.0'

conf = config.DB_CONFIG_cafedecoral_analysis
conn = pymysql.connect(**conf)
curs = conn.cursor()


def get_dp_memberNum(shop_id):
    sql = """SELECT COUNT(DISTINCT memberId) FROM reviews_dpreview WHERE shopId = %s"""
    try:
        curs.execute(sql, shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results


def get_ta_memberNum(shop_id):
    sql = """SELECT COUNT(DISTINCT memberId) FROM reviews_tareview WHERE shopId = %s"""
    try:
        curs.execute(sql, shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results


def get_or_memberNum(shop_id):
    sql = """SELECT COUNT(DISTINCT memberId) FROM reviews_orreview WHERE shopId = %s"""
    try:
        curs.execute(sql, shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results


def get_mfw_memberNum(shop_id):
    sql = """SELECT COUNT(DISTINCT memberId) FROM reviews_mfwreview WHERE shopId = %s"""
    try:
        curs.execute(sql, shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results


def get_dp_memNum(shop_id):
    sql = """SELECT COUNT(sex) FROM users_dpmember WHERE sex="男" AND memberId IN  (SELECT DISTINCT memberId FROM reviews_dpreview WHERE shopId = %s)"""
    try:
        curs.execute(sql, shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results


def get_dp_womemNum(shop_id):
    sql = """SELECT COUNT(sex) FROM users_dpmember WHERE sex="女" AND memberId IN  (SELECT DISTINCT memberId FROM reviews_dpreview WHERE shopId = %s)"""
    try:
        curs.execute(sql, shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results



def get_mfw_memNum(shop_id):
    sql = """SELECT COUNT(sex) FROM users_mfwmember WHERE sex="male" AND memberId IN  (SELECT DISTINCT memberId FROM reviews_mfwreview WHERE shopId = %s)"""

    results = DBManager.queryAll(sql, shop_id)
    return results


def get_mfw_womemNum(shop_id):
    sql = """SELECT COUNT(sex) FROM users_mfwmember WHERE sex="female" AND memberId IN  (SELECT DISTINCT memberId FROM reviews_mfwreview WHERE shopId = %s)"""

    results = DBManager.queryAll(sql, shop_id)
    return results


def get_or_favorite(shop_id):
    sql = """SELECT favorite FROM users_ormember WHERE memberId IN  (SELECT DISTINCT memberId FROM reviews_orreview WHERE shopId = %s)"""

    results = DBManager.queryAll(sql, shop_id)
    return results


def get_or_location(shop_id):
    sql = """SELECT location,COUNT(location) FROM users_ormember WHERE memberId IN  (SELECT DISTINCT memberId FROM reviews_orreview WHERE shopId = %s) GROUP BY location"""

    results = DBManager.queryAll(sql, shop_id)
    return results


def get_dp_location(shop_id):
    sql = """SELECT location,COUNT(location) FROM users_dpmember WHERE memberId IN  (SELECT DISTINCT memberId FROM reviews_dpreview WHERE shopId = %s)GROUP BY location"""

    results = DBManager.queryAll(sql, shop_id)
    return results


def get_ta_location(shop_id):
    sql = """SELECT location,COUNT(location) FROM users_tamember WHERE memberId IN  (SELECT DISTINCT memberId FROM reviews_tareview WHERE shopId = %s)GROUP BY location"""

    results = DBManager.queryAll(sql, shop_id)
    return results


def get_mfw_location(shop_id):
    sql = """SELECT location,COUNT(location) FROM users_mfwmember WHERE memberId IN  (SELECT DISTINCT memberId FROM reviews_mfwreview WHERE shopId = %s)GROUP BY location"""

    results = DBManager.queryAll(sql, shop_id)
    return results


def get_all_id(shop_id):
    sql = """SELECT id, o_r , mfw,ta, dp FROM view_shop_relation WHERE id = %s"""

    results = DBManager.queryAll(sql, shop_id)
    return results

