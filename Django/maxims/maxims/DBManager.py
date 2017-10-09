#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/9/26 0026 上午 9:21

数据库管理类
"""

import pymysql
from DBUtils.PooledDB import PooledDB
# 自定义的配置文件，主要包含DB的一些基本配置
from config import DB_CONFIG_maxims_analysis


__author__ = 'liuchao'
__version__ = '1.0'


# 数据库实例化类
class DbManager(object):
    def __init__(self):

        self._pool = PooledDB(pymysql, mincached=0, maxcached=10, maxshared=10, maxusage=10000, **DB_CONFIG_maxims_analysis)

    def getConn(self):
        return self._pool.connection()


_dbManager = DbManager()


def getConn():
    """ 获取数据库连接 """
    return _dbManager.getConn()


def executeAndGetId(sql, param=None):
    """ 执行插入语句并获取自增id """
    conn = getConn()
    cursor = conn.cursor()
    id = None
    try:
        if param == None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, param)
        id = cursor.lastrowid
    except BaseException, e:
        print e
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

    return id


def insert(sql, param=None):
    """ 执行sql插入语句 """
    conn = getConn()
    cursor = conn.cursor()
    if param == None:
        rowcount = cursor.execute(sql)
    else:
        rowcount = cursor.execute(sql, param)
    cursor.close()
    conn.close()

    return rowcount


def insertmany(sql, param=None):
    """ 执行多条sql插入语句 """
    conn = getConn()
    cursor = conn.cursor()
    if param is None:
        rowcount = cursor.execute(sql)
    else:
        rowcount = cursor.executemany(sql, param)
    cursor.close()
    conn.close()

    return rowcount


def queryOne(sql, param=None):
    """ 获取一条信息 """
    conn = getConn()
    cursor = conn.cursor()
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    if param is None:
        rowcount = cursor.execute(sql)
    else:
        rowcount = cursor.execute(sql, param)

    # if rowcount > 0:
    #     res = cursor.fetchone()
    # else:
    #     res = None
    res = cursor.fetchone()
    cursor.close()
    conn.close()

    return res


def queryAll(sql, param=None):
    """ 获取所有信息 """
    conn = getConn()
    cursor = conn.cursor()
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    if param is None:
        rowcount = cursor.execute(sql)
    else:
        rowcount = cursor.execute(sql, param)
    # if rowcount > 0:
    #     res = cursor.fetchall()
    # else:
    #     res = None
    res = cursor.fetchall()
    cursor.close()
    conn.close()

    return res


if __name__ == "__main__":
    # res = execute('SELECT count(*) FROM myt_link_list')
    # print str(res)

    res = queryOne('SELECT * FROM myt_link_list LIMIT 20000, 1')
    print str(res)

    res = queryAll('SELECT * FROM myt_link_list LIMIT 10')
    print str(res)


