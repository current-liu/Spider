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

reload(sys)
sys.setdefaultencoding("utf8")

# db = pymysql.connect("127.0.0.1", "root", "liu1991chao", "spider_manager", charset="utf8mb4")
# 严猛 和上面的交换
db = pymysql.connect("192.168.1.166", "root", "keystone", "spider_manager", charset="utf8mb4")

cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data

__author__ = 'Administrator'
__version__ = '1.0'


def get_spider_on_date(date):
    sql = """SELECT * FROM manager_spider
              WHERE manager_spider.id IN
              (SELECT DISTINCT spider_id FROM manager_spiderstatus WHERE edit_time LIKE %s)"""
    try:
        cursor.execute(sql, date + "%")
        results = cursor.fetchall()

    except BaseException, e:
        print e
    return results


def get_spider_id_on_date(date):
    sql = """SELECT DISTINCT spider_id FROM manager_spiderstatus WHERE edit_time LIKE %s"""
    try:
        cursor.execute(sql, date + "%")
        results = cursor.fetchall()

    except BaseException, e:
        print e
    return results


def get_error_spider_id_on_date(date):
    sql = """SELECT DISTINCT spider_id FROM manager_spiderstatus WHERE status=3 AND edit_time LIKE %s """
    try:
        cursor.execute(sql, date + "%")
        results = cursor.fetchall()

    except BaseException, e:
        print e
    return results


def get_spider_on_day_every_hour(date):
    sql = """SELECT EXTRACT(HOUR FROM `manager_spiderstatus`.`edit_time`) "hour", COUNT(DISTINCT(spider_id)) FROM manager_spiderstatus WHERE edit_time LIKE %s GROUP BY hour;"""
    try:
        cursor.execute(sql, date + "%")
        results = cursor.fetchall()

    except BaseException, e:
        print e
    return results


def get_date_to_update_spider_num():
    sql = """SELECT date FROM manager_spider_num WHERE date_cal < current_date() AND spider_num IS NULL;"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def update_spider_num(date):
    sql = """UPDATE manager_spider_num SET spider_num = (SELECT COUNT(id) FROM manager_spider 
              WHERE create_time < %s) WHERE date_cal = %s; """
    try:
        cursor.executemany(sql, date)
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


def select_spider_num_up_to_date():
    sql = """SELECT date_cal, spider_num FROM manager_spider_num WHERE date_cal < CURRENT_DATE();"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def select_spider_num_up_to_month(date_):
    sql = """SELECT DATE_FORMAT(date_cal, "%%Y-%%m" ) "month", max(spider_num) "spider_num" FROM manager_spider_num WHERE DATE_FORMAT(date_cal, "%%Y")=%s AND date_cal < current_date GROUP BY month ORDER BY month;"""
    try:
        cursor.execute(sql, date_)
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def get_spider_num_group_by_date(status, type_):
    sql = """SELECT c.datelist,COUNT(DISTINCT t.spider_id) num
              FROM calendar_to_yesterday c LEFT JOIN manager_spiderstatus_with_date t
              ON c.datelist = t.edit_date
              AND t.status = %s""" + type_ + """
              GROUP BY c.datelist
              ORDER BY c.datelist;"""
    try:
        cursor.execute(sql, status)
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def get_spider_num_group_by_hour(edit_date, type_):
    sql = """SELECT  i ,count(edit_hour) 
              FROM num LEFT JOIN manager_spiderstatus_with_date t 
              ON i = edit_hour AND t.status = 1 AND t.edit_date = %s AND t.type = %s
              GROUP BY i ORDER BY i;"""

    try:
        cursor.execute(sql, (edit_date, type_))
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def get_spider_num_group_by_month(edit_date, status):
    sql = """SELECT num.m,COUNT(DISTINCT t.spider_id) num
              FROM num LEFT JOIN manager_spiderstatus_with_date t
              ON num.m = t.edit_month
              AND t.edit_year = %s AND t.status = %s
              GROUP BY num.m
              ORDER BY num.m"""
    try:
        cursor.execute(sql, (edit_date, status))
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def get_spider_log_on_date(spider_id, log_date):
    sql = """SELECT spider_id,edit_time,log,status FROM manager_spiderstatus WHERE spider_id = %s AND DATE_FORMAT(edit_time, "%%Y-%%m-%%d" ) = %s;"""
    try:
        cursor.execute(sql, (spider_id, log_date))
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results

if __name__ == '__main__':
    get_error_spider_id_on_date("2017-09-06")
