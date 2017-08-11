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
from mafengwo import html_download
import h_parser
import dao
from mafengwo import base_dao

__author__ = 'Administrator'
__version__ = '1.0'
today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")
today_fo = today.strftime("%Y%m%d")
os.chdir("./log")
filename = today_fo + ".txt"
fo_log = open(filename, "a")


def get_hotel_list():
    flag = True
    hotel_total = 706
    page_num = hotel_total / 15 + 1
    index = 0
    while (flag):
        index += 1
        print "page:'%d'" % index
        if (index == page_num):
            flag = False
        url = "http://www.mafengwo.cn/search/s.php?q=%E9%A6%99%E6%B8%AF&p=" + str(index) + "&t=hotel&kt=1"
        doc, msg = html_download.downloadPage_without_proxy(url, fo_log)
        if msg != "ok":
            print "失败", url
        shopIds, picUrls, areas, review_nums, travel_nums = h_parser.parser_hotel_list(doc)
        dao.insert_hotel_shops(shopIds, picUrls, areas, review_nums, travel_nums)

        time.sleep(random.uniform(2, 3))


def get_hotel_shops():
    shops = base_dao.select_shopid("hotel_shops")

    for shop in shops:
        shop_id = shop[0]
        msg1 = "第'%d':'%s'" % (shops.index(shop), shop_id)
        print msg1
        fo_log.write(msg1)
        url = "http://www.mafengwo.cn/hotel/" + str(shop_id) + ".html"
        doc, msg = html_download.downloadPage_without_proxy(url, fo_log)

        if msg != "ok":
            continue
        try:
            shop_name, shop_name_en, score, loc, checkIn, checkOut, built, room_num, service, info, \
            sco_loc, sco_ser, sco_clear, sco_comfo, sco_fac, sco_food, tag = h_parser.parser_hotel_shops(doc)
            msg2 = "shopId:'%s'解析完成，正写入数据" % shop_id
            print msg2
            dao.update_hotel_shops(shop_name, shop_name_en, score, loc, checkIn, checkOut, built, room_num, service,
                                   info,sco_loc, sco_ser, sco_clear, sco_comfo, sco_fac, sco_food, tag, shop_id)
        except:
            fo_log.write("doc error '%s'" % shop_id)
            fo_log.write(doc)
