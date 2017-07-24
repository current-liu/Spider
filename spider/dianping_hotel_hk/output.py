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
        sql = """SELECT id
                    FROM dianping_hotel_hk_liuchao"""
        cursor.execute(sql)
        results = cursor.fetchall()

    except BaseException, e:
        db.rollback()
        print e

    return results


def insert_hotel_shops():
    """
    从dianping_hotel_hk_liuchao中把数据更新到hotel_shops中，
    要在每次准备爬取新的shop前调用一次
    :return:
    """

    sql = """INSERT INTO hotel_shops (
              shopId,shopName,area,walk,star,tag)
              SELECT id,name,addr,walk,star,tags
              FROM dianping_hotel_hk_liuchao d
              WHERE d.id NOT IN (SELECT shopId FROM hotel_shops)"""
    try:
        cursor.execute(sql)
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def update_hotel_shops(shopId, addr, tel, openTime, checkTime, facs, room_facs, services, info):
    """hotel_shop的部分信息已经由insert_hotel_shops插入，剩下的信息在这里补全"""
    sql = """UPDATE hotel_shops SET addr = '%s',tel = '%s',openTime = '%s',checkTime = '%s',facilities = '%s',roomFac = '%s', service = '%s',info = '%s' WHERE hotel_shops.shopId = '%d'""" % (
        addr, tel, openTime, checkTime, facs, room_facs, services, info, shopId)
    try:
        cursor.execute(sql)
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


def insert_hotel_goods(shopIds, roomIds, titles, bedTypes, breakfasts, netTypes, cancelRules, prices):

    # 清空原表
    try:
        cursor.execute("truncate hotel_room")
        db.commit()
    except BaseException, e:
        db.rollback()
        print e


    for (s, r, t, b, bf, n, c, p) in zip(shopIds, roomIds, titles, bedTypes, breakfasts, netTypes, cancelRules, prices):
        sql = """INSERT INTO hotel_room (shopId,roomType,bedType,breakfastInfo,internet,cancelRules,roomPrice)
                  VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%d')""" % (s, t, b, bf, n, c, p)
        try:
            cursor.execute(sql)
            db.commit()
        except BaseException, e:
            db.rollback()
            print e
