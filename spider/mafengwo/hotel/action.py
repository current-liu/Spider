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

from mafengwo.url_manager import UrlSet
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
# os.chdir()
filename = today_fo + ".txt"
fo_log = open("./log/" + filename, "a")

room_url_list = UrlSet()


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
        dao.insert_hotel_shop(shopIds, picUrls, areas, review_nums, travel_nums)

        time.sleep(random.uniform(2, 3))


def get_hotel_shop():
    table = "hotel_shop"
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
            dao.update_hotel_shop(shop_name, shop_name_en, score, loc, checkIn, checkOut, built, room_num, service,
                                  info, sco_loc, sco_ser, sco_clear, sco_comfo, sco_fac, sco_food, tag, shop_id)
        except:
            fo_log.write("doc error '%s'" % shop_id)
            fo_log.write(doc)


def get_hotel_review():
    table = "hotel_shop"
    shops = base_dao.select_shopid_and_reviewnum(table)
    for shop in shops:
        shop_id = shop[0]
        review_num = shop[1]
        page_num = (review_num + 10 - 1) / 10
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

    fo_log.flush()

    init_room_url_list()

    global room_url_list
    global today
    index = 0
    while (room_url_list.has_new_url()):
        try:
            try:
                urls = room_url_list.get_new_url()
                index += 1
                s = urls.split("mddid")[0].split("poi_id=")[1]
                shopId = int(re.sub(r'\D', "", s))
                print "crawling_room num.'%s' shopId: '%s'" % (index, shopId)
                url_list = urls.split(" ")
            except BaseException, e:
                print e
                msg0 = "fail to get url"
                print msg0
                continue
            doc_list = []
            for url in url_list:
                time.sleep(random.uniform(3, 4))
                doc, msg = html_download.downloadPage_without_proxy(url, fo_log)
                doc_list.append(doc)
            # doc0, msg = html_download.downloadPage(url_list[0], fo_log)
            # doc1, msg = html_download.downloadPage(url_list[1], fo_log)
            # doc2, msg = html_download.downloadPage(url_list[2], fo_log)
            # doc3, msg = html_download.downloadPage(url_list[3], fo_log)
            # doc4, msg = html_download.downloadPage(url_list[4], fo_log)
            # doc_list = (doc0, doc1, doc2, doc3, doc4)

            try:
                rooms_info_total = h_parser.get_room(doc_list)
            except BaseException, e:
                print e
                msg1 = "fail to parser hotel room"
                print msg1
                continue

            query_time = today_str
            ota = "youyu_pkg"
            dao.insert_hotel_room(shopId, rooms_info_total, query_time, ota)

        except BaseException, e:
            print e


