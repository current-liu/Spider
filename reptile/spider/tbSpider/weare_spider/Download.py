# -*- coding:utf-8 -*-

import socket
import urllib
import logging
import random
from urllib import request
from http import cookiejar
from weare_spider import Parser, Output


class Download(object):
    def __init__(self, logger):
        self.parser = Parser.Parser()
        self.output = Output.Output()
        self.logger = logger
        self.title_str = r'http://weare.hk/bbs/forumdisplay.php?fid=13&page='
        self.reply_url = "http://weare.hk/bbs/viewthread.php?tid=437776&amp;extra=page%3D1&page="
        # 用来存储cookie
        self.cookie = cookiejar.CookieJar()
        # 用来管理cookie
        self.handle = request.HTTPCookieProcessor(self.cookie)
        self.opener = request.build_opener(self.handle)

    # 下载动态的title页面，服务器响应值为json类型的数据，里面存放站点信息
    def title_download(self, page):
        req_header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # Accept-Encoding:'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Cookie': '5AL_cookietime=2592000; smile=1D1; 5AL_visitedfid=13; __atuvc=29%7C50%2C16%7C51; '
                      '5AL_sid=HFz9yk;__utmt=1; __utma=185387823.472381668.1481597518.1482126353.1482243066.17; '
                      '__utmb=185387823.2.10.1482243066; __utmc=185387823; '
                      '__utmz=185387823.1481597518.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            'Host': 'weare.hk',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'
        }
        req_header1 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # Accept-Encoding:'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep - alive',
            'Cookie': 'bdshare_firstime=1476951279863; uuid_tt_dd=-3267531199103678933_20161020; UN=Fantasy_Virgo; UE="1002297618@qq.com"; BT=1479559135791; __message_district_code=000000; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0; uuid=8feaf5b8-1a15-43c6-b7da-9d71896ef813; avh=42784275; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1482138296,1482208071,1482208090,1482222101; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1482244927; dc_tos=oihni7; dc_session_id=1482244927866',
            'Host': 'blog.csdn.net',
            'If-None-Match': 'W / "1b61fc9100eb68a00cbf15bd798b3cf4"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
        }
        # r'http://blog.csdn.net/dc_726/article/details/42784275'
        title_url = self.title_str + str(page)
        maxTryNum = 10
        # proxy_support = request.ProxyHandler({'http': '172.19.12.26:80'})
        # proxy=request.build_opener(proxy_support)
        # request.install_opener(proxy)
        for tries in range(maxTryNum):
            try:
                print(title_url)
                req = request.Request(title_url, headers=req_header)
                response = self.opener.open(req, timeout=5)
                # response = request.urlopen(req, timeout=1)
                # return response.read()
                read_content = response.read()
                fopen = open("page.html", "wb")
                fopen.write(read_content)
                return read_content
            except request.URLError as e:
                if tries < (maxTryNum - 1):
                    continue
                if hasattr(e, "code"):
                    print("获取 " + str(page) + " 页时发生request.HTTPError异常," + "错误code: " + str(e.code()))
                    self.logger.error("获取 " + str(page) + " 页时发生request.HTTPError异常," + "错误code: " + str(e.code()))
                if hasattr(e, "reason"):
                    print(e)
                    print("获取 " + str(page) + " 页时发生request.URLError异常")
                    self.logger.error("获取 " + str(page) + " 页时发生request.URLError异常")
            except socket.timeout as e:
                if tries < (maxTryNum - 1):
                    continue
                print("获取 " + str(page) + " 页时发生socket.timeout异常")
                self.logger.error("获取 " + str(page) + " 页时发生socket.timeout异常")
            except socket.error as e:
                if tries < (maxTryNum - 1):
                    continue
                print(e)
                print("获取 " + str(page) + " 页时发生socket.error异常")
                self.logger.error("获取 " + str(page) + " 页时发生socket.error异常")
                self.logger.error(e)
            except Exception as e:
                if tries < (maxTryNum - 1):
                    continue
                print(e)
                print("获取 " + str(page) + " 页时发生其他异常")
                self.logger.error("获取 " + str(page) + " 页时发生其他异常")
                self.logger.error(e)
        return None

    # 下载实时数据页面，服务器响应值为整个页面
    def reply_download(self, title_url, now, tenago):
        data_list = []
        page = 1
        while page != -1:
            # 完整的url
            reply_url = title_url + '&page=' + str(page)
            print(reply_url)
            # 获取第x页的回复内容
            response_reply = self._reply_download(reply_url)
            # 解析第X页的回复内容
            page_list, page = self.parser.reply_parse(response_reply, page, now, tenago)
            if len(page_list) > 0:
                data_list.extend(page_list)

        # 如果结果集不为空肯定要插入主题和回复内容
        if len(data_list) > 0:
            if self.output.title_is_exist(self.parser.subject['titleId']) == False:
                self.output.insertTitle(self.parser.subject)
            self.output.insertReply(data_list)
        # 如果title存在关键字并且结果集为空并且该title不存在于数据库中
        if self.parser.istitle() == True:
            if self.output.title_is_exist(self.parser.subject['titleId']) == False:
                self.output.insertTitle(self.parser.subject)

    def _reply_download(self, title_url):
        req_header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            # 'Accept-Encoding':'gzip, deflate, sdch',
            'Host': 'weare.hk',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://weare.hk/bbs/forumdisplay.php?fid=13',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/50.0.2661.102 Safari/537.36'
        }
        maxTryNum = 10
        for tries in range(maxTryNum):
            try:
                req = request.Request(title_url, headers=req_header)
                response = self.opener.open(req, timeout=5)
                print(response.getcode())
                # return response.read()
                reply_content = response.read()
                fopen = open("1.html", "wb")
                fopen.write(reply_content)
                return reply_content
            except request.URLError as e:
                if tries < (maxTryNum - 1):
                    continue
                if hasattr(e, "code"):
                    print("获取 " + title_url + " 时发生request.HTTPError异常," + "错误code: " + str(e.code()))
                    self.logger.error("获取 " + title_url + " 时发生request.HTTPError异常," + "错误code: " + str(e.code()))
                if hasattr(e, "reason"):
                    print("获取 " + title_url + " 时发生request.URLError异常")
                    self.logger.error("获取 " + title_url + " 时发生request.URLError异常")
            except socket.timeout as e:
                if tries < (maxTryNum - 1):
                    continue
                print("获取 " + title_url + " 时发生socket.timeout异常")
                self.logger.error("获取 " + title_url + " 时发生socket.timeout异常")
            except socket.error as e:
                if tries < (maxTryNum - 1):
                    continue
                print(e)
                print("获取 " + title_url + " 时发生socket.error异常")
                self.logger.error("获取 " + title_url + " 时发生socket.error异常")
                self.logger.error(e)
            except Exception as e:
                if tries < (maxTryNum - 1):
                    continue
                print(e)
                print("获取 " + title_url + " 页时发生其他异常")
                self.logger.error("获取 " + title_url + " 页时发生其他异常")
                self.logger.error(e)
        return None
