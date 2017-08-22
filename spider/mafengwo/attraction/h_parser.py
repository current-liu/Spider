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
filename = today_fo + ".txt"
fo_log = open("./log/" + filename, "a")
__author__ = 'Administrator'
__version__ = '1.0'


def parser_attraction_list(doc):
    res = json.loads(doc)
    succ = res["succ"]
    attractions = []
    msg = "ok"
    if succ == 1:
        list = res["data"]["list"]
        li_list = BeautifulSoup(list, "lxml").find_all("li")
        for li in li_list:
            href = li.find("a")["href"]
            shop_id = int(re.sub(r"\D", "", href))
            pic_url = li.find("div", class_="img").find("img")["src"]
            attraction = [shop_id, pic_url]
            attractions.append(attraction)
    else:
        msg = "fail"

    return attractions, msg


def parser_attraction_shops(doc):
    soup = BeautifulSoup(doc, "lxml")

    shop_name = "-1"
    shop_name_en = "-1"
    try:
        top = soup.find("div", class_="row row-top")
        title = top.find("div", class_="title")
        shop_name = title.find("h1").get_text()
        shop_name_en = title.find("div", class_="en").get_text()
    except BaseException, e:
        print e

    info = "-1"
    tel = "-1"
    site = "-1"
    time_use = "-1"
    trans = "-1"
    ticket = "-1"
    bussiness_time = "-1"
    try:
        detail = soup.find("div", class_="mod mod-detail")
        info = detail.find("div", class_="summary").get_text().strip().replace("'", "").replace('"', "")
        tel = detail.find("li", class_="tel").find("div", class_="content").get_text()
        site = detail.find("li", class_="item-site").find("div", class_="content").get_text()
        time_use = detail.find("li", class_="item-time").find("div", class_="content").get_text()
        dls = detail.find_all("dl")
        trans = dls[0].find("dd").get_text().strip().replace("'", "").replace('"', "")
        ticket = dls[1].find("dd").get_text().strip().replace("'", "").replace('"', "")
        bussiness_time = dls[2].find("dd").get_text()
    except BaseException, e:
        print e

    loc = "-1"
    try:
        loc = soup.find("div", class_="mod mod-location").find("p", class_="sub").get_text()
    except BaseException, e:
        print e

    inner_scenic = ""
    try:
        li_list = soup.find("div", class_="mod mod-innerScenic").find_all("li")
        for li in li_list:
            inner_scenic += re.sub(r"\D", "", li.find("a")["href"]) + " "
    except BaseException, e:
        print e

    review_num = "-1"
    try:
        span = soup.find("div", id="poi-navbar").find("a", title="蜂蜂点评")
        review_num = re.sub(r"\D", "", span.get_text())
    except BaseException, e:
        print e

    return shop_name, shop_name_en, info, tel, site, time_use, trans, ticket, bussiness_time, loc, inner_scenic, review_num


def parser_attraction_review(doc):
    json_data = doc.split("(", 1)[1].replace('"css":[],"js":[]}});', '"css":[],"js":[]}}')
    review_list = json.loads(json_data)['data']['html']
    soup = BeautifulSoup(review_list, "lxml")
    review_ids = []
    member_ids = []
    likes = []
    contents = []
    stars = []
    times = []
    try:
        comment_list = soup.find("div", class_='rev-list').find("ul").find_all("li", recursive=False)
        for comment in comment_list:
            review_id = -1
            member_id = -1
            like = 0
            try:
                review_id = comment.find("a", class_="useful")['data-id']
                member = comment.find("div", class_="user").find("a", class_="avatar")['href']
                member_id = re.sub(r"\D", "", member)
            except BaseException, e:
                print e
                msg1 = "get review_id,member_id failed "
                print msg1
                fo_log.write(msg1)

            try:
                like = int(comment.find("a", class_="useful").find("span", class_="useful-num").get_text())
            except BaseException, e:
                pass
            content = "-1"
            try:
                content = comment.find("p", class_="rev-txt").get_text().replace("\n", "").replace("'", "").replace('"',
                                                                                                                    "")
            except:
                pass
            star = -1
            try:
                comm_star = comment.find("span", recursive=False)
                star_str = comm_star['class'][1]
                star = int(re.sub(r"\D", "", star_str))
            except BaseException, e:
                pass
                create_time = "1946-01-01 00:00:00"
            try:
                time = comment.find("span", class_="time").get_text()
                create_time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

            except BaseException, e:
                pass
            pass

            review_ids.append(review_id)
            member_ids.append(member_id)
            likes.append(like)
            contents.append(content)
            stars.append(star)
            times.append(create_time)
    except BaseException, e:
        print e

    return review_ids, member_ids, likes, contents, stars, times
