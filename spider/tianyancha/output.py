# coding=utf-8

import pymysql

db = pymysql.connect("192.168.1.166", "root", "keystone", "k11data", charset="utf8")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data


def insert(p, e, c, ct, l, r):
    try:
        sql = """INSERT INTO user_voice(
                     headPic,userName,creatTime,content,label,reply)
                     VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" % (p, e, c, ct, l, r)

        cursor.execute(sql)
        # 获取自增id
        new_id = cursor.lastrowid
        print new_id
        db.commit()
    except BaseException, e:
        db.rollback()
        print e

