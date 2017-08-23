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


def parser_shopping_list(doc):
    shoppings = []
    msg = json.loads(doc)['msg']
    if msg != "succ":
        return shoppings

    html = json.loads(doc)['html']['html']
    soup = BeautifulSoup(html, "lxml")

    try:
        ul = soup.find("div", class_="poi-list")
        li_list = ul.find_all("div", class_="poi-item clearfix", recursive=False)
    except BaseException, e:
        print e
        msg1 = "parser page fail"
        print msg1
    else:
        for li in li_list:
            try:
                href = li.find("a", class_="img")["href"]
                shop_id = int(re.sub(r"\D", "", href))
                pic_url = li.find("a", class_="img").find("img")["src"]
                shopping = [shop_id, pic_url]
                shoppings.append(shopping)
            except BaseException, e:
                print e
                msg2 = "parser shopping_shop fail"
                print msg2
    return shoppings


def parser_shopping_shops(doc):
    soup = BeautifulSoup(doc, "lxml")

    shop_name = "-1"
    shop_name_en = "-1"
    try:
        title = soup.find("div", class_="title")
        shop_name = title.find("h1").get_text()
        shop_name_en = title.find("div", class_="en").get_text()
    except BaseException, e:
        print e

    score = "-1"
    star = "-1"
    review_num = "0"
    tip = "-1"
    try:
        info = soup.find("div", class_="info")
        grade = info.find("div", class_="grade")
        score_str = grade.find("span", class_="score").get_text()
        score = re.sub(r"\D", "", score_str)
        star_str = grade.find("span", class_="star").find("span")['class'][0]
        star = re.sub(r"\D", "", star_str)
        review_num_str = info.find("div", class_="rev-count").find("em").get_text()
        review_num = re.sub(r"\D", "", review_num_str)
        tip = info.find("div", class_="rev-txt").get_text()
    except BaseException, e:
        print e

    site = "-1"
    tel = "-1"
    try:
        baseinfo = soup.find("div", class_="mbd clearfix").find("ul", class_="baseinfo clearfix")
        tel = baseinfo.find("li", class_="item-tel").find("div", class_="content").get_text()
        site = baseinfo.find("li", class_="item-site").find("div", class_="content").get_text()

    except BaseException, e:
        print e

    intro = "-1"
    trans = "-1"
    loc = "-1"
    try:
        detail_dls = soup.find("div", class_="main-detail").find_all("dl")
        for dl in detail_dls:
            label = dl.find("dt").get_text()
            if label == "简介":
                intro = dl.find("dd").get_text()
            elif label == "地址":
                loc = dl.find("dd").find("div", class_="address").get_text()
            elif label == "交通":
                trans = detail_dls[2].find("dd").get_text()

    except BaseException, e:
        print e
    return shop_name, shop_name_en, score, star, review_num, tip, site, tel, intro, trans, loc


def parser_shopping_review(doc):
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
