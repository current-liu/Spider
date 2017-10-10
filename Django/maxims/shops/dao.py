#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/11 0011 上午 11:23

base Info
"""

import sys
import pymysql
from maxims import config
from maxims import DBManager

reload(sys)
sys.setdefaultencoding("utf8")

__author__ = 'Administrator'
__version__ = '1.0'

conf = config.DB_CONFIG_maxims_analysis
conn = pymysql.connect(**conf)
curs = conn.cursor()


def get_all_id(shop_id):
    """没有的平台，id返回0"""
    # sql = """SELECT id, o_r , mfw,ta, dp FROM view_shop_relation where id = %s"""
    sql = """SELECT id,(CASE WHEN o_r IS NOT NULL THEN o_r ELSE 0 END) o_r ,(CASE WHEN mfw IS NOT NULL THEN mfw ELSE 0 END) mfw,(CASE WHEN ta IS NOT NULL THEN ta ELSE 0 END) ta, (CASE WHEN dp IS NOT NULL THEN dp ELSE 0 END) dp
                      FROM view_shop_relation WHERE id = %s"""
    results = DBManager.queryAll(sql, shop_id)

    return results


def select_shop_all():
    sql = """SELECT id,shopName,(CASE WHEN o_r IS NOT NULL THEN 1 ELSE 0 END) o_r ,(CASE WHEN mfw IS NOT NULL THEN 1 ELSE 0 END) mfw,(CASE WHEN ta IS NOT NULL THEN 1 ELSE 0 END) ta, (CASE WHEN dp IS NOT NULL THEN 1 ELSE 0 END) dp
              FROM view_shop_relation"""
    results = DBManager.queryAll(sql)
    return results


def select_shop_all_info(shop_id):
    sql = """SELECT id,shopName,shopAddr,shopTelFix FROM view_shop_relation WHERE id = %s """
    results = DBManager.queryAll(sql, shop_id)
    return results


def select_dp_pic(shop_id):
    sql = """SELECT pic FROM shops_dpshop WHERE shopId = %s """
    results = DBManager.queryAll(sql, shop_id)
    return results


def select_ta_pic(shop_id):
    sql = """SELECT pic FROM shops_tashop WHERE shopId = %s """
    results = DBManager.queryAll(sql, shop_id)
    return results


def select_or_pic(shop_id):
    sql = """SELECT pic FROM shops_orshop WHERE shopId = %s """
    results = DBManager.queryAll(sql, shop_id)
    return results


def select_mfw_pic(shop_id):
    sql = """SELECT pic FROM shops_mfwshop WHERE shopId = %s """
    results = DBManager.queryAll(sql, shop_id)
    return results


def get_all_shop_ids():
    sql = """SELECT id,shopName,(CASE WHEN dp IS NOT NULL THEN dp ELSE 0 END) dp, (CASE WHEN o_r IS NOT NULL THEN o_r ELSE 0 END) o_r ,(CASE WHEN mfw IS NOT NULL THEN mfw ELSE 0 END) mfw,(CASE WHEN ta IS NOT NULL THEN ta ELSE 0 END) ta
              FROM view_shop_relation"""

    results = DBManager.queryAll(sql)
    return results


def get_shop_star_from_pla(pla, shop_id):
    sql = "SELECT star FROM shops_" + pla + "shop WHERE shopId = %s"

    results = DBManager.queryAll(sql, shop_id)
    return results


def get_shop_star_and_more_from_dp(shop_id):
    sql = """SELECT star,taste,environment,service FROM shops_dpshop WHERE shopId = %s"""

    results = DBManager.queryAll(sql, shop_id)
    return results


# ======================================================================================================
# 以下为处理原始数据


def selete_shops_info(platform):
    sql_or = """SELECT shopId, shopAddress, shopName, shopTel FROM or_shops;"""
    sql_dp = """SELECT shopId, addr, shopName, addr FROM dp_shops;"""
    sql_mfw = """SELECT shopId,addr, shopName, tel FROM mfw_shops;"""
    sql_ta = """SELECT shopId,addr, shopName,telephone FROM ta_shops;"""
    platform_table = {"or": sql_or, "dp": sql_dp, "mfw": sql_mfw, "ta": sql_ta}

    try:
        sql = platform_table[platform]
        curs.execute(sql)
        results = curs.fetchall()
    except BaseException, e:
        print e

    return results


def insert_shop_relation(shop_info):
    sql = "INSERT INTO shop_relation (shopName, shopAddr, shopAddrFix, shopTel, shopTelFix, shopId, pla) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    try:
        curs.executemany(sql, shop_info)
        conn.commit()
    except BaseException, e:
        print e
        conn.rollback()


def update_repeat_mark_to_0():
    sql = "UPDATE shop_relation SET repeat_mark = 0 WHERE shop_relation.repeat_mark IS NULL ;"
    try:
        curs.execute(sql)
        conn.commit()
    except BaseException, e:
        print e
        conn.rollback()


def get_shopid_tel_from_shop_relation():
    sql = "SELECT shopId,shopTelFix,pla FROM shop_relation WHERE shopTelFix >1 AND repeat_mark = 0;"
    try:
        curs.execute(sql)
        results = curs.fetchall()
    except BaseException, e:
        print e
    return results


def get_shopid_name_from_shop_relation():
    sql = "SELECT shopId,shopName,pla FROM shop_relation WHERE repeat_mark = 0;"
    try:
        curs.execute(sql)
        results = curs.fetchall()
    except BaseException, e:
        print e
    return results


def get_shopid_addr_from_shop_relation(repeat_mark):
    sql = "SELECT shopId,shopAddr,pla FROM shop_relation WHERE repeat_mark = %s;"
    try:
        curs.execute(sql, repeat_mark)
        results = curs.fetchall()
    except BaseException, e:
        print e
    return results


def update_shop_relation_repeat(shop_id, n):
    sql = "UPDATE shop_relation SET repeat_mark = %s WHERE shopId = %s;"
    try:
        curs.execute(sql, (n, shop_id))
        conn.commit()
    except BaseException, e:
        print e
        conn.rollback()


def update_shop_relation_relative_pla(distinct_shop_id, shop_pla, shop_id):
    sql = "UPDATE shop_relation SET " + shop_pla + " = %s WHERE shopId = %s;"
    if shop_pla == "or":
        sql = "UPDATE shop_relation SET" + " o_r" + "= %s WHERE shopId = %s;"
    try:
        curs.execute(sql, (shop_id, distinct_shop_id))
        conn.commit()
    except BaseException, e:
        print e
        conn.rollback()


def update_repeat_mark_to_0():
    sql = "UPDATE shop_relation SET repeat_mark = 0 WHERE shop_relation.repeat_mark IS NULL ;"
    try:
        curs.execute(sql)
        conn.commit()
    except BaseException, e:
        print e
        conn.rollback()


def up_repeat_mark_to_10():
    sql = 'UPDATE shop_relation SET repeat_mark = 10 WHERE repeat_mark = 0 AND shop_relation.shopName = "大家乐" AND dp IS NULL AND o_r IS NULL AND mfw IS NULL AND ta IS NULL ;'
    sql_ = 'UPDATE shop_relation SET repeat_mark = 10 WHERE repeat_mark = 0 AND shop_relation.shopName = "大家乐快餐" AND dp IS NULL AND o_r IS NULL AND mfw IS NULL AND ta IS NULL;'

    try:
        curs.execute(sql)
        curs.execute(sql_)
        conn.commit()
    except BaseException, e:
        print e
        conn.rollback()
