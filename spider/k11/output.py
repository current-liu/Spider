# coding=utf-8

import pymysql

db = pymysql.connect("192.168.1.166", "root", "keystone", "k11data")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data

