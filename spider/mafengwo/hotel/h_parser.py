#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/10 0010 下午 3:01

base Info
"""
import os
import re

import datetime
from bs4 import BeautifulSoup
from pandas import json

today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")
today_fo = today.strftime("%Y%m%d")
# os.chdir("./log")
filename = today_fo + ".txt"
fo_log = open("./log/" + filename, "a")
__author__ = 'Administrator'
__version__ = '1.0'


def parser_hotel_list(doc):
    soup = BeautifulSoup(doc, "lxml")
    hotel_list = soup.find("div", class_="hot-list")
    hotels = hotel_list.find_all("div", class_="hot-about clearfix _j_hotel")
    shopIds = []
    picUrls = []
    areas = []
    review_nums = []
    travel_nums = []
    for hotel in hotels:
        shopId = hotel['data-id']
        picUrl = hotel.find("div", class_="flt1").find("a").find("img")['src']
        seg_info_list = hotel.find("ul", class_="seg-info-list clearfix").find_all("li")
        area = seg_info_list[0].get_text().split("香港-")[1]
        review_num = re.sub(r'\D', "", seg_info_list[1].get_text())
        travels_num = re.sub(r'\D', "", seg_info_list[2].get_text())

        shopIds.append(shopId)
        picUrls.append(picUrl)
        areas.append(area)
        review_nums.append(review_num)
        travel_nums.append(travels_num)

    return shopIds, picUrls, areas, review_nums, travel_nums


def parser_hotel_shops(doc):
    soup = BeautifulSoup(doc, "lxml")

    score = "-1"
    shop_name = "-1"
    shop_name_en = "-1"
    loc = "-1"
    try:
        hotel_intro = soup.find("div", class_="hotel-intro")
        shop_name = hotel_intro.find("div", class_="main-title").get_text().replace("\n", "").replace("'", "").replace(
            '"', "").split("(")[0]
        shop_name_en = hotel_intro.find("div", class_="en-title").get_text().replace("\n", "").replace("'", "").replace(
            '"', "")
        loc = hotel_intro.find("div", class_="location").find("span").get_text().get_text().replace("\n", "").replace(
            "'", "").replace('"', "")
        score = re.sub(r"\D", "", hotel_intro.find("span", class_="score").get_text())

    except BaseException, e:
        msg1 = "in get_hotel_shops() shop_name, shop_name_en, score, loc"
        print msg1
        fo_log.write(msg1)
        print e

    try:
        hotel_info = soup.find("div", class_="hotel-info")
        info_sections = hotel_info.find_all("div", class_="info-section")

        checkIn = "-1"
        checkOut = "-1"
        built = "-1"
        room_num = "-1"
        try:
            basic_infos = info_sections[0].find("dd", class_="clearfix").find_all("div", class_="cell")
            basic_info_list = {u"入住时间": "", u"离店时间": "", u"建成于": "", u"酒店规模": ""}

            b_cells = []
            for b in basic_infos:
                b_cells.append(b.get_text())
            for b_cell in b_cells:
                label = b_cell.split(":")[0].replace("\n", "")
                content = b_cell.split(":")[1].replace("\n", "")
                basic_info_list[label] = content

            checkIn = basic_info_list[u"入住时间"] + "之后"
            checkOut = basic_info_list[u"离店时间"] + "之前"
            built = basic_info_list[u"建成于"]
            room_num = int(re.sub(r"\D", "", basic_info_list[u"酒店规模"]))
        except BaseException, e:
            msg2 = "in get_hotel_shops() checkIn, checkOut, built, room_num"
            print msg2
            fo_log.write(msg2)
            print e

        service = "-1"
        try:
            expand_wrap = info_sections[1].find("div", class_="expand-wrap")
            service = expand_wrap.get_text().replace("\n", " ").replace("'", "").replace('"', "")
        except BaseException, e:
            msg3 = "in get_hotel_shops() service"
            print msg3
            fo_log.write(msg3)
            print e

        info = "-1"
        try:
            expand_wrap1 = info_sections[2].find("div", class_="expand-wrap")
            info = expand_wrap1.get_text().replace("\n", "").replace("'", "").replace('"', "")
        except BaseException, e:
            msg4 = "in get_hotel_shops() info"
            print msg4
            fo_log.write(msg4)
            print e

    except BaseException, e:
        print e

    try:
        comment = soup.find("div", class_="hotel-comment")

        sco_list = {}
        sco_loc = ""
        sco_ser = ""
        sco_clear = ""
        sco_comfo = ""
        sco_fac = ""
        sco_food = ""
        try:
            hotel_score = comment.find("dl", class_="hotel-score clearfix")
            dds = hotel_score.find_all("dd")
            sco_list = {u"位置": "", u"服务": "", u"清洁度": "", u"舒适度": "", u"设施": "", u"餐饮": "", }
            for dd in dds:
                text = dd.get_text()
                sco = re.sub(r"\D", "", text)
                lab = re.sub(r"\d", "", text).strip().replace('.', "")
                sco_list[lab] = sco

            sco_loc = sco_list[u"位置"]
            sco_ser = sco_list[u"服务"]
            sco_clear = sco_list[u"清洁度"]
            sco_comfo = sco_list[u"舒适度"]
            sco_fac = sco_list[u"设施"]
            sco_food = sco_list[u"餐饮"]
        except BaseException, e:
            msg5 = "in get_hotel_shops() soc_list"
            print msg5
            fo_log.write(msg5)
            print e

        rev_tags = ""
        try:
            rev_tags = comment.find("div", class_="rev-tags") \
                .get_text().replace("\n", "").replace("'", "").replace('"', "")
        except BaseException, e:
            msg6 = "in get_hotel_shops() tags"
            print msg6
            fo_log.write(msg6)
            print e
    except BaseException, e:
        pass

    return shop_name, shop_name_en, score, loc, checkIn, checkOut, built, room_num, service, info, \
           sco_loc, sco_ser, sco_clear, sco_comfo, sco_fac, sco_food, rev_tags


def parser_hotel_review(doc):
    review_list = json.loads(doc)['html']
    soup = BeautifulSoup(review_list, "lxml")
    review_ids = []
    member_ids = []
    likes = []
    contents = []
    stars = []
    times = []
    try:
        comment_list = soup.find_all("div", class_="comm-item _j_comment_item")
        for comment in comment_list:
            review_id = -1
            member_id = -1
            try:
                review_id = int(comment['data-id'])
                member = comment.find("div", class_="user").find("a", class_="avatar")['href']
                member_id = int(re.sub(r"\D", "", member.split("&")[0]))
            except BaseException, e:
                print e
                msg1 = "review_id,member_id获取失败"
                print msg1
                fo_log.write(msg1)

            like = -1
            try:
                like = int(comment.find("div", class_="like").get_text())
            except:
                pass
            content = "-1"
            try:
                content = comment.find("div", class_="txt").get_text().replace("\n", "").replace("'", "").replace('"',
                                                                                                                  "")
            except:
                pass
            star = -1
            try:
                comm_star = comment.find("div", class_="comm-meta").find("span")
                star_str = comm_star['class'][2]
                star = int(re.sub(r"\D", "", star_str))
            except BaseException, e:
                pass
                create_time = "1946-01-01 00:00:00"
            try:
                time = comment.find("span", class_="time").get_text()
                create_time = datetime.datetime.strptime(time, '%Y-%m-%d')

            except:
                pass
            pass

            review_ids.append(review_id)
            member_ids.append(member_id)
            likes.append(like)
            contents.append(content)
            stars.append(star)
            times.append(create_time)

        return review_ids, member_ids, likes, contents, stars, times
    except BaseException, e:
        print e


def get_room(doc_list):
    """获取每个酒店房型的详细信息"""

    room_infos = []
    room_name = "-1"
    for doc in doc_list:
        try:
            #TODO
            room = json.loads(doc.split("(")[1].split(")")[0])
            price = room['msg']['list']["youyu_pkg"]
        except BaseException, e:
            print e
            print "获取酒店房型详情失败"
            price = "-1"
        else:
            if (price == 0):
                print "房型信息为空"
            else:
                print "成功获取房型"
                if room_name == "-1":
                    room_name = room['msg']['room_name']

        room_infos.append(price)

    room_infos.append(room_name)
    return room_infos
