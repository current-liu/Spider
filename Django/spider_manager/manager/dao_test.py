#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/9/13 0013 下午 2:27

base Info
"""
import pymysql
import sys
from django.http import HttpResponse, JsonResponse
from manager import dao

reload(sys)
sys.setdefaultencoding("utf8")

db = pymysql.connect("127.0.0.1", "root", "liu1991chao", "spider_manager", charset="utf8mb4")

cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print data
__author__ = 'liuchao'
__version__ = '1.0'


def get_date_to_update_spider_num():
    res = dao.get_date_to_update_spider_num()
    date_list = []
    for r in res:
        date = r[0]
        date_list.append((date, date))

    return date_list


def update_spider_num():
    date_list = get_date_to_update_spider_num()
    dao.update_spider_num(date_list)


def get_spider_num_group_by_date(request):
    print "get_spider_num_group_by_date"
    spiders_2 = dao.get_spider_num_group_by_date(2)
    spiders_3 = dao.get_spider_num_group_by_date(3)
    spiders_num = dao.select_spider_num_up_to_date()
    length = spiders_2.__len__()
    spider_4_list = []
    spider_2_list = []
    spider_3_list = []

    for i in range(0, length):
        date = spiders_2[i][0]
        s_2 = spiders_2[i][1]
        s_3 = spiders_3[i][1]
        s_all = spiders_num[i][1]
        s_4 = s_all - s_2 - s_3

        spider_2_list.append({"date": date, "num": s_2})
        spider_3_list.append({"date": date, "num": s_3})
        spider_4_list.append({"date": date, "num": s_4})

    res_list = [{"run": spider_2_list}, {"error": spider_3_list}, {"pause": spider_4_list}]
    j = JsonResponse(res_list, safe=False)
    return j


def get_spider_num_group_by_hour():
    # date = request.GET.get("date")
    date = "2017-09-06"
    type_ = 1
    spider_num_list = []
    for i in range(1, 7):
        spider_num = dao.get_spider_num_group_by_hour(date, type_)
        spider_num_list.append(spider_num)

    res_list = []
    for spider_num in spider_num_list:
        res = []
        index = spider_num_list.index(spider_num)+1
        for s_n in spider_num:
            i = s_n[0]
            n = s_n[1]
            res.append({"hour": i, "num": n})
        res_list.append({"type": index, "date": res})

    j = JsonResponse(res_list, safe=False)
    return j


if __name__ == '__main__':
    # get_date_to_update_spider_num()
    # update_spider_num()
    # res = dao.get_spider_num_group_by_date(3)
    # get_spider_num_group_by_date()
    get_spider_num_group_by_hour()
    pass
