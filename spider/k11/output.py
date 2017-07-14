# coding=utf-8

import pymysql

db = pymysql.connect("192.168.1.166", "root", "keystone", "k11data")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data


def insert(p, e, c, ct, l, r):
    sql = """INSERT INTO user_voice(
             id,headPic,userName,creatTime,content,label,reply)
             VALUES (1, '%s', '%s', '%s', '%s', '%s', '%s', )""" % (p, e, c, ct, l, r)

    cursor.execute(sql)
