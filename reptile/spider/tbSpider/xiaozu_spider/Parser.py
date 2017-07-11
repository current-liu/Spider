# -*- coding:utf-8 -*-

import json
from bs4 import BeautifulSoup
import bs4
import re
from datetime import datetime


class Parser(object):
    def __init__(self):
        self.url_str = r'http://lsforum.net/board/'
        self.subject={'titleId':'','title':'','author':'','publishTime':''}
        self.keywords = ['民主','選舉','共産黨','泛民派','建制派','達賴','立法','會竞选','謝謝']

    # 解析站点json字符串
    def title_parse(self, response_page, now, tenago):
        title_list = []
        # 如果是最后一页的话为空，标志着结束
        if response_page == None:
            return None,False
        # 输出测试代码
        print("response_page:")
        print(response_page)
        bs = BeautifulSoup(response_page, 'html.parser', from_encoding='big5')
        tbodys = bs.find_all('tbody', id=re.compile(r'normalthread_'))
        for tbody in tbodys:
            # str = r'2016-11-17 05:33 PM'  2016-11-4 05:55 PM  两种类型
            lastTimeStr = tbody.find('td', class_='lastpost').find('em').get_text()
            print('lastTimeStr:' + lastTimeStr)
            # (2016-11-4)   (05:55)   (PM)
            formatTime = self.transTitleTime(lastTimeStr)
            lastTime = datetime.strptime(formatTime, "%Y-%m-%d %H:%M:%S")
            if lastTime <= now and lastTime > tenago:
                # <a href="thread-269146-1-1.html">下周一冷氣團減弱</a>
                # <a href="viewthread.php?tid=269146&amp;extra=page%3D1&amp;sid=g2g3b2">下周一冷氣團減弱</a></span>

                print(type(tbody))
                for child in tbody.descendants:
                    print(child)
                title_url = tbody.find('a', href=re.compile('viewthread.php'))['href']
                # title_url = tbody.find('a', href=re.compile('thread-269146-1-1.html'))
                # print(type(title_url))
                # print(title_url)
                title_list.append(title_url)
            else:
                # 因为是按照最后回复时间来排序的，所以当前的不符合时间限制的话，就可以返回了
                return title_list,False
        # 把json字符串里面的stations的值取出来返回一个list
        return title_list,True

    def transTitleTime(self,timeStr):
        timeArr = timeStr.split()
        mydate = timeArr[0].split("-")
        if len(mydate[1]) == 1:
            mydate[1] = '0' + mydate[1]
        if len(mydate[2]) == 1:
            mydate[2] = '0' + mydate[2]
        apm = timeArr[2]
        hour = timeArr[1][0:2]
        if apm == 'PM':
            hour = int(hour) + 12
        lastTime = mydate[0] + '-' + mydate[1] + '-' + mydate[2] + ' ' + str(hour) + timeArr[1][2:] + ':00'
        print(lastTime)
        return lastTime

    def reply_parse(self, response_reply,now,tenago,title_url):
        print(response_reply)
        next_url = self._reply_parse(response_reply,title_url)
        data_list = []
        bs = BeautifulSoup(response_reply, 'html.parser', from_encoding='big5')
        # <table id="pid2317718" summary="pid2317718" cellspacing="0" cellpadding="0">
        post_nodes = bs.find_all('table',id=re.compile(r'pid\d*'))
        for post_node in post_nodes:
            keys=''
            # pid2317718
            replyId = re.sub(r'\D',"",post_node['id'])
            #  <a href="space-uid-146959.html" target="_blank" id="userinfo2317718" class="dropmenu" onmouseover="showMenu(this.id)">kiutse</a>
            author_info = post_node.find('td',class_='postauthor').find('a',class_='dropmenu')
            replierIdLink = author_info['href']
            replierId = re.sub(r'\D',"",replierIdLink)
            replyName = author_info.get_text()

            postBody = post_node.find('td',class_='postcontent')
            time_floor = postBody.find('div',class_='postinfo')
            # 1#
            floor = time_floor.find('strong').get_text()[0]

            # 發表於 2016-2-19 02:25 PM&nbsp;(第 308 天
            # 發表於 2010-8-17 05:54 PM&nbsp;(第 2318 天)   时间简直不能再不规范，无语
            time = time_floor.get_text()
            time1 = (re.search(r"\d\d\d\d-\d+-\d+ \d\d:\d\d [A|P]M", time)).group()
            formatTime = self.transTitleTime(time1)
            lastTime = datetime.strptime(formatTime, "%Y-%m-%d %H:%M:%S")
            # 如果时间满足并且包含关键字的话就要插入
            if lastTime <= now and lastTime > tenago:
                postContent = postBody.find('div',id='postmessage_'+replyId).get_text()
                for keyword in self.keywords:
                    if keyword in postContent:
                        keys = keys + ',' + keyword
                if keys != '':
                    post = (replyId,postContent,replierId,replyName,formatTime,keys,floor,self.subject['titleId'])
                    data_list.append(post)
            # 借用一楼信息
            if floor == '1':
                self.subject['author'] = replyName
                self.subject['publishTime'] = formatTime

        # 返回结果集
        return data_list,next_url

    def _reply_parse(self, response_reply,title_url):
        bs = BeautifulSoup(response_reply, 'html.parser', from_encoding='big5')
        # 找出下一页的url
        # <a href="thread-149010-2-2.html" class="next">››</a>
        pages_node = bs.find('div', class_='pages')
        # 如果只有一页的话没有页码div，没有下一页或者没有页码div，nexe_url都为空
        if pages_node != None:
            next_node = pages_node.find('a', class_='next')
            if next_node != None:
                next_url = next_node['href']
            else:
                next_url = ''
        else:
            next_url = ''
        title = bs.find('div',class_='mainbox viewthread').find('h1').get_text()
        self.subject['title'] = title
        temp = re.search('tid=\d+',title_url).group()[4:]
        self.subject['titleId'] = temp
        return next_url

    def istitle(self):
        for keyword in self.keywords:
            if keyword in self.subject['title']:
                return True






