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


def select_member_id_not_in_member(table):
    """查询不在表member中的member_id"""
    # TODOmember_fix

    results = []
    try:
        sql = """SELECT DISTINCT %s.memberId FROM %s LEFT JOIN member ON %s.memberId = member.memberId WHERE member.memberId IS NULL""" % (
            table, table, table)
        cursor.execute(sql)
        results = cursor.fetchall()

    except BaseException, e:
        print e

    return results


def update_member_mark(table, value):
    try:
        sql = """UPDATE %s SET memberMark = %s WHERE memberId in (SELECT memberId FROM member) """ % (table, value)
        cursor.execute(sql)
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def insert_member(pic, name, gender, vip, duo, zhi, level, loc, profile, follow, fans, contribution, review, member_id):


    try:
        sql = """INSERT INTO member (pic, name, sex, vip, duo, zhiluren, location, level, follows, fans, review, profile, contribution, memberId) 
                  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        cursor.execute(sql, (
            pic, name, gender, vip, duo, zhi, loc, level, follow, fans, review, profile, contribution, member_id))
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def select_member_id_not_in_member_path(sql_):
    """查询不在表member_path中的member_id"""

    results = []
    try:
        sql = """SELECT member.memberId FROM member LEFT JOIN member_path ON member.memberId = member_path.memberId WHERE member_path.memberId IS NULL """
        cursor.execute(sql + sql_)
        results = cursor.fetchall()

    except BaseException, e:
        print e

    return results


def insert_member_path(member_reviews):
    index = 0
    msg = ""
    try:
        sql = """INSERT INTO member_path (memberId, shopId, shopName, reviewId, star, likes, createTime, typeId) 
                  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.executemany(sql, member_reviews)
        db.commit()
    except BaseException, e:
        print e
        db.rollback()
        # if str(e).__contains__("for key 'PRIMARY'"):
        #     # 由于一条评论信息可能出现在连续的两页上，故一个页面上有一个主键冲突不能判定该页面已经爬取过
        #     index += 1

    # if index == 40:
    #     msg = "for key 'PRIMARY'"
    # return msg