def init_room_url_list():
    global room_url_list
    global today
    global today_str
    after_1 = today + datetime.timedelta(days=1)
    after_2 = today + datetime.timedelta(days=2)
    after_3 = today + datetime.timedelta(days=3)
    after_4 = today + datetime.timedelta(days=4)
    after_5 = today + datetime.timedelta(days=5)

    checkinDate_0 = today.strftime("%Y-%m-%d")
    checkoutDate_0 = after_1.strftime("%Y-%m-%d")
    checkinDate_1 = after_1.strftime("%Y-%m-%d")
    checkoutDate_1 = after_2.strftime("%Y-%m-%d")
    checkinDate_2 = after_2.strftime("%Y-%m-%d")
    checkoutDate_2 = after_3.strftime("%Y-%m-%d")
    checkinDate_3 = after_3.strftime("%Y-%m-%d")
    checkoutDate_3 = after_4.strftime("%Y-%m-%d")
    checkinDate_4 = after_4.strftime("%Y-%m-%d")
    checkoutDate_4 = after_5.strftime("%Y-%m-%d")

    shop_id_list = dao.download_hotel_shopIds_unselected(today_str)

    for shop_id in shop_id_list:
        i = str(shop_id)
        shop_id_str = re.sub(r'\D', "", i)
        # "http://server.mafengwo.cn/hotel/ajax.php?sJsonCallBack=jQuery18109789543989958343_1502861850903&sAction=getRealPrice&iMddId=10189&iPoiId=36273&sOta=youyu_pkg&sCheckIn=2017-08-19&sCheckOut=2017-08-20&iAdultsNum=2&iChildrenNum=0&sChildrenAge=&_=1502862132197"
        str1 = "http://server.mafengwo.cn/hotel/ajax.php?sJsonCallBack=jQuery18109789543989958343_1502861850903&sAction=getRealPrice&iMddId=10189&iPoiId="
        str2 = "&sOta=youyu_pkg&sCheckIn="
        str3 = "&sCheckOut="
        str4 = "&iAdultsNum=2&iChildrenNum=0&sChildrenAge=&_=1502862132197"


        "http://www.mafengwo.cn/hotel/ajax_remote/price?poi_id=36273&mddid=10189&ota=youyu_pkg&check_in=2017-11-21&check_out=2017-11-22&adults_num=2&children_num=0&children_age=&platform=www"
        str1 = "http://www.mafengwo.cn/hotel/ajax_remote/price?poi_id="
        str2 = "&mddid=10189&ota=youyu_pkg&check_in="
        str3 = "&check_out="
        str4 = "&adults_num=2&children_num=0&children_age=&platform=www"
        u0 = str1 + shop_id_str + str2 + checkinDate_0 + str3 + checkoutDate_0 + str4
        u1 = str1 + shop_id_str + str2 + checkinDate_1 + str3 + checkoutDate_1 + str4
        u2 = str1 + shop_id_str + str2 + checkinDate_2 + str3 + checkoutDate_2 + str4
        u3 = str1 + shop_id_str + str2 + checkinDate_3 + str3 + checkoutDate_3 + str4
        u4 = str1 + shop_id_str + str2 + checkinDate_4 + str3 + checkoutDate_4 + str4

        room_url_list.add_new_url(u0 + " " + u1 + " " + u2 + " " + u3 + " " + u4)

    u = room_url_list.get_new_url()

    "http://server.mafengwo.cn/hotel/ajax.php?sJsonCallBack=jQuery18109789543989958343_1502861850903&sAction=getRealPrice&iMddId=10189&iPoiId=36273&sOta=youyu_pkg&sCheckIn=2017-08-19&sCheckOut=2017-08-20&iAdultsNum=2&iChildrenNum=0&sChildrenAge=&_=1502862132197"
    "http://server.mafengwo.cn/hotel/ajax.php?sJsonCallBack=jQuery18109789543989958343_1502861850902&sAction=getRealPrice&iMddId=10189&iPoiId=36273&sOta=hotels&sCheckIn=2017-08-19&sCheckOut=2017-08-20&iAdultsNum=2&iChildrenNum=0&sChildrenAge=&_=1502862132199"
    "http://server.mafengwo.cn/hotel/ajax.php?sJsonCallBack=jQuery18109789543989958343_1502861850901&sAction=getRealPrice&iMddId=10189&iPoiId=36273&sOta=booking&sCheckIn=2017-08-19&sCheckOut=2017-08-20&iAdultsNum=2&iChildrenNum=0&sChildrenAge=&_=1502862132201"
    "http://server.mafengwo.cn/hotel/ajax.php?sJsonCallBack=jQuery18109789543989958343_1502861850904&sAction=getRealPrice&iMddId=10189&iPoiId=36273&sOta=agoda&sCheckIn=2017-08-19&sCheckOut=2017-08-20&iAdultsNum=2&iChildrenNum=0&sChildrenAge=&_=1502862132203"
    "http://server.mafengwo.cn/hotel/ajax.php?sJsonCallBack=jQuery18109789543989958343_1502861850905&sAction=getRealPrice&iMddId=10189&iPoiId=36273&sOta=youyu&sCheckIn=2017-08-19&sCheckOut=2017-08-20&iAdultsNum=2&iChildrenNum=0&sChildrenAge=&_=1502862132204"
