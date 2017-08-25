#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/25 0025 下午 12:00

base Info
数据库连接池管理模块
"""

__author__ = 'liuchao'
__version__ = '1.0'

import pymysql;
from DBUtils.PooledDB import PooledDB;

import db_config as Config;

'''
@功能：PT数据库连接池
'''


class PTConnectionPool(object):
    __pool = None;

    def __enter__(self):
        self.conn = self.getConn();
        self.cursor = self.conn.cursor();

        print "PT数据库创建con和cursor";
        return self;

    def getConn(self):
        if self.__pool is None:
            self.__pool = PooledDB(creator=pymysql, mincached=Config.DB_MIN_CACHED, maxcached=Config.DB_MAX_CACHED,
                                   maxshared=Config.DB_MAX_SHARED, maxconnections=Config.DB_MAX_CONNECYIONS,
                                   blocking=Config.DB_BLOCKING, maxusage=Config.DB_MAX_USAGE,
                                   setsession=Config.DB_SET_SESSION, host=Config.DB_MFW_HOST, port=Config.DB_MFW_PORT,
                                   user=Config.DB_MFW_USER, passwd=Config.DB_MFW_PASSWORD, db=Config.DB_MFW_DBNAME,
                                   use_unicode=False, charset=Config.DB_CHARSET);

        return self.__pool.connection()

    # def cursor(self):
    #     return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    """
    @summary: 释放连接池资源
    """

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()

        print "PT连接池释放con和cursor";


'''
@功能：获取PT数据库连接
'''


def getPTConnection():
    return PTConnectionPool()
