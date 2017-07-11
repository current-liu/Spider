# -*- coding:utf-8 -*-

import json
from bs4 import BeautifulSoup
import bs4
import re
from datetime import datetime


class Parser(object):
    def __init__(self):
        self.url_str = r'http://weare.hk/bbs/'
        self.subject = {'titleId': '', 'title': '', 'author': '', 'publishTime': ''}
        self.keywords = ['民主', '選舉', '共産黨', '泛民派', '建制派', '達賴', '立法', '會竞选', '日本']

    # 解析站点json字符串
    def title_parse(self, response_page, now, tenago):
        title_list = []
        if response_page == None:
            return None, False
        # 输出测试代码
        print("response_page:")
        print(response_page.decode('big5'))
        bs = BeautifulSoup(response_page, 'html.parser', from_encoding='big5')
        tbodys = bs.find_all('tbody', id=re.compile(r'normalthread_'))
        for tbody in tbodys:
            # <a href="redirect.php?tid=437968&amp;goto=lastpost#lastpost">
            # <span title="2016-12-18 19:22">6&nbsp;天前&nbsp;19:22</span></a>
            lastTimeNode = tbody.find('td', class_='lastpost').find('span')
            if lastTimeNode != None:
                lastTimeStr = lastTimeNode['title']
            else:
                # <a href="redirect.php?tid=437931&amp;goto=lastpost#lastpost">2016-12-6 16:32</a>
                lastTimeStr = tbody.find('td', class_='lastpost').find('em').get_text()
            formatTime = self.transTitleTime(lastTimeStr)
            print('formatTime:' + formatTime)
            lastTime = datetime.strptime(formatTime, "%Y-%m-%d %H:%M:%S")
            if lastTime <= now and lastTime > tenago:
                title_url = self.url_str + tbody.find('a', href=re.compile(r'^viewthread.php'))['href']
                print(title_url)
                title_list.append(title_url)
            else:
                return title_list, False
        # 把json字符串里面的stations的值取出来返回一个list
        return title_list, True

    def transTitleTime(self, timeStr):
        timeArr = timeStr.split()
        mydate = timeArr[0].split("-")
        if len(mydate[1]) == 1:
            mydate[1] = '0' + mydate[1]
        if len(mydate[2]) == 1:
            mydate[2] = '0' + mydate[2]
        lastTime = mydate[0] + '-' + mydate[1] + '-' + mydate[2] + ' ' + timeArr[1] + ':00'
        print(lastTime)
        return lastTime

    # 解析实时数据
    def reply_parse(self, response_reply, page, now, tenago):
        print(response_reply)
        next_page = self._reply_parse(response_reply)
        data_list = []
        bs = BeautifulSoup(response_reply, 'html.parser', from_encoding='big5')
        post_nodes = bs.find_all('div', id=re.compile(r'post_\d+'))
        for post_node in post_nodes:
            keys = ''
            # post_73645181
            replyId = re.sub(r'\D', '', post_node['id'])

            #  href="space.php?uid=2106869" style="margin-left: 20px; font-weight: 800">california2</a>
            author_info = post_node.find('td', class_='postauthor').find('div', class_='postinfo').find('a')
            replierIdLink = author_info['href']
            replierId = re.sub(r'\D', '', replierIdLink)
            replyName = author_info.get_text()

            postBody = post_node.find('td', class_='postcontent')
            time_floor = postBody.find('div', class_='postinfo')
            # 1#
            floor = time_floor.find('a').get_text()[0]
            print("floor:" + floor)
            # <span title="2016-12-20 15:59">昨天&nbsp;15:59</span>
            time_node = time_floor.find('div', class_='authorinfo').find('span')
            if time_node != None:
                lastTimeStr = time_node['title']
            else:
                # <em id="authorposton73645181">發表於 2016-11-25 23:50</em>
                lastTimeStr = time_floor.find('div', class_='authorinfo').find('em').get_text()
            time1 = re.search(r'\d\d\d\d-\d+-\d+ \d\d:\d\d', lastTimeStr).group()
            formatTime = self.transTitleTime(time1)
            lastTime = datetime.strptime(formatTime, "%Y-%m-%d %H:%M:%S")
            if lastTime <= now and lastTime > tenago:
                postContent = postBody.find('td', id='postmessage_' + replyId).get_text()
                for keyword in self.keywords:
                    if keyword in postContent:
                        keys = keys + ',' + keyword
                if keys != '':
                    post = (replyId, postContent.encode('big5', 'ignore').decode('big5', 'ignore'), replierId,
                            replyName, formatTime, keys.encode('big5', 'ignore').decode('big5', 'ignore'), floor,
                            self.subject['titleId'])
                    data_list.append(post)
            # 借用一楼信息,floor是一个字符串
            if floor == '1':
                self.subject['author'] = replyName
                self.subject['publishTime'] = formatTime

        # 返回结果集
        return data_list, next_page

    def _reply_parse(self, response_reply):
        bs = BeautifulSoup(response_reply, 'html.parser', from_encoding='big5')
        # 找出下一页的数字
        # href="viewthread.php?tid=437776&extra=page%3D1&page=2"
        next_node = bs.find('a', class_='next')
        if next_node != None:
            next_page_num = next_node['href'][-1]
        else:
            next_page_num = -1
        # 因为如果查找pages这个div的话，有可能没有下一页，所以只看该作者这个肯定有
        href = 'tid=000000'
        maxTryNum = 10
        for i in range(maxTryNum):
            href_node = bs.find('a', rel='nofollow', string='只看該作者')
            if href_node != None:
                href = href_node['href']
                break
        tid = re.search(r'tid=\d+', href).group()[4:]
        # title = bs.find('div',class_='postmessage firstpost').get_text()
        title_str = bs.find('div', id='nav').get_text()
        title = title_str.split()
        self.subject['titleId'] = tid
        self.subject['title'] = title[-1].encode('big5', 'ignore').decode('big5', 'ignore')
        return next_page_num

    def istitle(self):
        for keyword in self.keywords:
            if keyword in self.subject['title']:
                return True
