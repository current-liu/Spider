#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/10 0010 下午 3:01

base Info
"""
from mafengwo import base_dao

__author__ = 'Administrator'
__version__ = '1.0'
cursor = base_dao.cursor
db = base_dao.db


def insert_attraction_shop(attractions):
    sql = 'INSERT INTO attraction_shop (shopId, picUrl) VALUES ("%d","%s" )'
    for attraction in attractions:
        try:
            cursor.execute(sql % (attraction[0], attraction[1]))
            db.commit()
        except BaseException, e:
            db.rollback()
            print e


def update_attraction_shop(shop_name, shop_name_en, info, tel, site, time_use, trans, ticket, bussiness_time,
                           loc, inner_scenic, review_num, shop_id):
    sql = """UPDATE attraction_shop SET 
              shopName=%s, shopNameEn=%s, info=%s, addr=%s, tel=%s, bussinessTime=%s, innerScenic=%s, 
              reviewNum=%s, ticket=%s, timeUse=%s, site=%s, trans=%s
              WHERE shopId = %s"""
    try:
        cursor.execute(sql, (shop_name, shop_name_en, info, loc, tel, bussiness_time, inner_scenic, review_num,
                             ticket, time_use, site, trans, shop_id))
        db.commit()
    except BaseException, e:
        db.rollback()
        print e
