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


def insert_shopping_shop(shoppings, area):
    sql = 'INSERT INTO shopping_shop (shopId, picUrl,area) VALUES (%s,%s,%s)'
    for shopping in shoppings:
        try:
            cursor.execute(sql, (shopping[0], shopping[1], area))
            db.commit()
        except BaseException, e:
            db.rollback()
            print e


def update_shopping_shop(shop_name, shop_name_en, score, star, review_num, tip, site, tel, intro, trans, loc, shop_id):
    sql = """UPDATE shopping_shop SET shopName=%s, shopNameEn=%s, addr=%s, tip=%s, site=%s,tel=%s, score=%s, star=%s, intro=%s, trans=%s,reviewNum=%s              
              WHERE shopId = %s"""

    try:
        cursor.execute(sql, (shop_name, shop_name_en, loc, tip, site, tel, score, star, intro, trans, review_num, shop_id))
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def insert_shopping_review(shop_id, review_ids, member_ids, likes, contents, stars, times):
    sql = """INSERT INTO shopping_review (reviewId,memberId,shopId,reviewStar,content,creatTime,likes)
                         VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    msg = ""
    index = 0
    for (q, w, e, r, t, y) in zip(review_ids, member_ids, likes, contents, stars, times):
        try:
            cursor.execute(sql, (q, w, shop_id, t, r, y, e))
            db.commit()
        except BaseException, e:
            db.rollback()
            print e
            if str(e).__contains__("for key 'PRIMARY'"):
                # 由于一条评论信息可能出现在连续的两页上，故一个页面上有一个主键冲突不能判定该页面已经爬取过
                index += 1

    if index == 15:
        msg = "for key 'PRIMARY'"
    return msg
