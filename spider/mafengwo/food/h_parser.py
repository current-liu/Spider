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


def parser_food_list(doc):
    soup = BeautifulSoup(doc, "lxml")
    foods = []
    try:
        ul = soup.find("ul", class_="poi-list")
        li_list = ul.find_all("li", recursive=False)
    except BaseException, e:
        print e
        msg1 = "parser page fail"
        print msg1
    else:
        for li in li_list:
            try:
                href = li.find("span", class_="img").find("a")["href"]
                shop_id = int(re.sub(r"\D", "", href))
                pic_url = li.find("span", class_="img").find("a").find("img")["src"]
                food = [shop_id, pic_url]
                foods.append(food)
            except BaseException, e:
                print e
                msg2 = "parser food_shop fail"
                print msg2
    return foods


def parser_food_shops(doc):
    soup = BeautifulSoup(doc, "lxml")

    shop_name = "-1"
    try:
        top = soup.find("div", class_="title clearfix")
        title = top.find("div", class_="t")
        shop_name = title.find("h1").get_text()
    except BaseException, e:
        print e
    score = "-1"
    star = "-1"
    review_num = "-1"
    try:
        score_info = soup.find("div", class_="score")
        score_str = score_info.find("span", class_="score-info").get_text()
        score = re.sub(r"\D", "", score_str)
        star_str = score_info.find("span", class_="comm-info").find("div", class_="rank-star").find("span")['class'][0]
        star = re.sub(r"\D", "", star_str)
        review_num_str = score_info.find("p", class_="ranking").find("em").get_text()
        review_num = re.sub(r"\D", "", review_num_str)
    except BaseException, e:
        print e

    loc = "-1"
    tel = "-1"
    # TODO 根据子标签的内容，来判断时什么信息
    try:
        m_box_li_list = soup.find("div", class_="m-box m-info").find_all("li")

        li_01 = m_box_li_list[0]
        content_01 = li_01.get_text()
        icon_01 = li_01.find("i")['class'][0]
        if icon_01 == "icon-location":
            loc = content_01.split("址：")[1].replace(" ", "").replace("\n", "")
        elif icon_01 == "icon-tel":
            tel = content_01.replace(" ", "").replace("\n", "")

        li_02 = m_box_li_list[1]
        content_02 = li_02.get_text()
        icon_02 = li_02.find("i")['class'][0]
        if icon_02 == "icon-tel":
            tel = content_02.replace(" ", "").replace("\n", "")

    except BaseException, e:
        print e
    return shop_name, loc, tel, score, star, review_num


def parser_food_review(doc):
    review_ids = []
    member_ids = []
    likes = []
    contents = []
    stars = []
    times = []

    msg = json.loads(doc)['msg']
    if msg != "succ":
        return review_ids, member_ids, likes, contents, stars, times

    html = json.loads(doc)['html']['html']
    soup = BeautifulSoup(html, "lxml")
    try:
        comment_list = soup.find_all("div", class_='comment-item')
        for comment in comment_list:
            review_id = -1
            member_id = -1

            try:
                review_id = re.sub(r"\D", "", comment['id'])
                member = comment.find("div", class_="user-bar").find("span", class_="user-avatar").find("a")['href']
                member_id = re.sub(r"\D", "", member)
            except BaseException, e:
                print e
                msg1 = "get review_id,member_id failed "
                print msg1
                fo_log.write(msg1)

            like = 0
            try:
                like = int(comment.find("span", class_="useful").find("span", class_="useful-num").get_text())
            except BaseException, e:
                pass
            content = "-1"
            try:
                content = comment.find("p", class_="rev-txt").get_text().replace("\n", "").replace("'", "").replace('"',
                                                                                                                    "")
            except:
                pass

            star = 0
            try:
                comm_star = comment.find("span", class_="rank-star").find("span")
                star_str = comm_star['class'][0]
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
