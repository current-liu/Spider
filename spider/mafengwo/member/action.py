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


def get_member(table):
    # dao.update_member_mark("hotel_review", 1)

    try:
        member_ids = dao.select_member_id_not_in_member(table)
        print "%d members to update this time in %s" % (member_ids.__len__(), table)
        # member_ids = [(17212115,)]
        for member in member_ids:
            time.sleep(random.uniform(3, 4))
            index = member_ids.index(member)
            member_id = member[0]

            url = "http://www.mafengwo.cn/u/" + str(member_id) + ".html"
            msg0 = "num.'%d' member_id:'%d'" % (index, member_id)
            print msg0
            doc, msg = html_download.downloadPage_without_proxy(url, fo_log)
            if msg != "ok":
                continue
            try:
                pic, name, gender, vip, duo, zhi, level, loc, profile, follow, fans, contribution, \
                    review = h_parser.parser_member(doc)
            except BaseException, e:
                print e
                msg1 = "in parser_member()"
                print msg1
            try:
                dao.insert_member(pic, name, gender, vip, duo, zhi, level, loc, profile, follow, fans, contribution,
                                  review, member_id)
            except BaseException, e:
                print e
                msg2 = "in insert_member()"
                print msg2
                # TODO mysql server has gone away 的处理
            # 改在每次get_member之前从表中更新
            # else:
            #     # 查询成功的member_id积累到一定的量，打mark
            #     queried_member_ids.append(member_id)
            #     if index % 100 == 0:
            #         for member_id in queried_member_ids:
            #             dao.update_member_mark("hotel_review", 1, member_id)

    except BaseException, e:
        print e
        msg1 = "in get_member()"
        print msg1
    # finally:
    #     for member_id in queried_member_ids:
    #         dao.update_member_mark("hotel_review", 1, member_id)


def get_member_path():
    try:
        sql_ = "AND name != '-1' AND review > 0"
        member_ids = dao.select_member_id_not_in_member_path(sql_)
        for member in member_ids:

            index = member_ids.index(member)
            member_id = member[0]
            # member_id = 35464616

            msg0 = "num.'%d' member_id:'%d'" % (index, member_id)
            print msg0

            get_member_path_on_page(member_id)
            get_member_path_on_page_03(member_id)

    except BaseException, e:
        print e


def get_member_path_on_page(member_id):
    offset = 0
    hasmore = False
    while True:
        time.sleep(random.uniform(3, 4))

        url = "http://www.mafengwo.cn/home/ajax_review.php?act=loadList&filter=0&offset=" + str(
            offset) + "&limit=40&uid=" + str(member_id) + "&sort=1"

        doc, msg = html_download.downloadPage_without_proxy(url, fo_log)
        if msg == "ok":
            try:
                member_reviews, hasmore = h_parser.parser_member_review(doc, member_id)
                dao.insert_member_path(member_reviews)
            except BaseException, e:
                print e
                msg1 = "in get_member_path_on_page(member_id)"
                print msg1
        if (hasmore == False):
            break
        else:
            offset += 40


def get_member_path_on_page_03(member_id):
    """未点评的"""
    offset = 0
    hasmore = False
    while True:
        time.sleep(random.uniform(3, 4))

        url = "http://www.mafengwo.cn/home/ajax_review.php?act=loadList&filter=3&offset=" + str(
            offset) + "&limit=40&uid=" + str(member_id) + "&sort=1"

        doc, msg = html_download.downloadPage_without_proxy(url, fo_log)
        if msg == "ok":
            try:
                member_reviews, hasmore = h_parser.parser_member_review_03(doc, member_id)
                dao.insert_member_path(member_reviews)
            except BaseException, e:
                print e
                msg1 = "in get_member_path_on_page_03(member_id)"
                print msg1
        if (hasmore == False):
            break
        else:
            offset += 40
