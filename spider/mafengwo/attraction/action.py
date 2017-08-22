#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/10 0010 下午 3:01

base Info
"""
import os
import random
import time
import datetime
import urlparse
import re
from pandas import json
from mafengwo import html_download
import h_parser
import dao
from mafengwo import base_dao

__author__ = 'Administrator'
__version__ = '1.0'
today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")
today_fo = today.strftime("%Y%m%d")
filename = today_fo + ".txt"
fo_log = open("./log/" + filename, "a")


def get_attraction_list():
    url_pre = "http://www.mafengwo.cn/ajax/router.php?cb=jQuery18109768219088779657_1503019977250&sAct=KMdd_StructWebAjax|GetPoisByTag&iMddid=10189&iTagId=0&iPage="
    flag = True
    index = 0
    while (flag):
        index += 1
        if index == 32:
            flag = False

        url = url_pre + str(index)
        doc, msg = html_download.downloadPage_without_proxy(url, fo_log)
        if msg != "ok":
            continue
        else:
            attractions, msg = h_parser.parser_attraction_list(doc)

        if msg != "ok":
            msg1 = "get attraction from page %d is fail" % index
            print msg1
        else:
            dao.insert_attraction_shop(attractions)


def get_attraction_shop():
    table = "attraction_shop"
    shops = base_dao.select_shopid(table, "WHERE shopName Is Null ")
    fo_log.flush()
    for shop in shops:
        shop_id = shop[0]
        # shop_id = 520
        msg1 = "第'%d':'%s'" % (shops.index(shop), shop_id)
        print msg1
        fo_log.write(msg1)

        url = "http://www.mafengwo.cn/poi/" + str(shop_id) + ".html"
        doc, msg = html_download.downloadPage(url, fo_log)

        if msg != "ok":
            continue

        try:
            shop_name, shop_name_en, info, tel, site, time_use, trans, ticket, bussiness_time, loc, inner_scenic, review_num = h_parser.parser_attraction_shops(
                doc)
            msg2 = "shopId:'%s'解析完成，正写入数据" % shop_id
            print msg2
            dao.update_attraction_shop(shop_name, shop_name_en, info, tel, site, time_use, trans, ticket,
                                       bussiness_time, loc, inner_scenic, review_num, shop_id)
        except:
            # TODO 这里会接到异常吗？ 两个函数的异常都在内部处理过了
            fo_log.write("doc error '%s'" % shop_id)
            fo_log.write(doc)


def get_attraction_review():
    table = "attraction_shop"
    shops = base_dao.select_shopid_and_reviewnum(table)
    for shop in shops:
        shop_id = shop[0]
        review_num = shop[1]
        page_num = (review_num + 15 - 1) / 15
        msg1 = "num.%d %s : totally %d pages review" % (shops.index(shop), shop_id, page_num)
        print msg1
        fo_log.write(msg1)
        if review_num < 1:
            continue
        get_attraction_review_on_page(shop_id, page_num)
    pass


def get_attraction_review_on_page(shop_id, page_num):
    index = 0
    if shop_id == 520:
        index = 293
    flag = True
    while (flag):
        index += 1
        url = 'http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18107355407450384277_1503280700250&params=%7B%22poi_id%22%3A%22' + str(
            shop_id) + '%22%2C%22page%22%3A' + str(index) + '%2C%22just_comment%22%3A1%7D&_=1503281566568'

        if index == page_num:
            flag = False
        time.sleep(random.uniform(2, 3))
        doc, msg = html_download.downloadPage_without_proxy(url, fo_log)
        if msg != "ok":
            continue
        try:
            review_ids, member_ids, likes, contents, stars, times = h_parser.parser_attraction_review(doc)
            msg = dao.insert_attraction_review(shop_id, review_ids, member_ids, likes, contents, stars, times)
            if msg == "for key 'PRIMARY'":
                msg2 = "shopId %s reach the page scrawled" % shop_id
                print msg2
                fo_log.write(msg2)
                break

        except BaseException, e:
            print e
    msg3 = "shopId %s log to pageno=%s" % (shop_id, index)
    print msg3
    fo_log.write(msg3)
