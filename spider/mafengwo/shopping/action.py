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


def get_shopping_list():
    area01 = ["尖沙咀", 170, 7]
    area02 = ["旺角/油麻地", 175, 5]
    area03 = ["湾仔及铜锣湾", 173, 5]
    area04 = ["太子/深水埗", 2343, 2]
    area05 = ["上环", 172, 2]
    area06 = ["中环/金钟", 1725, 3]
    area07 = ["迪士尼乐园", 176, 0]
    area08 = ["九龙城", 2347, 1]
    area09 = ["荃湾区", 8428, 1]
    area10 = ["香港仔/海洋公园", 2338, 1]
    area11 = ["赤鱲角机场", 174, 1]
    area12 = ["沙田", 12071, 1]
    area13 = ["南丫岛", 12086, 0]
    area14 = ["北角", 46183, 0]
    areas = [area01, area02, area03, area04, area05, area06, area07, area08, area09, area10, area11, area12, area13,
             area14]

    for area in areas:
        area_num = area[1]
        pages = area[2]
        if pages < 1:
            continue
        area_name = area[0]
        flag = True
        index = 0
        while (flag):
            index += 1
            if index == pages:
                flag = False
            url = "http://www.mafengwo.cn/gonglve/ajax.php?act=get_poi_list&mddid=10189&mdd_type=gw&tag_id=0&keyword=&page=" + str(
                index) + "&order=0&area_id=" + str(area_num) + "&is_ginfo=0&ts=1503388274049"

            time.sleep(random.uniform(2, 3))
            doc, msg = html_download.downloadPage_without_proxy(url, fo_log)
            if msg != "ok":
                continue
            else:
                shopping_shops = h_parser.parser_shopping_list(doc)
                dao.insert_shopping_shop(shopping_shops, area_name)


def get_shopping_shop():
    table = "shopping_shop"
    shops = base_dao.select_shopid(table, "WHERE shopName Is Null OR shopName = '-1'")
    fo_log.flush()
    for shop in shops:
        shop_id = shop[0]
        # shop_id = 5796607
        msg1 = "num. '%d':'%s'" % (shops.index(shop), shop_id)
        print msg1
        fo_log.write(msg1)
        url = "http://www.mafengwo.cn/poi/" + str(shop_id) + ".html"
        time.sleep(random.uniform(2, 3))
        doc, msg = html_download.downloadPage_without_proxy(url, fo_log)

        if msg != "ok":
            continue

        try:
            shop_name, shop_name_en, score, star, review_num, tip, site, tel, intro, trans, loc = h_parser.parser_shopping_shops(
                doc)
            msg2 = "shopId:'%s' parser complete，inserting into database" % shop_id
            print msg2
            dao.update_shopping_shop(shop_name, shop_name_en, score, star, review_num, tip, site, tel, intro, trans,
                                     loc, shop_id)
        except:
            # TODO 这里会接到异常吗？ 两个函数的异常都在内部处理过了
            fo_log.write("doc error '%s'" % shop_id)
            fo_log.write(doc)


def get_shopping_review():
    table = "shopping_shop"
    sql_ = "WHERE shopId not in (select shopId from shopping_review)"
    shops = base_dao.select_shopid_and_reviewnum(table, sql_)
    for shop in shops:
        try:
            shop_id = shop[0]
            review_num = shop[1]
            page_num = (review_num + 15 - 1) / 15
            msg1 = "num.%d %s : totally %d pages review" % (shops.index(shop), shop_id, page_num)
            print msg1
            fo_log.write(msg1)
            if review_num < 1:
                continue
            get_shopping_review_on_page(shop_id, page_num)
        except BaseException, e:
            msg2 = "fail to get_shopping_review on shopId:%s", shop_id
            print e
            print msg2


def get_shopping_review_on_page(shop_id, page_num):
    index = 0
    flag = True
    while (flag):
        index += 1
        url = "http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18109820997935580524_1503472918639&params=%7B%22poi_id%22%3A%22" + str(
            shop_id) + "%22%2C%22page%22%3A" + str(index) + "%2C%22just_comment%22%3A1%7D&_=1503472928260"

        if index == page_num:
            flag = False
        time.sleep(random.uniform(2, 3))
        doc, msg = html_download.downloadPage_without_proxy(url, fo_log)
        if msg != "ok":
            continue
        try:
            review_ids, member_ids, likes, contents, stars, times = h_parser.parser_shopping_review(doc)
            msg = dao.insert_shopping_review(shop_id, review_ids, member_ids, likes, contents, stars, times)
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
