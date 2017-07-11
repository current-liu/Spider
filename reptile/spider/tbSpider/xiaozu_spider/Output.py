# -*- coding:utf-8 -*-

from mysql import connector

class Output(object):
    def __init__(self):
        self.conn = connector.connect(host="192.168.1.154",user="root",password="root",database="hkstar",charset="big5",buffered=True)

    def insertTitle(self,title):
        insert_sql = "insert into title values('"+title['titleId']+"','"+title['title']+"','"+title['author']+"','"+title['publishTime']+"')"
        cursor = self.conn.cursor()
        # 输出测试代码
        # print(data_result_list)
        cursor.execute(insert_sql)
        # cursor.executemany(insert_sql,data_result_list)
        cursor.close()
        self.conn.commit()

    def insertReply(self, data_list):
        insert_sql = "insert into reply values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor = self.conn.cursor()
        # 输出测试代码
        # print(data_result_list)
        cursor.executemany(insert_sql, data_list)
        cursor.close()
        self.conn.commit()

    def title_is_exist(self, titleId):
        sql = "select * from title where titleId=" + titleId
        cursor = self.conn.cursor()
        cursor.execute(sql)
        num = cursor.fetchall()
        if num == None or len(num) == 0:
            return False
        else:
            return True
    def reply_is_exist(self,replyId):
        sql = "select * from reply where replyId=" + replyId
        cursor = self.conn.cursor()
        num = cursor.execute(sql)
        if num == None or num == 0:
            return False
        else:
            return True

    def close(self):
        self.conn.close()
