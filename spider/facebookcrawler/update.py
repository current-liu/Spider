#!/usr/bin/env python
# -*- coding: utf-8 -*-
#此程序的作用是进行更新目标用户，保持程序运行即可，每12个小时会自动更新一次
import facebook
import requests
import pymysql
import datetime
import threading
from time import sleep
from DBUtils.PooledDB import PooledDB
dbpool = PooledDB(creator=pymysql, mincached=10, maxcached=10, maxshared=20, maxconnections=50, host='202.110.49.146', user='root', passwd='keystone',db='dpark',port=3381,charset='utf8mb4' )

graph = facebook.GraphAPI(access_token='312819675783598|Vb6UKYBHG0bhlCL2EbyoBViACSE', version='2.7')

sql1 = "replace into facebook_likes(statusID,likesID,likesName)values (%s,%s,%s)"
sql2 = '''REPLACE INTO facebook_comments(commentID,message,createdTime,fromID,fromName,statusID,comment_count,like_count,mark)VALUES (%s,%s,%s,%s,%s,%s,0,0,0)'''
sql3 = "REPLACE INTO facebook_comments(statusID,commentID,createdTime,fromID,fromName,message,comment_count,like_count,mark)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,1)"

def get_allPage():
    conn = dbpool.connection()
    cur = conn.cursor()
    sqlGet = "select * from fb_pageprofile"
    cur.execute(sqlGet)
    ID = cur.fetchall()
    conn.close()
    return ID
def get_allStatus():
    conn = dbpool.connection()
    cur = conn.cursor()
    sqlGet = "select * from facebook_status WHERE mark = 0"
    cur.execute(sqlGet)
    ID = cur.fetchall()
    conn.close()
    return ID
def get_allComments(updateTime):
    conn = dbpool.connection()
    cur = conn.cursor()
    sqlGet = "select * from facebook_comments WHERE mark = 0 AND createdTime > '%s'" % (updateTime)
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
def get_post_list(fb_page_id, createdName, updateTime):  #获取一个用户在24小时内发送的帖子
    conn = dbpool.connection()
    cur = conn.cursor()
    s = get_fb_page_post(fb_page_id)
    breakPoint = 1
    while (True):  # 获取用户发送的全部的status\
        if breakPoint == 2:
            break
        try:
            for item in s['data']:
                try:
                    a = item['id']
                    b = trans_date(item['created_time'])
                    time = b
                    c = createdName
                    d = item['message']
                    if time < updateTime:
                        breakPoint = 2
                        break
                    sql = '''replace INTO facebook_status(statusID,createdTime,createdName,message,reactions_count,comments_count,shares_count,mark)VALUES (%s,%s,%s,%s,0,0,0,0)'''
                    param = (a, b, c, d)
                    cur.execute(sql, param)
                    conn.commit()
                except Exception as e:
                    print e
                    continue
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
def getReactions(statusID):
    conn = dbpool.connection()
    cur = conn.cursor()
    indexLike = 0
    reactions = graph.get_object(id=statusID, fields='reactions.limit(100)')
    index1 = 0
    while True:
        try:
            many = []
            if index1 == 0:
                for user in reactions['reactions']['data']:
                    indexLike += 1
                    many.append([statusID, user['id'], user['name']])
                cur.executemany(sql1, many)
                conn.commit()
                reactions = requests.get(reactions['reactions']['paging']['next']).json()
            else:
                for user in reactions['data']:
                    indexLike += 1
                    many.append([statusID, user['id'], user['name']])
                cur.executemany(sql1, many)
                conn.commit()
                reactions = requests.get(reactions['paging']['next']).json()
        except KeyError:
            break
        print index1
        index1 += 1
    print "The status likes has been read!"
    print indexLike
    sql = "update facebook_status set reactions_count = '%s',mark = 4 WHERE statusID = '%s'" % (indexLike, statusID)
    cur.execute(sql)
    conn.commit()
    conn.close()

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

def get_List_10(num, somelist):
    return somelist[num*10:(num+1)*10]

def post_threading(updateTime):
    index = 0
    users = get_allPage()
    while True:
        threads = []
        loops = get_List_10(index, users)
        if not loops:
            break
        length = range(len(loops))
        for i in length:
            a = loops[i][0]
            t = threading.Thread(target=get_post_list, args=(loops[i][0], loops[i][1], updateTime))
            threads.append(t)
        for i in length:
            threads[i].start()
        for i in length:
            threads[i].join()
        index += 1
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
def comment_CommentLike_threading(someList):
    index = 0
    print index
    while True:
        threads = []
        loops = get_List_10(index, someList)
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
def status_reactions_threading(statusID):
    index = 0
    print index
    while True:
        threads = []
        loops = get_List_10(index, statusID)
        if not loops:
            break
        length = range(len(loops))
        for i in length:
            t = threading.Thread(target=getReactions, args=(loops[i][0],))
            threads.append(t)
        for i in length:
            threads[i].start()
        for i in length:
            threads[i].join()
        index += 1
if __name__ == "__main__":
    while True:
        a = datetime.datetime.now()
        updateTime = str(datetime.datetime.now() - datetime.timedelta(hours=24))
        post_threading(updateTime)
        print "Status get has Done.Now begin to get the comment and share!!!"
        print"Begin to get the status comments and shares!!"
        sleep(2)
        status = get_allStatus()
        commentShare_threading()
        print "Statu's Comment and share have got."
        print"Begin to get the comments comments and likes!!"
        sleep(2)
        index = 1
        while True:
            comments = get_allComments(updateTime)
            if not comments:
                break
            comment_CommentLike_threading(comments)
            print "The ", index, " loop has done!"
            index += 1
        print "comment's comment and like have got."
        print"Begin to get the status likes!!"
        sleep(2)
        status_reactions_threading(status)
        print "Status likes has got!"
        b = datetime.datetime.now()
        print b
        print "This update has completed!It spared time:  ", b-a
        sleep(43200)
