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


config_cafedecoral_data = config.DB_CONFIG_cafedecoral_data
db = pymysql.connect(**config_cafedecoral_data)
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data

__author__ = 'Administrator'
__version__ = '1.0'


conf = config.DB_CONFIG_cafedecoral_analysis
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
conn = pymysql.connect(**conf)
curs = conn.cursor()


def selete_shops_id_tel(platform):
    sql_or = """SELECT shopId, shoptel FROM or_shops;"""
    sql_dp = """SELECT shopId,addr FROM dp_shops;"""
    sql_mfw = """SELECT shopId,tel FROM mfw_shops;"""
    sql_ta = """SELECT shopId,telephone FROM ta_shops;"""
    platform_table = {"or": sql_or, "dp": sql_dp, "mfw": sql_mfw, "ta": sql_ta}

    try:
        sql = platform_table[platform]
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e

    return results


def insert_x_shops_tel(pla, shop_id_tel):
    sql = "INSERT INTO " + pla + "_shops_tel" + " (shopId, tel_fix) VALUES (%s, %s)"
    try:
        cursor.executemany(sql, shop_id_tel)
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


def get_shop_id_with_the_same_tel(target, pla):
    sql = "SELECT t.shopId, tar.shopId FROM " + pla + "_shops_tel t JOIN " + target + "_shops_tel tar ON t.tel_fix = tar.tel_fix;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e

    return results


def update_shop_id(target, pla, id_shop):
    """更新表shop_id"""

    sql = "UPDATE shop_id SET " + pla + "_id = %s WHERE " + target + "_id = %s"
    try:
        cursor.executemany(sql, id_shop)
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


def selete_shops_id_addr(platform):
    sql_or = """SELECT shopId, shopAddress FROM or_shops;"""
    sql_dp = """SELECT shopId,addr FROM dp_shops;"""
    sql_mfw = """SELECT shopId,addr FROM mfw_shops;"""
    sql_ta = """SELECT shopId,addr FROM ta_shops;"""
    platform_table = {"or": sql_or, "dp": sql_dp, "mfw": sql_mfw, "ta": sql_ta}

    try:
        sql = platform_table[platform]
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e

    return results


def insert_x_shops_addr(pla, shop_id_addr):
    sql = "UPDATE " + pla + "_shops_tel SET addr_fix = %s WHERE shopId = %s"
    try:
        cursor.executemany(sql, shop_id_addr)
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


def get_shop_id_with_the_same_addr(target, pla):
    sql = "SELECT t.shopId, tar.shopId FROM " + pla + "_shops_tel t JOIN " + target + "_shops_tel tar ON t.addr_fix = tar.addr_fix;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e

    return results


def init_shop_id_by_pla(target, ids):
    sql = "INSERT INTO shop_id (" + target + "_id) VALUES (%s)"
    try:
        cursor.executemany(sql, ids)
        db.commit()
    except BaseException, e:
        print e
        db.rollback()
    pass


def select_shop_id_unmatched(target):
    sql = "SELECT shopId from " + target + "_shops_tel WHERE shopId NOT IN (SELECT  " + target + "_id FROM shop_id)"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e

    return results


def selete_shops_info(platform):
    sql_or = """SELECT shopId, shopAddress, shopName, shopTel FROM or_shops;"""
    sql_dp = """SELECT shopId, addr, shopName, addr FROM dp_shops;"""
    sql_mfw = """SELECT shopId,addr, shopName, tel FROM mfw_shops;"""
    sql_ta = """SELECT shopId,addr, shopName,telephone FROM ta_shops;"""
    platform_table = {"or": sql_or, "dp": sql_dp, "mfw": sql_mfw, "ta": sql_ta}

    try:
        sql = platform_table[platform]
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e

    return results


def insert_shop_relation(shop_info):
    # sql = "UPDATE " + pla + "_shops_tel SET addr_fix = %s WHERE shopId = %s"
    sql = "INSERT INTO shop_relation (shopName, shopAddr, shopAddrFix, shopTel, shopTelFix, shopId, pla) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    # shop_info = [(name, addr, addr_fix, tel, tel_fix, shop_id, pla),]
    try:
        cursor.executemany(sql, shop_info)
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


def get_shopid_tel_from_shop_relation():
    sql = "SELECT shopId,shopTelFix,pla FROM shop_relation WHERE shopTelFix >1 AND repeat_mark = 0;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def get_shopid_name_from_shop_relation():
    sql = "SELECT shopId,shopName,pla FROM shop_relation WHERE repeat_mark = 0;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def get_shopid_addr_from_shop_relation(repeat_mark):
    sql = "SELECT shopId,shopAddr,pla FROM shop_relation WHERE repeat_mark = %s;"
    try:
        cursor.execute(sql, repeat_mark)
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def update_shop_relation_repeat(shop_id, n):
    sql = "UPDATE shop_relation SET repeat_mark = %s WHERE shopId = %s;"
    try:
        cursor.execute(sql, (n, shop_id))
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


def update_shop_relation_relative_pla(distinct_shop_id, shop_pla, shop_id):
    sql = "UPDATE shop_relation SET " + shop_pla + " = %s WHERE shopId = %s;"
    if shop_pla == "or":
        sql = "UPDATE shop_relation SET" + " o_r" + "= %s WHERE shopId = %s;"
    try:
        cursor.execute(sql, (shop_id, distinct_shop_id))
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


def update_repeat_mark_to_0():
    sql = "UPDATE shop_relation SET repeat_mark = 0 WHERE shop_relation.repeat_mark IS NULL ;"
    try:
        cursor.execute(sql)
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


def up_repeat_mark_to_10():
    sql = 'UPDATE shop_relation SET repeat_mark = 10 WHERE repeat_mark = 0 AND shop_relation.shopName = "大家乐" AND dp IS NULL AND o_r IS NULL AND mfw IS NULL AND ta IS NULL ;'
    sql_ = 'UPDATE shop_relation SET repeat_mark = 10 WHERE repeat_mark = 0 AND shop_relation.shopName = "大家乐快餐" AND dp IS NULL AND o_r IS NULL AND mfw IS NULL AND ta IS NULL;'

    try:
        cursor.execute(sql)
        cursor.execute(sql_)
        db.commit()
    except BaseException, e:
        print e
        db.rollback()

########################################################################################## 以上为处理原始数据


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