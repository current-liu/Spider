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


def insert_hotel_shops(shopIds, picUrls, areas, review_nums, travel_nums):
    for q, w, e, r, t in zip(shopIds, picUrls, areas, review_nums, travel_nums):
        try:
            sql = """INSERT INTO hotel_shops(
                         shopId, picUrl,area,reviewNum,travelsNum)
                         VALUES ('%s', '%s', '%s', '%s', '%s')""" % (q, w, e, r, t)
            cursor.execute(sql)
            db.commit()
        except BaseException, e:
            db.rollback()
            print e


def update_hotel_shops(shop_name, shop_name_en, score, loc, checkIn, checkOut, built, room_num, service, info, \
                       sco_loc, sco_ser, sco_clear, sco_comfo, sco_fac, sco_food, tag, shopId):
    try:
        sql = """UPDATE hotel_shops SET shopName = '%s', shopNameEn = '%s', score = '%s', addr = '%s', checkIn = '%s', checkOut = '%s', openTime = '%s', roomNum = '%s', service = '%s', info = '%s', 
                  scoLoc = '%s', scoSer = '%s', scoClear = '%s', scoComfo = '%s', scoFac = '%s', scoFood = '%s', tag = '%s' WHERE shopId = '%d'"""

        cursor.execute(sql % (shop_name, shop_name_en, score, loc, checkIn, checkOut, built, room_num, service, info, \
                              sco_loc, sco_ser, sco_clear, sco_comfo, sco_fac, sco_food, tag, int(shopId)))
        db.commit()

    except BaseException, e:
        db.rollback()
        print e


def insert_hotel_review(shop_id, review_ids, member_ids, likes, contents, stars, times):
    sql = """INSERT INTO hotel_review (reviewId,memberId,shopId,reviewStar,content,creatTime,likes)
                         VALUES('%s','%s','%s','%s','%s','%s','%s')"""
    msg = ""
    index = 0
    for (q, w, e, r, t, y) in zip(review_ids, member_ids, likes, contents, stars, times):
        try:
            cursor.execute(sql % (q, w, shop_id, t, r, y, e))
            db.commit()
        except BaseException, e:
            db.rollback()
            print e
            if str(e).__contains__("for key 'PRIMARY'"):
                # 由于一条评论信息可能出现在连续的两页上，故一个页面上有一个主键冲突不能判定该页面已经爬取过
                index += 1

    if index == 10:
        msg = "for key 'PRIMARY'"
    return msg
