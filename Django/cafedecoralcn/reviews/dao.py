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
conf = config.DB_CONFIG
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

conn = pymysql.connect(**conf)
curs = conn.cursor()


def get_or_reviewNum(shop_id):
    sql = """SELECT COUNT(shopId) from reviews_orreview where shopId = %s"""
    # try:
    #     curs.execute(sql,shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_dp_reviewNum(shop_id):
    sql = """SELECT COUNT(shopId) from reviews_dpreview where shopId = %s"""
    # try:
    #     curs.execute(sql,shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_ta_reviewNum(shop_id):
    sql = """SELECT COUNT(shopId) from reviews_tareview where shopId = %s"""
    # try:
    #     curs.execute(sql,shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_mfw_reviewNum(shop_id):
    sql = """SELECT COUNT(shopId) from reviews_mfwreview where shopId = %s"""
    # try:
    #     curs.execute(sql,shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_all_id(shop_id):
    sql = """SELECT id, o_r , mfw,ta, dp FROM view_shop_relation where id = %s"""
    # try:
    #     curs.execute(sql, shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_or_review(shop_id):
    sql = """select content from reviews_orreview where memberId IN  (SELECT DISTINCT memberId from reviews_orreview where shopId = %s)"""
    # try:
    #     curs.execute(sql, shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_mfw_review(shop_id):
    sql = """select content from reviews_mfwreview where memberId IN  (SELECT DISTINCT memberId from reviews_mfwreview where shopId = %s)"""
    # try:
    #     curs.execute(sql, shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_dp_review(shop_id):
    sql = """select content from reviews_dpreview where memberId IN  (SELECT DISTINCT memberId from reviews_dpreview where shopId = %s)"""
    # try:
    #     curs.execute(sql, shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_ta_review(shop_id):
    sql = """select content from reviews_tareview where memberId IN  (SELECT DISTINCT memberId from reviews_tareview where shopId = %s)"""
    # try:
    #     curs.execute(sql, shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_or_month_review(shop_id):
    sql = """select LEFT(time,7) from reviews_orreview where memberId IN  (SELECT DISTINCT memberId from reviews_orreview where shopId = %s)"""
    # try:
    #     curs.execute(sql, shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_mfw_month_review(shop_id):
    sql = """select LEFT(time,7) from reviews_mfwreview where memberId IN  (SELECT DISTINCT memberId from reviews_mfwreview where shopId = %s)"""
    # try:
    #     curs.execute(sql, shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_dp_month_review(shop_id):
    sql = """select LEFT(time,7) from reviews_dpreview where memberId IN  (SELECT DISTINCT memberId from reviews_dpreview where shopId = %s)"""
    # try:
    #     curs.execute(sql, shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_ta_month_review(shop_id):
    sql = """select LEFT(time,7) from reviews_tareview where memberId IN  (SELECT DISTINCT memberId from reviews_tareview where shopId = %s)"""
    # try:
    #     curs.execute(sql, shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_or_review_info(shop_id):
    sql = """select memberName,memberId,title,content,time,taste,environment,services,health,pic from view_orreview where memberId IN  (SELECT DISTINCT memberId from reviews_orreview where shopId = %s)"""
    # try:
    #     curs.execute(sql,shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_dp_review_info(shop_id):
    sql = """select memberId,name,content,time,taste,environment,likes,reply,pic from view_dpreview where memberId IN (SELECT DISTINCT memberId from reviews_dpreview where shopId = %s)"""
    # try:
    #     curs.execute(sql,shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_ta_review_info(shop_id):
    sql = """select memberId,memberName,title,content,time,star,pic from view_tareview where memberId IN (SELECT DISTINCT memberId from reviews_tareview where shopId = %s)"""
    # try:
    #     curs.execute(sql,shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_mfw_review_info(shop_id):
    sql = """select memberId,name,content,time,star,likes,pic from view_mfwreview where memberId IN (SELECT DISTINCT memberId from reviews_mfwreview where shopId = %s)"""
    # try:
    #     curs.execute(sql,shop_id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results

