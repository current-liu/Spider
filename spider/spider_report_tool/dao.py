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


def insert_spider_status_start(spider_id, status, edit_time, log):
    sql = """INSERT INTO manager_spiderstatus (spider_id, status, edit_time, log) VALUES (%s, %s, %s, %s)"""
    try:
        cursor.execute(sql, (spider_id, status, edit_time, log))
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


def update_spider_status(spider_id, status):
    sql = """UPDATE manager_spider SET status=%s WHERE id = %s"""
    try:
        cursor.execute(sql, (status, spider_id))
        db.commit()
    except BaseException, e:
        print e
        db.rollback()


def update_spiderstatus_status(spider_id, status):
    sql = """UPDATE manager_spiderstatus SET status=%s 
              WHERE id = 
              (SELECT id FROM 
              (SELECT id FROM manager_spiderstatus WHERE status=2 AND spider_id=%s ORDER BY edit_time DESC ) as t1 LIMIT 1)"""
    try:
        cursor.execute(sql, (status, spider_id))
        db.commit()
    except BaseException, e:
        print e
        db.rollback()

if __name__ == '__main__':
    update_spider_status(1, 2)
