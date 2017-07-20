# coding=utf-8

import pymysql

db = pymysql.connect("192.168.1.166", "root", "keystone", "k11data", charset="utf8")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data


def insert(i, n, d, a, w, t, p, s, r):
    try:
        sql = """INSERT INTO dianping_hotel_hk_liuchao(
                     id, name, detail_url, addr, walk, tags, price, star, review_num)
                     VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%d')""" % (i, n, d, a, w, t, p, s, r)

        cursor.execute(sql)
        db.commit()
    except BaseException, e:
        db.rollback()
        print e

def downloadShopUrl():
    results = []
    try:
        sql = """SELECT detail_url
                    FROM dianping_hotel_hk_liuchao"""
        cursor.execute(sql)
        results = cursor.fetchall()

    except BaseException, e:
        db.rollback()
        print e

    return results

