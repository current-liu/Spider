#!/usr/bin/env python
# coding=utf-8
"""
Created on 2017/10/17 20:28

base Info
"""
import os
import sys
import scrapy
from scrapy import Selector
from demo.items import *

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
rootPath1 = os.path.split(rootPath)[0]

# 要添加 'D:\LiuChao\PycharmProjects\Scrapy\demo'
sys.path.append(rootPath1)
sys.path.append(rootPath)
a = sys.path

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'liuchao'
__version__ = '1.0'


class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = ["http://www.cnblogs.com/qiyeboy/default.html?page=1"]

    def parse(self, response):
        papers = response.xpath(".//*[@class='day']")
        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]

            print url, title, time, content
            item = DemoItem(url=url, title=title, time=time, content=content)
            yield item
        next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)

