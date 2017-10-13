#!/usr/bin/env python
# -*- coding: utf-8 -*-
#此程序是获取一个新的主页的状态，以及状态的评论和分享
import facebook
import requests
import pymysql
import datetime
import threading
from time import sleep
from DBUtils.PooledDB import PooledDB
dbpool = PooledDB(creator=pymysql, mincached=10, maxcached=10, maxshared=20, maxconnections=50, host='202.110.49.146', user='root', passwd='keystone',db='dpark',port=3381,charset='utf8mb4' )
#dbpool = PooledDB(creator=pymysql, mincached=10, maxcached=10, maxshared=20, maxconnections=30, host='localhost', user='root', passwd='123456',db='facebook',port=3306,charset='utf8mb4' )

#graph = facebook.GraphAPI(access_token='312819675783598|Vb6UKYBHG0bhlCL2EbyoBViACSE', version='2.7')
graph = facebook.GraphAPI(access_token='1537948926257443|kfpadyau2sHmH_u25oj7oZYwX50', version='2.7')

sql1 = "replace into facebook_likes(statusID,likesID,likesName)values (%s,%s,%s)"
sql2 = '''REPLACE INTO facebook_comments(commentID,message,createdTime,fromID,fromName,statusID,comment_count,like_count,mark)VALUES (%s,%s,%s,%s,%s,%s,0,0,0)'''

def get_allPage():
    conn = dbpool.connection()
    cur = conn.cursor()
    sqlGet = "select * from fb_pageprofile WHERE mark = 5"
    cur.execute(sqlGet)
    ID = cur.fetchall()
    conn.close()
    return ID
def get_allStatus():
    conn = dbpool.connection()
    cur = conn.cursor()
    sqlGet = "select * from facebook_status WHERE mark = 0 ORDER BY createdTime DESC "
    cur.execute(sqlGet)
    ID = cur.fetchall()
    conn.close()
    return ID

def get_fb_page_post(fb_page_id):  #获取发表的状态
    args = {'fields': 'posts'}
    page = graph.get_object(fb_page_id, **args)
    return page.get('posts', 0)

def trans_date(a):  #处理时间格式
    b = a.replace("T", " ")
    c = b.replace("+0000", "")
    d = datetime.datetime.strptime(c, "%Y-%m-%d %H:%M:%S")
    e = d + datetime.timedelta(hours=8)
    f = e.strftime("%Y-%m-%d %H:%M:%S")
    return f
def get_post_list(fb_page_id, createdName):  #获取一个用户在2017-01-01之后发送的帖子
    conn = dbpool.connection()
    cur = conn.cursor()
    s = get_fb_page_post(fb_page_id)
    time = '2017-01-01'
    breakPiont = 1
    while (True):  # 获取用户发送的全部的status
        try:
            for item in s['data']:
                try:
                    a = item['id']
                    b = trans_date(item['created_time'])
                    if b < time:
                        breakPiont = 2
                        break
                    c = createdName
                    d = item['message']
                    sql = '''replace INTO facebook_status(statusID,createdTime,createdName,message,reactions_count,comments_count,shares_count,mark)VALUES (%s,%s,%s,%s,0,0,0,0)'''
                    param = (a, b, c, d)
                    cur.execute(sql, param)
                    conn.commit()
                except Exception as e:
                    print e
                    continue
            if breakPiont == 2:
                break
            s = requests.get(s['paging']['next']).json()
        except KeyError:
            break
    print createdName, ": has done!"
    conn.close()
def getComments(statusID):
    conn = dbpool.connection()
    cur = conn.cursor()
    comment = []
    indexComment = 0
    comments = graph.get_all_connections(id=statusID, connection_name='comments')
    for j in comments:
        indexComment += 1
        a = j['id']
        b = j['message']
        c = trans_date(j['created_time'])
        d = j['from']['id']
        e = j['from']['name']
        comment.append([a, b, c, d, e, statusID])
    cur.executemany(sql2, comment)
    conn.commit()
    conn.close()
    return indexComment
def getCommentShare(statusID):
    conn = dbpool.connection()
    cur = conn.cursor()
    indexLike = 0
    indexComment = 0
    indexShare = 0
    try:
        indexComment = getComments(statusID)
        shares = graph.get_object(id=statusID, fields='shares')
        indexShare = shares['shares']['count']
        print "commentCount:", indexComment, "   shareCount: ", indexShare
    except Exception as e:
        print e
        print "Error!!"
    sql = "update facebook_status set reactions_count = '%s',comments_count= '%s',shares_count = '%s',mark = 3 WHERE statusID = '%s'" % (indexLike, indexComment, indexShare, statusID)
    cur.execute(sql)
    conn.commit()
    conn.close()

def get_List_10(num, somelist):
    return somelist[num*10:(num+1)*10]


def commentShare_threading():
    index = 0
    print index
    status = get_allStatus()
    while True:
        threads = []
        loops = get_List_10(index, status)
        if not loops:
            break
        length = range(len(loops))
        for i in length:
            t = threading.Thread(target=getCommentShare, args=(loops[i][0],))
            threads.append(t)
        for i in length:
            threads[i].start()
        for i in length:
            threads[i].join()
        index += 1

if __name__ == "__main__":
    a = datetime.datetime.now()
    page = get_allPage()
    print page
    for i in page:
        get_post_list(i[0], i[1])
        conn = dbpool.connection()
        cur = conn.cursor()
        sqlp = "update fb_pageprofile set mark=0 where pageID ='%s'" % (i[0])
        cur.execute(sqlp)
        conn.commit()
        conn.close()
    print "Status get has Done.Now begin to get the comment and share!!!"
    print"Begin to get the status comments and shares!!"
    sleep(2)
    commentShare_threading()
    print "Statu's Comment and share have got."
    b = datetime.datetime.now()
    print b
    print "This get new page process has completed!It spared time:  ", b-a
    sleep(2)
