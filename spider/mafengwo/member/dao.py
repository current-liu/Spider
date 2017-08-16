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


def select_member_id(table):
    results = []
    try:
        sql = """SELECT memberId FROM %s WHERE memberMark IS NULL""" % table
        cursor.execute(sql)
        results = cursor.fetchall()

    except BaseException, e:
        print e

    return results


def update_member_mark(table, value, member_id):
    try:
        sql = """UPDATE %s SET memberMark = '%s' WHERE memberId = '%s' """ % (table, value, member_id)
        cursor.execute(sql)
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def insert_member(pic, name, gender, vip, duo, zhi, level, loc, profile, follow, fans, contribution, review, member_id):
    try:
        sql = """INSERT INTO member (pic, name, sex, vip, duo, zhiluren, location, level, follows, fans, review, profile, contribution, memberId) 
                  VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""

        cursor.execute(sql % (
            pic, name, gender, vip, duo, zhi, loc, level, follow, fans, review, profile, contribution, member_id))
        db.commit()
    except BaseException, e:
        db.rollback()
        print e
