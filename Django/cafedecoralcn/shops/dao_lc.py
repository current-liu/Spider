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
#         'charset': 'utf8mb4'}
conf = config.DB_CONFIG
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
conn = pymysql.connect(**conf)
curs = conn.cursor()


def get_all_shop_ids():
    sql = """SELECT id,shopName,(CASE WHEN dp IS NOT NULL THEN dp ELSE 0 END) dp, (CASE WHEN o_r IS NOT NULL THEN o_r ELSE 0 END) o_r ,(CASE WHEN mfw IS NOT NULL THEN mfw ELSE 0 END) mfw,(CASE WHEN ta IS NOT NULL THEN ta ELSE 0 END) ta
              FROM view_shop_relation"""
    # try:
    #     curs.execute(sql)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql)
    return results


def get_shop_star_from_pla(pla, shop_id):
    sql = "SELECT star FROM shops_"+pla+"shop WHERE shopId = %s"
    # try:
    #     curs.execute(sql, id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_shop_star_and_more_from_dp(shop_id):
    sql = """SELECT star,taste,environment,service FROM shops_dpshop WHERE shopId = %s"""
    # try:
    #     curs.execute(sql, id)
    #     results = curs.fetchall()
    #     print results
    # except BaseException, e:
    #     print e
    results = DBManager.queryAll(sql, shop_id)
    return results
