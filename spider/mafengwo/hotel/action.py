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
# os.chdir()
filename = today_fo + ".txt"
fo_log = open("./log/" + filename, "a")


# os.chdir("..")


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
    table = "hotel_shops"
    shops = base_dao.select_shopid(table)
    fo_log.flush()
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
                                   info, sco_loc, sco_ser, sco_clear, sco_comfo, sco_fac, sco_food, tag, shop_id)
        except:
            fo_log.write("doc error '%s'" % shop_id)
            fo_log.write(doc)


def get_hotel_review():
    table = "hotel_shops"
    shops = base_dao.select_shopid_and_reviewnum(table)
    for shop in shops:
        shop_id = shop[0]
        review_num = shop[1]
        page_num = review_num / 10 + 1
        msg1 = "第'%d':'%s' 共'%d':页评论" % (shops.index(shop), shop_id, page_num)
        print msg1
        fo_log.write(msg1)
        get_hotel_review_on_page(shop_id, page_num)
    pass


def get_hotel_review_on_page(shop_id, page_num):
    url = "http://www.mafengwo.cn/hotel/info/comment_list?poi_id=" + str(shop_id) + "&type=0&keyword_id=0&page="
    index = 0
    flag = True
    while (flag):
        index += 1
        if index == page_num:
            flag = False

        url_full = url + str(index)

        doc, msg = html_download.downloadPage(url_full, fo_log)
        if msg != "ok":
            continue
        try:
            review_ids, member_ids, likes, contents, stars, times = h_parser.parser_hotel_review(doc)
            msg = dao.insert_hotel_review(shop_id, review_ids, member_ids, likes, contents, stars, times)
            if msg == "for key 'PRIMARY'":
                msg2 = "shopId %s 已循环到已经爬过内容" % shop_id
                print msg2
                fo_log.write(msg2)
                break

        except BaseException, e:
            print e
    msg3 = "shopId %s log to pageno=%s" % (shop_id, index)
    print msg3
    fo_log.write(msg3)


def get_hotel_room():
    url = "http://www.mafengwo.cn/hotel/36273.html#checkin=2017-08-16&checkout=2017-08-17&guests=2-0"
    table = "hotel_shops"
    shops = base_dao.select_shopid(table)
    fo_log.flush()
    for shop in shops:
        shop_id = shop[0]
        msg1 = "第'%d':'%s'" % (shops.index(shop), shop_id)
        print msg1
        fo_log.write(msg1)
        # TODO


def get_room_on_the_day():
    pass
