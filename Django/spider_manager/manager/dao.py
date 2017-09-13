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

db = pymysql.connect("127.0.0.1", "root", "liu1991chao", "spider_manager", charset="utf8mb4")
# 严猛 和上面的交换
# db = pymysql.connect("192.168.1.166", "root", "keystone", "spider_manager", charset="utf8mb4")

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
    sql = """SELECT date FROM manager_spider_num WHERE date < current_date() AND spider_num IS NULL;"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def update_spider_num(date):
    sql = """UPDATE manager_spider_num SET spider_num = (SELECT COUNT(id) FROM manager_spider 
              WHERE create_time < %s) WHERE date = %s; """
    try:
        cursor.executemany(sql, date)
        db.commit()
    except BaseException, e:
        print e


def select_spider_num_up_to_date():
    sql = """SELECT date, spider_num FROM manager_spider_num WHERE date < CURRENT_DATE();"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


def get_spider_num_group_by_date(status, type):
    sql = """SELECT c.datelist,COUNT(DISTINCT t.spider_id) num
              FROM calendar_to_yesterday c LEFT JOIN manager_spiderstatus_with_date t
              ON c.datelist = t.edit_date
              AND t.status = %s AND t.type = %s
              GROUP BY c.datelist
              ORDER BY c.datelist;"""
    try:
        cursor.execute(sql, (status, type))
        results = cursor.fetchall()
    except BaseException, e:
        print e
    return results


if __name__ == '__main__':
    get_error_spider_id_on_date("2017-09-06")
