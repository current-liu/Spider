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

reload(sys)
sys.setdefaultencoding("utf8")

# config = {'host': '202.110.49.146', 'port': 3355, 'user': 'root', 'password': 'keystone', 'db': 'cafedecoral_data',
#     'charset': 'utf8mb4', 'cursorclass': pymysql.cursors.DictCursor, }
config_146 = {'host': '202.110.49.146', 'port': 3355, 'user': 'root', 'password': 'keystone', 'db': 'cafedecoral_data',
    'charset': 'utf8mb4'}
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

db = pymysql.connect(**config_146)
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data

__author__ = 'Administrator'
__version__ = '1.0'


# conf = {'host': '202.110.49.146', 'port': 3355, 'user': 'root', 'password': 'keystone', 'db': 'cafedecoral_analysis',
#     'charset': 'utf8mb4'}
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
conf = config.DB_CONFIG_166

conn = pymysql.connect(**conf)
curs = conn.cursor()

def get_dp_memberNum(shop_id):
    sql = """SELECT COUNT(DISTINCT memberId) from reviews_dpreview where shopId = %s"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_ta_memberNum(shop_id):
    sql = """SELECT COUNT(DISTINCT memberId) from reviews_tareview where shopId = %s"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_or_memberNum(shop_id):
    sql = """SELECT COUNT(DISTINCT memberId) from reviews_orreview where shopId = %s"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_mfw_memberNum(shop_id):
    sql = """SELECT COUNT(DISTINCT memberId) from reviews_mfwreview where shopId = %s"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_dp_memNum(shop_id):
    sql = """select COUNT(sex) from users_dpmember where sex="男" AND memberId IN  (SELECT DISTINCT memberId from reviews_dpreview where shopId = %s)"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_dp_womemNum(shop_id):
    sql = """select COUNT(sex) from users_dpmember where sex="女" AND memberId IN  (SELECT DISTINCT memberId from reviews_dpreview where shopId = %s)"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results


# def selete_ta_shop_memberNum():
#     sql = """SELECT COUNT(DISTINCT memberId) from reviews_tareview where shopId = 5292664"""
#     try:
#         curs.execute(sql)
#         results = curs.fetchall()
#         print results
#     except BaseException, e:
#         print e
#
#     return results
#
# def selete_or_shop_memberNum():
#     sql = """SELECT COUNT(DISTINCT memberId) from reviews_mfwreview where shopId = 669"""
#     try:
#         curs.execute(sql)
#         results = curs.fetchall()
#         print results
#     except BaseException, e:
#         print e
#
#     return results

def get_mfw_memNum(shop_id):
    sql = """select COUNT(sex) from users_mfwmember where sex="male" AND memberId IN  (SELECT DISTINCT memberId from reviews_mfwreview where shopId = %s)"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_mfw_womemNum(shop_id):
    sql = """select COUNT(sex) from users_mfwmember where sex="female" AND memberId IN  (SELECT DISTINCT memberId from reviews_mfwreview where shopId = %s)"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return   results


def get_or_favorite(shop_id):
    sql = """select favorite from users_ormember where memberId IN  (SELECT DISTINCT memberId from reviews_orreview where shopId = %s)"""
    try:
        curs.execute(sql, shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_or_location(shop_id):
    sql = """select location,COUNT(location) from users_ormember where memberId IN  (SELECT DISTINCT memberId from reviews_orreview where shopId = %s) GROUP BY location"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_dp_location(shop_id):
    sql = """select location,COUNT(location) from users_dpmember where memberId IN  (SELECT DISTINCT memberId from reviews_dpreview where shopId = %s)GROUP BY location"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_ta_location(shop_id):
    sql = """select location,COUNT(location) from users_tamember where memberId IN  (SELECT DISTINCT memberId from reviews_tareview where shopId = %s)GROUP BY location"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_mfw_location(shop_id):
    sql = """select location,COUNT(location) from users_mfwmember where memberId IN  (SELECT DISTINCT memberId from reviews_mfwreview where shopId = %s)GROUP BY location"""
    try:
        curs.execute(sql,shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results

def get_all_id(shop_id):
    sql = """SELECT id, o_r , mfw,ta, dp FROM view_shop_relation where id = %s"""
    try:
        curs.execute(sql, shop_id)
        results = curs.fetchall()
        print results
    except BaseException, e:
        print e

    return results