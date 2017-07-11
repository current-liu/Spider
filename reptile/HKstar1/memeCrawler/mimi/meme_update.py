# -*-coding:utf-8 -*-
import re
import time
import urlparse
import urllib2
import pymysql
from bs4 import BeautifulSoup

# from mimi import html_downloader
# from mimi.html_downloader import HtmlDownloader


# class SpiderMain(object):
#     def __init__(self):
#
#         self.downloader=html_downloader.HtmlDownloader()
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
        time.sleep(1)
    return html
#获取一个主题的所有页的URL
def craw1(root_url):
    html= download(root_url)
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    pid = soup.find('a',{'class': 'nxt'})
    return pid
#获取每一页中帖子名称中包含敏感词汇的帖子的URL
def craw2(url):
    html = download(url)
    # soup = BeautifulSoup(html, "lxml")
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    result = soup.find_all('a', class_='xst', text=re.compile(
        u"\u6c11\u4e3b|\u9009\u4e3e|\u5171\u4ea7\u515a|\u6cdb\u6c11\u6d3e|\u5efa\u5236\u6d3e|\u8fbe\u8d56|\u7acb\u6cd5\u4f1a|\u7ade\u9009"))
    return result

#获取帖子的内容、作者、发布时间等信息
def craw (url):
    ids = []
    names = []
    html = download(url)
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    message = soup.findAll('td', class_="t_f")
    # message = soup.findAll('div', align='left')
    pid = soup.findAll('div', 'em', class_="authi")
    for i in pid:
        c = i.em
        b = i.a
        ids.append(c)
        names.append(b)
    user_id = ids[1]['id']
    if ids[1].span:
        time = ids[1].span['title']
    else:
        time = ids[1].text
    name = names[0].text
    return message, user_id, time, name


def craw4(url):
    html = download(url)
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    message = soup.findAll('td', class_="t_f")
    pid = soup.findAll('div', 'em', class_="authi")
    return message, pid

def trans_datetime(a):
    b = a.replace("發表於 ", "")
    return b


def trans_id(a):
    b = a.replace("&", "")
    return b


while 1:
    comments_url = []
    #db = pymysql.connect(host="202.110.49.146", user="root",port=3306, passwd="Sz@860213", db="hkstar", charset="utf8")
    db = pymysql.connect(host="192.168.1.20", user="root",port=3306, passwd="root", db="hkstar", charset="utf8")
    cursor = db.cursor()
    cursor.execute('SET NAMES utf8mb4')
    cursor.execute('set GLOBAL max_allowed_packet=67108864')
    root_url = ['http://forum.memehk.com/forum.php?mod=forumdisplay&fid=106',
                'http://forum.memehk.com/forum.php?mod=forumdisplay&fid=60',
                'http://forum.memehk.com/forum.php?mod=forumdisplay&fid=61',
                'http://forum.memehk.com/forum.php?mod=forumdisplay&fid=62',
                'http://forum.memehk.com/forum.php?mod=forumdisplay&fid=64',
                'http://forum.memehk.com/forum.php?mod=forumdisplay&fid=65',
                'http://forum.memehk.com/forum.php?mod=forumdisplay&fid=108']
    sql = """INSERT IGNORE INTO meme_message(message_id,message,created_at,user_id,name) VALUES (%s,%s,%s,%s,%s)"""
    for url_a in root_url:
        result = craw2(url_a)
        for i in result:
            c = i.get('href')
            url = 'http://forum.memehk.com/'
            d = urlparse.urljoin(url, c)
            message, user_id, time2, name = craw(d)
            meg = ''
            for i in message:
                meg = meg + i.get_text()
            if len(time2) > 19:
                time2 = time2[4:]
            message_ids = d[53:59]
            message_id = trans_id(message_ids)
            # print d
            # print meg
            # print time
            # print user_id
            # print name
            if meg:
                cursor.execute(sql, (message_id, meg, time2, user_id, name))
                db.commit()
                comments_url.append(d)

    for comments in comments_url:
        comment_url = []

        comment_url.append(comments)
        # 获取每一篇文章的所有评论页的url
        while 1:
            pid = craw1(comments)
            if pid:
                a = pid.get('href')
                url = 'http://forum.memehk.com/'
                b = urlparse.urljoin(url, a)
                comment_url.append(b)
            else:
                break
        # print comment_url

        # 获取每一个评论页中的评论信息并插入到数据库中
        for url1 in comment_url:
            comment = []
            ids = []
            names = []
            message, pid = craw4(url1)
            # print len(message)
            # print len(pid)
            for i in message:
                # print i
                # print i.text
                comment.append(i.text)
            for i in pid:
                c = i.em
                b = i.a
                ids.append(c)
                names.append(b)
            names.pop(0)
            comment.pop(0)

            # 写数据库
        sql1 = 'Insert ignore into meme_comment (message_id,comment,created_at,from_id,from_name) VALUES (%s,%s,%s,%s,%s)'
        k = 0
        while k < len(comment):
            d = 2 * k + 1
            text = comment[k]
            user_id = ids[d + 2]['id']
            if ids[d + 2].span:
                time = ids[d + 2].span['title']
            else:
                time = ids[d + 2].text
            if len(time) > 19:
                time = time[4:]

            print time
            name = names[d].text
            comment_ids = trans_id(url1[53:59])
            comment_id = comment_ids + '_' + str(k)
            print comment_id
            if (text):
                cursor.execute(sql, (comment_id, text, time, user_id, name))
                db.commit()
            k += 1
    print 1








