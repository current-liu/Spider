# -*-coding:utf-8 -*-
import re
import urlparse

import pymysql
from bs4 import BeautifulSoup

from mimi import html_downloader
from mimi.html_downloader import HtmlDownloader


class SpiderMain(object):
    def __init__(self):

        self.downloader=html_downloader.HtmlDownloader()

#获取一个主题的所有页的URL
    def craw1(self,root_url):
        html= self.downloader.download(root_url)
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        pid = soup.find('a',{'class': 'nxt'})
        return pid
#获取每一页中帖子名称中包含敏感词汇的帖子的URL
    def craw2(self,url):
        html = self.downloader.download(url)
        soup = BeautifulSoup(html, "lxml")
        result=soup.find_all('a', class_='xst', text=re.compile(u"\u6c11\u4e3b|\u9009\u4e3e|\u5171\u4ea7\u515a|\u6cdb\u6c11\u6d3e|\u5efa\u5236\u6d3e|\u8fbe\u8d56|\u7acb\u6cd5\u4f1a|\u7ade\u9009"))
        return result

#获取帖子的内容、作者、发布时间等信息
    def craw (self,url):
        ids=[]
        names=[]
        html = self.downloader.download(url)
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        message = soup.findAll('td', class_="t_f")
        # message = soup.findAll('div', align='left')
        pid= soup.findAll('div','em',class_="authi")
        for i in pid:
            c = i.em
            b=i.a
            ids.append(c)
            names.append(b)
        user_id=ids[1]['id']
        if ids[1].span:
            time=ids[1].span['title']
        else:
            time = ids[1].text
        name=names[0].text
        return message,user_id,time,name

def trans_datetime(a):
    b = a.replace("發表於 ", "")
    return b

def trans_id(a):
    b = a.replace("&", "")
    return b


if __name__=="__main__":
    #db = pymysql.connect(host="202.110.49.146", user="root", passwd="Sz@860213", db="hkstar", charset="utf8")
	db = pymysql.connect(host="192.168.1.20", user="root", passwd="root", db="hkstar", charset="utf8")

    cursor = db.cursor()
    cursor.execute('SET NAMES utf8mb4')
    cursor.execute('set GLOBAL max_allowed_packet=67108864')
    root_url=['http://forum.memehk.com/forum.php?mod=forumdisplay&fid=106','http://forum.memehk.com/forum.php?mod=forumdisplay&fid=60','http://forum.memehk.com/forum.php?mod=forumdisplay&fid=61','http://forum.memehk.com/forum.php?mod=forumdisplay&fid=62','http://forum.memehk.com/forum.php?mod=forumdisplay&fid=64','http://forum.memehk.com/forum.php?mod=forumdisplay&fid=65','http://forum.memehk.com/forum.php?mod=forumdisplay&fid=108']
    sql= """INSERT IGNORE INTO meme_message(message_id,message,created_at,user_id,name) VALUES (%s,%s,%s,%s,%s)"""
    for url_a in root_url:
        url_original = []
        result_url = []
        url_original.append(url_a)
        obj_spider = SpiderMain()
        count = 200
        while count:
            pid = obj_spider.craw1(url_original[-1])
            print pid
            # print url_original[-1]
            if pid==None:
                break
            else:
                a = pid.get('href')
                url = 'http://forum.memehk.com/'
                b = urlparse.urljoin(url, a)
                url_original.append(b)
                count -= 1
        for link in url_original:
            result = obj_spider.craw2(link)
            for i in result:
                c = i.get('href')
                url = 'http://forum.memehk.com/'
                d = urlparse.urljoin(url, c)
                result_url.append(d)
                message, user_id, time, name = obj_spider.craw(d)
                meg = ''
                for i in message:
                    meg = meg + i.get_text()
                if len(time)>19:
                    time = time[4:]

                message_id=d[53:59]
                a=trans_id(message_id)
                print d
                # print meg

                print time
                # print time1

                # print user_id
                # print name
                if meg:
                    cursor.execute(sql, (a, meg, time, user_id, name))
                    db.commit()




