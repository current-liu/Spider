#!/usr/bin/env python
# -*- coding: utf-8 -*-
#此程序是获取状态的点赞数量
import facebook
import requests
import pymysql
import threading
from DBUtils.PooledDB import PooledDB
#graph = facebook.GraphAPI(access_token='1798673940392223|16crjBJNqFyNgCOo0BPpY4dgFqw', version='2.7')
graph = facebook.GraphAPI(access_token='1537948926257443|kfpadyau2sHmH_u25oj7oZYwX50', version='2.7')
dbpool = PooledDB(creator=pymysql, mincached=10, maxcached=10, maxshared=20, maxconnections=50, host='202.110.49.146', user='root', passwd='keystone',db='dpark',port=3381,charset='utf8mb4' )
sql1 = "replace into facebook_likes(statusID,likesID,likesName)values (%s,%s,%s)"

def get_allStatus():
    conn = dbpool.connection()
    cur = conn.cursor()
    sqlGet = "select * from facebook_status WHERE mark = 3 ORDER BY createdTime DESC"
    cur.execute(sqlGet)
    ID = cur.fetchall()
    conn.close()
    return ID
def getReactions(statusID):
    conn = dbpool.connection()
    cur = conn.cursor()
    indexLike = 0
    reactions = graph.get_object(id=statusID, fields='reactions.llimit(200)')
    index1 = 0#页码信息
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
def get_List_10(num, somelist):
    return somelist[num*10:(num+1)*10]
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
    print "Now start to get Likes!"
    statusID = get_allStatus()
    status_reactions_threading(statusID)

