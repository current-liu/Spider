#!/usr/bin/env python
# -*- coding: utf-8 -*-
import facebook
import requests
import pymysql
import datetime
import threading
from DBUtils.PooledDB import PooledDB
dbpool = PooledDB(creator=pymysql, mincached=10, maxcached=10, maxshared=20, maxconnections=50, host='202.110.49.146', user='root', passwd='keystone',db='dpark',port=3381,charset='utf8mb4' )
#dbpool = PooledDB(creator=pymysql, mincached=10, maxcached=10, maxshared=20, maxconnections=100, host='localhost', user='root', passwd='123456',db='facebook',port=3306,charset='utf8mb4' )

graph = facebook.GraphAPI(access_token='1798673940392223|16crjBJNqFyNgCOo0BPpY4dgFqw', version='2.7')

sql = "select * from facebook_comments where mark = 0 ORDER BY createdTime DESC LIMIT 300000"
sql1 = "replace into facebook_likes(statusID,likesID,likesName)values (%s,%s,%s)"
sql2 = '''REPLACE INTO facebook_comments(commentID,message,createdTime,fromID,fromName,statusID,comment_count,like_count,mark)VALUES (%s,%s,%s,%s,%s,%s,0,0,0)'''
sql3 = "REPLACE INTO facebook_comments(statusID,commentID,createdTime,fromID,fromName,message,comment_count,like_count,mark)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,1)"


def trans_date(a): #处理时间格式
    b = a.replace("T", " ")
    c = b.replace("+0000", "")
    d = datetime.datetime.strptime(c, "%Y-%m-%d %H:%M:%S")
    e = d + datetime.timedelta(hours=8)
    f = e.strftime("%Y-%m-%d %H:%M:%S")
    return f
def get_comment():
    conn = dbpool.connection()
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    conn.close()
    return results

def get_ID_10(num, commentlist):
    return commentlist[num*10:(num+1)*10]

def get_Comment_CommentLike(i0, i1, i2, i3, i4, i5):
    conn = dbpool.connection()
    cur = conn.cursor()
    print i1
    indexLike = 0
    indexComment = 0
    like = []
    comment = []
    try:
        likes = graph.get_all_connections(id=i1, connection_name='likes')
        comments = graph.get_all_connections(id=i1, connection_name='comments')
        for i in likes:
            indexLike += 1
            like.append([i1, i['id'], i['name']])
        cur.executemany(sql1, like)
        conn.commit()
        print 'like_count:', indexLike
        for j in comments:
            indexComment += 1
            a = j['id']
            b = j['message']
            c = trans_date(j['created_time'])
            d = j['from']['id']
            e = j['from']['name']
            comment.append([a, b, c, d, e, i1])
        cur.executemany(sql2, comment)
        conn.commit()
        print 'comment_count:',indexComment
    except Exception as e:
        print "Error is as follows!!!", e
    param = (i0, i1, i2, i3, i4, i5, indexComment, indexLike)
    cur.execute(sql3, param)
    conn.commit()
    conn.close()
if __name__ == "__main__":
    a = datetime.datetime.now()
    allComments = get_comment()
    index = 0

    while True:
        print index
        threads = []

        loops = get_ID_10(index, allComments)
        if not loops:
            break
        length = range(len(loops))
        for i in length:
            t = threading.Thread(target=get_Comment_CommentLike, args=(loops[i][0], loops[i][1], loops[i][2], loops[i][3], loops[i][4], loops[i][5]))
            threads.append(t)
        for i in length:
            threads[i].start()
        for i in length:
            threads[i].join()
        index += 1


    b = datetime.datetime.now()
    print b-a
