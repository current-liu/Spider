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


def get_food_list():
    area01 = ["尖沙咀", 170, 76]
    area02 = ["旺角/油麻地", 175, 84]
    area03 = ["湾仔及铜锣湾", 173, 114]
    area04 = ["太子/深水埗", 2243, 60]
    area05 = ["上环", 172, 50]
    area06 = ["中环/金钟", 1725, 40]
    area07 = ["迪士尼乐园", 176, 3]
    area08 = ["九龙城", 2347, 47]
    area09 = ["荃湾区", 8428, 39]
    area10 = ["香港仔/海洋公园", 2338, 7]
    area11 = ["赤鱲角机场", 174, 13]
    area12 = ["沙田", 12071, 22]
    area13 = ["南丫岛", 12086, 4]
    area14 = ["北角", 46183, 12]
    areas = [area01, area02, area03, area04, area05, area06, area07, area08, area09, area10, area11, area12, area13,
             area14]
    for area in areas:
        area = areas[12]
        area_num = area[1]
        pages = area[2]
        area_name = area[0]
        flag = True
        index = 0
        while (flag):
            index += 1
            if index == pages:
                flag = False
            url = "http://www.mafengwo.cn/cy/10189/0-" + str(area_num) + "-0-0-0-" + str(index) + ".html"

            doc, msg = html_download.downloadPage_without_proxy(url, fo_log)
            if msg != "ok":
                continue
            else:
                food_shops = h_parser.parser_food_list(doc)
                dao.insert_food_shop(food_shops, area_name)


def get_food_shop():
    table = "food_shop"
    shops = base_dao.select_shopid(table, "WHERE shopName Is Null ")
    fo_log.flush()
    for shop in shops:
        shop_id = shop[0]
        # shop_id = 520
        msg1 = "num. '%d':'%s'" % (shops.index(shop), shop_id)
        print msg1
        fo_log.write(msg1)

        url = "http://www.mafengwo.cn/poi/" + str(shop_id) + ".html"
        doc, msg = html_download.downloadPage_without_proxy(url, fo_log)

        if msg != "ok":
            continue

        try:
            shop_name, loc, tel, score, star, review_num = h_parser.parser_food_shops(doc)
            msg2 = "shopId:'%s' parser complete，inserting into database" % shop_id
            print msg2
            dao.update_food_shop(shop_name, loc, tel, score, star, review_num, shop_id)
        except:
            # TODO 这里会接到异常吗？ 两个函数的异常都在内部处理过了
            fo_log.write("doc error '%s'" % shop_id)
            fo_log.write(doc)


def get_food_review():
    table = "food_shop"
    shops = base_dao.select_shopid_and_reviewnum(table)
    for shop in shops:
        shop_id = shop[0]
        review_num = shop[1]
        page_num = (review_num + 15 - 1) / 15
        msg1 = "num.%d %s : totally %d pages review" % (shops.index(shop), shop_id, page_num)
        print msg1
        fo_log.write(msg1)
        get_food_review_on_page(shop_id, page_num)
    pass


def get_food_review_on_page(shop_id, page_num):
    index = 0
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
            review_ids, member_ids, likes, contents, stars, times = h_parser.parser_food_review(doc)
            msg = dao.insert_food_review(shop_id, review_ids, member_ids, likes, contents, stars, times)
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
