# coding=utf-8
"""Python CGI编程
    Common Gateway Interface:通用网关接口，它是一段程序，运行在服务器上如：
        HTTP服务器，提供同客户端HTML页面的接口"""

"""Python MySQl
"""
import pymysql

db = pymysql.connect("localhost", "root", "1234", "test")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data

sql = """INSERT INTO emp(NAME, AGE,  INCOME)
         VALUES ('Mac', 20, 2000)"""
sql1 = """SELECT * FROM emp"""
try:
    cursor.execute(sql1)
    r = cursor.fetchall()
    db.commit()
except:
    db.rollback()


db.close()


