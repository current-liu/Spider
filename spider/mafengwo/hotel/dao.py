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