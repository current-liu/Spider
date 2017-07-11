#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import urllib2
import urlparse
import time

import pymysql

from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
f=open('meme.txt', 'r')
#db = pymysql.connect(host="202.110.49.146", user="root", passwd="Sz@860213", db="hkstar", charset="utf8")
db = pymysql.connect(host="192.168.1.20", user="root", passwd="root", db="hkstar", charset="utf8")
cursor = db.cursor()
def download(url):
    print 'Downloading:',url
    try:
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}

        request = urllib2.Request(url, headers=headers)
        html = urllib2.urlopen(request).read()
        # print html
    except urllib2.URLError as e:
        print 'Download error:',e.reason
        html = None
    return html


def craw(url):
    html = download(url)
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    message = soup.findAll('td', class_="t_f")

    pid = soup.findAll('div', 'em', class_="authi")
    return  message,pid
def trans_datetime(a):
    b = a.replace("發表於 ", "")
    return b

def trans_id(a):
    b = a.replace("&", "")
    return b

while 1:
    count=10
    comment_url = []
    url = f.readline()
    comment_url.append(url)
    # 获取每一篇文章的所有评论页的url
    while count:
        html = download(comment_url[-1])
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        pid = soup.find('a', {'class': 'nxt'})
        if pid:
            a = pid.get('href')
            url = 'http://forum.memehk.com/'
            b = urlparse.urljoin(url, a)
            comment_url.append(b)
            count -= 1
        else:
            break
    print comment_url

    #获取每一个评论页中的评论信息并插入到数据库中
    for url1 in comment_url:
        comment=[]
        ids=[]
        names=[]
        message,pid= craw(url1)
        print len(message)
        print len(pid)
        for i in message:
            print i
            print i.text
            comment.append(i.text)
        for i in pid:
            c = i.em
            b = i.a
            ids.append(c)
            names.append(b)
        names.pop(0)
        comment.pop(0)
        print ids
        print names

#写数据库
    sql = 'Insert ignore into meme_comment (message_id,comment_id,comment,created_at,from_id,from_name) VALUES (%s,%s,%s,%s,%s,%s)'
    k = 0
    while k < len(comment):
        d = 2 * k + 1
        text = comment[k]
        user_id = ids[d+2]['id']
        if ids[d+2].span:
            time = ids[d + 2].span['title']
        else:
            time = ids[d + 2].text
        time = trans_datetime(time)
        print time
        name = names[d].text
        comment_ids=trans_id(url1[49:59])
        comment_id = comment_ids + '_' + str(k)
        print comment_id
        if(text):
            cursor.execute(sql, (comment_ids,comment_id, text, time, user_id,name))
            db.commit()
        k += 1
