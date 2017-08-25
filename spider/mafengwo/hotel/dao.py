#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/10 0010 下午 3:01

base Info
"""
from mafengwo import base_dao
# from mafengwo.db_connection_pool import getPTConnection
__author__ = 'Administrator'
__version__ = '1.0'
cursor = base_dao.cursor
db = base_dao.db


def insert_hotel_shop(shopIds, picUrls, areas, review_nums, travel_nums):
    for q, w, e, r, t in zip(shopIds, picUrls, areas, review_nums, travel_nums):
        try:
            sql = """INSERT INTO hotel_shop(
                         shopId, picUrl,area,reviewNum,travelsNum)
                         VALUES ('%s', '%s', '%s', '%s', '%s')""" % (q, w, e, r, t)
            cursor.execute(sql)
            db.commit()
        except BaseException, e:
            db.rollback()
            print e


def update_hotel_shop(shop_name, shop_name_en, score, loc, checkIn, checkOut, built, room_num, service, info, \
                      sco_loc, sco_ser, sco_clear, sco_comfo, sco_fac, sco_food, tag, shopId):
    try:
        sql = """UPDATE hotel_shop SET shopName = '%s', shopNameEn = '%s', score = '%s', addr = '%s', checkIn = '%s', checkOut = '%s', openTime = '%s', roomNum = '%s', service = '%s', info = '%s', 
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


def download_hotel_shopIds_unselected(today_str):
    """今天还没有查过房价的酒店id"""
    results = []
    try:
        sql = """SELECT shopId
                    FROM hotel_shop WHERE
                    shopId NOT IN (SELECT shopId FROM hotel_room WHERE queryTime = '%s')"""
        cursor.execute(sql % today_str)
        results = cursor.fetchall()

    except BaseException, e:
        db.rollback()
        print e

    return results


def insert_hotel_room(shopId, rooms_info_total, query_time, ota):
    sql = """INSERT INTO hotel_room (shopId, roomType, queryTime, ota, roomPrice_0, roomPrice_1, roomPrice_2, roomPrice_3, roomPrice_4)
              VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""

    try:
        cursor.execute(sql % (
            shopId, rooms_info_total[5], query_time, ota, rooms_info_total[0], rooms_info_total[1], rooms_info_total[2],
            rooms_info_total[3], rooms_info_total[4]))
        db.commit()
    except BaseException, e:
        db.rollback()
        print e
