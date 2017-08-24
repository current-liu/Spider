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


def parser_member(doc):
    try:
        soup = BeautifulSoup(doc, "lxml")
        avatar = soup.find("div", class_="MAvatar")
    except BaseException, e:
        print e
        msg1 = "part1"
        print msg1

    pic = "-1"
    name = "-1"
    gender = "-1"
    try:
        pic = avatar.find("div", class_="MAvaImg hasAva").find("img")['src']
        name = avatar.find("div", class_="MAvaName").get_text().strip().replace("\n", "").replace("'", "").replace('"',
                                                                                                                   "")
        gender_tag = avatar.find("div", class_="MAvaName").find("i")
        gender_s = gender_tag['class'][0]
        if gender_s == 'MGenderMale':
            gender = "male"
        elif gender_s == "MGenderFemale":
            gender = "female"
    except BaseException, e:
        print e
        msg2 = "part2"
        print msg2

    vip = 0
    duo = 0
    zhi = 0
    try:
        its_tags = avatar.find("div", class_="its_tags")
        tags = its_tags.find_all("a")
        t0 = tags[0].find("i")['class']
        t1 = tags[1].find("i")['class']
        t2 = tags[2].find("i")['class']

        if t0.__len__() == 2:
            vip = 1
        if t1.__len__() == 2:
            duo = 1
        if t2.__len__() == 2:
            zhi = 1
    except BaseException, e:
        print e
        msg3 = "part3"
        print msg3

    level = -1
    loc = "-1"
    try:
        info = avatar.find("div", class_="MAvaInfo clearfix")
        level = int(re.sub(r"\D", "", info.find("span", class_="MAvaLevel flt1").find("a").get_text()))
        loc = str(info.find("span", class_="MAvaPlace flt1").get_text()).split("：")[1]

    except BaseException, e:
        print e
        msg4 = "part4"
        print msg4

    profile = "-1"
    try:
        profile = avatar.find("div", class_="MProfile").get_text().strip().replace("\n", "").replace("'", "").replace(
            '"', "")
    except BaseException, e:
        print e
        msg5 = "part5"
        print msg5
    follow = "-1"
    fans = "-1"
    contribution = "-1"
    try:
        avamore = avatar.find("div", class_="MAvaMore clearfix").find_all("div")
        follow = avamore[0].find("a").get_text()
        fans = avamore[1].find("a").get_text()
        contribution = avamore[2].find("a").get_text()
    except BaseException, e:
        print e
        msg6 = "part6"
        print msg6
    review = "-1"
    try:
        review = re.sub(r"\D", "", soup.find("div", class_="common_block my_ask my_dp").find("div",
                                                                                             class_="more_notes").get_text())
    except BaseException, e:
        print e
        msg7 = "part7"
        print msg7

    return pic, name, gender, vip, duo, zhi, level, loc, profile, follow, fans, contribution, review


def parser_member_review(doc):
    html = json.loads(doc)["data"]["html"]
    hasmore = json.loads(doc)["data"]["hasmore"]
    soup = BeautifulSoup(html, "lxml")
    reviews = soup.find("html").find("body").find_all("div", recursive=False)
    member_reviews = []
    for review in reviews:
        data_typeid = "-1"
        review_id = "-1"
        create_time = "1946-01-01 00:00:00"
        try:
            data_typeid = review["data-typeid"]
            review_id = review["data-itemid"]
            createTime_str = soup.find("span", class_="time").get_text()
            create_time = datetime.datetime.strptime(createTime_str, '%Y-%m-%d %H:%M:%S')
        except BaseException, e:
            print e
        like = "0"
        star = "0"
        shopName = "-1"
        shopId = "-1"

        try:
            detail = review.find("div", class_="poi-detail")
            like = re.sub(r"\D", "", detail.find("span", class_="s-ding").get_text())
            shopName = detail.find("h3", class_="title").get_text()
            shopId_str = detail.find("h3", class_="title").find("a")["href"]
            shopId = re.sub(r"\D", "", shopId_str)
            star = detail.find("div", class_="rating")["data-star"]


        except BaseException, e:
            print e

        member_review = [shopId, shopName, review_id, star, like, create_time, data_typeid]
        member_reviews.append(member_review)

    return member_reviews, hasmore
