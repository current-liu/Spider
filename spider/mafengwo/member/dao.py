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


def select_member_id_not_in_member(table):
    """查询不在表member中的member_id"""
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
        sql = """UPDATE %s SET memberMark = '%s' WHERE memberId in (SELECT memberId FROM member) """ % (table, value)
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


def select_member_id_not_in_member_review():
    """查询不在表member中的member_id"""
    results = []
    try:
        sql = """SELECT member.memberId FROM member LEFT JOIN member_review ON member.memberId = member_review.memberId WHERE member_review.memberId IS NULL"""
        cursor.execute(sql)
        results = cursor.fetchall()

    except BaseException, e:
        print e

    return results
