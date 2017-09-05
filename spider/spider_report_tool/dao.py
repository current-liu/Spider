#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/9/5 0005 上午 11:43

base Info
"""
import base_dao

__author__ = 'liuchao'
__version__ = '1.0'

cursor = base_dao.cursor
db = base_dao.db


def insert_spider_status_start(spider_id, status, edit_time):
    sql = """INSERT INTO manager_spiderstatus (spider_id, status, edit_time) VALUES (%s, %s, %s)"""
    try:
        cursor.execute(sql, (spider_id, status, edit_time))
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


def insert_spider_status_end(spider_id, status, edit_time, log, operation_time):
    sql = """INSERT INTO manager_spiderstatus (spider_id, status, edit_time, log, operation_time) VALUES (%s, %s, %s, %s, %s)"""
    try:
        cursor.execute(sql, (spider_id, status, edit_time, log, operation_time))
        db.commit()
    except BaseException, e:
        print e
        db.rollback()
