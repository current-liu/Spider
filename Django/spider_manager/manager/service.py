#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/9/1 0001 上午 9:31

base Info
"""

from __future__ import unicode_literals

from django.db.models import QuerySet, Count
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.utils import timezone
from .models import Spider, Project, SpiderStatus, Dict
from django.core import serializers
import datetime
import pdb
import json
import dao
from django.utils import timezone

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import TruncYear, TruncMonth, TruncDay, TruncHour
import calendar

__author__ = 'liuchao'
__version__ = '1.0'


def ajax(request):
    # pdb.set_trace()
    n = request.GET.get("id")
    print n
    ret = {'status': True, 'error': "null"}
    l = [1, 2, 3, 4, 5]
    r = {"l": n}
    # a = ["123", "456"]

    return JsonResponse(r)


def get_projects(request):
    p = Project.objects.order_by("-create_time")
    response = serializers.serialize("json", p)
    return HttpResponse(response, content_type="application/json")


def get_spiders_in_project(request):
    project_id = request.GET.get("id")
    print "project_id: " + str(project_id)

    spiders = Spider.objects.filter(project_id=project_id)
    response = serializers.serialize("json", spiders)

    return HttpResponse(response, content_type="application/json")


def get_project(request):
    project_id = request.GET.get("id")
    print "project_id: " + str(project_id)
    project = Project.objects.get(pk=project_id)
    projects = (project,)
    response = serializers.serialize("json", projects)
    return HttpResponse(response, content_type="application/json")
    # return JsonResponse(project)


def get_spider(request):
    spider_id = request.GET.get("id")
    print "spider_id: " + str(spider_id)
    spider = Spider.objects.get(pk=spider_id)
    response = serializers.serialize("json", (spider,))
    return HttpResponse(response, content_type="application/json")


def get_spiders(request):
    spiders = Spider.objects.order_by("-create_time")
    response = serializers.serialize("json", spiders)
    return HttpResponse(response, content_type="application/json")


def get_spiderstatus_last(request):
    spider_id = request.GET.get("id")
    print "spider_id: " + str(spider_id)
    spider = Spider.objects.get(pk=spider_id)
    spiderstatus = spider.spiderstatus_set.order_by("-edit_time")[:1]

    response = serializers.serialize("json", spiderstatus)
    return HttpResponse(response, content_type="application/json")


def get_spiderstatus_today(request):
    spider_id = request.GET.get("id")
    print "spider_id: " + str(spider_id)
    spider = Spider.objects.get(pk=spider_id)
    spiderstatus = spider.spiderstatus_set.filter(edit_time__gte=datetime.date.today())
    response = serializers.serialize("json", spiderstatus)
    return HttpResponse(response, content_type="application/json")


def get_spiderstatus_on_day(request):
    spider_id = request.GET.get("id")
    log_date = request.GET.get("date")
    print "spider_id: " + str(spider_id)
    spider = Spider.objects.get(pk=spider_id)
    spiderstatus = spider.spiderstatus_set.filter(edit_time__date=log_date)
    response = serializers.serialize("json", spiderstatus)
    return HttpResponse(response, content_type="application/json")


def get_spiderstatus(request):
    spider_id = request.GET.get("id")
    print "spider_id: " + str(spider_id)
    spider = Spider.objects.get(pk=spider_id)
    spiderstatus = spider.spiderstatus_set.all()
    response = serializers.serialize("json", (spiderstatus))
    return HttpResponse(response, content_type="application/json")


def get_spider_group_on_status(request):
    status = request.GET.get("status")
    res = Spider.objects.filter(status=status)
    response = serializers.serialize("json", res)
    return HttpResponse(response, content_type="application/json")


def get_spider_on_date(request):
    run_date = request.GET.get("date")
    print run_date
    results = dao.get_spider_id_on_date(run_date)
    id_list = []
    for res in results:
        id_list.append(res[0])
    res = Spider.objects.filter(id__in=id_list)
    response = serializers.serialize("json", res)
    return HttpResponse(response, content_type="application/json")


def get_error_spider_on_date(request):
    run_date = request.GET.get("date")
    print run_date
    results = dao.get_error_spider_id_on_date(run_date)
    id_list = []
    for res in results:
        id_list.append(res[0])
    res = Spider.objects.filter(id__in=id_list)
    response = serializers.serialize("json", res)
    return HttpResponse(response, content_type="application/json")


def get_spider_on_day_every_hour(request):
    # TODO按hour查会出错
    # TODO按状态，按类别还没加
    date = str(request.GET.get("date"))
    date_str = date.split("-")
    year = date_str[0]
    month = date_str[1]
    day = date_str[2]
    status = request.GET.get("status")
    type_id = request.GET.get("type")

    print date
    print status, type_id

    spiders = Spider.objects.filter()

    if date is None:
        pass
    else:
        spiders = spiders.filter(spiderstatus__edit_time__year=year, spiderstatus__edit_time__month=month,
                                 spiderstatus__edit_time__day=day)

    # debug
    r = serializers.serialize("json", spiders)
    h_r = HttpResponse(r, content_type="application/json")

    if status is None:
        pass
    else:
        spiders = spiders.filter(spiderstatus__status=status)
    if type_id is None:
        pass
    else:
        spiders = spiders.filter(type=type_id)

    res_list = []
    for i in range(0, 24):
        spiders_num = {"hour": i, "num": 0}
        res_list.append(spiders_num)

    # for i in range(0, 24):
    #     key = "hour" + str(i)
    #     spiders_f = spiders.filter(spiderstatus__edit_time__hour=i)
    #     r_1 = serializers.serialize("json", spiders)
    #     h_r_1 = HttpResponse(r_1, content_type="application/json")
    #     spiders_i = spiders_f.distinct().count()
    #     spiders_num[key] = spiders_i

    # res = SpiderStatus.objects.filter(edit_time__date=date).values('spider_id').distinct().annotate(hour=TruncHour('edit_time')).values('hour').annotate(num=Count('id')).values('num', 'hour').order_by('hour')
    res = dao.get_spider_on_day_every_hour(date)
    for r in res:
        res_list[r[0]]["num"] = r[1]
    return JsonResponse(res_list, safe=False)


def get_spider_on_month_every_day(request):
    date = str(request.GET.get("date"))
    year = date.split("-")[0]
    month = date.split("-")[1]
    status = request.GET.get("status")
    type_id = request.GET.get("type")

    print date
    print status, type_id

    spiders = Spider.objects.filter()

    if date is None:
        pass
    else:
        spiders = spiders.filter(spiderstatus__edit_time__year=year, spiderstatus__edit_time__month=month)
    if status is None:
        print str(status)
    else:
        spiders = spiders.filter(spiderstatus__status=status)
    if type_id is None:
        pass
    else:
        spiders = spiders.filter(type=type_id)

    res = calendar.monthrange(int(year), int(month))
    days_on_month = res[1]
    spiders_num_list = []
    for i in range(1, days_on_month + 1):
        spiders_i = spiders.filter(spiderstatus__edit_time__day=i).distinct().count()
        spiders_num = {"num": spiders_i, "day": i}
        spiders_num_list.append(spiders_num)

    return JsonResponse(spiders_num_list, safe=False)


def get_spider_on_year_every_month(request):
    year = request.GET.get("date")
    status = request.GET.get("status")
    type_id = request.GET.get("type")

    print year
    print status, type_id

    spiders = Spider.objects.filter()

    if year is None:
        pass
    else:
        spiders = spiders.filter(spiderstatus__edit_time__year=year)

    if status is None:
        print str(status)
    else:
        spiders = spiders.filter(spiderstatus__status=status)

    if type_id is None:
        pass
    else:
        spiders = spiders.filter(type=type_id)

    # response = serializers.serialize("json", res)
    # return HttpResponse(response, content_type="application/json")
    spiders_num_list = []
    for i in range(1, 13):
        spiders_i = spiders.filter(spiderstatus__edit_time__month=i).distinct().count()
        # spiders_num[key] = spiders_i
        spiders_num = {"num": spiders_i, "month": i}
        spiders_num_list.append(spiders_num)

    # res = SpiderStatus.objects.filter(edit_time__year=year).annotate(month=TruncMonth('edit_time')).values(
    #     'month').annotate(num=Count('id')).values('num', 'month').order_by('month')
    #
    # spider_json = json.dumps(list(res), cls=DjangoJSONEncoder)
    # return JsonResponse(spider_json, safe=False)
    # return HttpResponse(spider_json, content_type="application/json")
    return JsonResponse(spiders_num_list, safe=False)


def get_operation_time_last_n_days(request):
    """每天的时间累加"""
    spider_id = request.GET.get("id")
    n = int(request.GET.get("n"))
    today = datetime.datetime.today()
    res_list = []
    for i in range(0, n):
        time_search = today + datetime.timedelta(days=-i)
        year = time_search.year
        month = time_search.month
        day = time_search.day
        operation_time_list = SpiderStatus.objects.filter(spider_id=spider_id, edit_time__year=year,
                                                          edit_time__month=month, edit_time__day=day).values_list(
            "operation_time")

        total_sec = 0
        for op_time in operation_time_list:
            try:
                total_sec += int(op_time[0])
            except BaseException, e:
                print e

        hour = total_sec / 3600
        last_sec = total_sec - hour * 3600
        minutes = last_sec / 60
        sec = last_sec % 60

        full_seconds = 86400
        operation_time_seconds = total_sec
        leisure_seconds = full_seconds - operation_time_seconds

        operation_time = {"hour": hour, "minutes": minutes, "sec": sec,
                          "operation_time_seconds": operation_time_seconds, "leisure_seconds": leisure_seconds}
        date = str(year) + "-" + str(month) + "-" + str(day)
        res = {"date": date, "operation_time": operation_time}
        res_list.append(res)

    return JsonResponse(res_list, safe=False)


def get_date_to_update_spider_num():
    res = dao.get_date_to_update_spider_num()
    date_list = []
    for r in res:
        date = r[0]
        date_list.append((date, date))

    return date_list


def update_spider_num():
    # 更新截止昨天，当天系统中有多少个爬虫
    date_list = get_date_to_update_spider_num()
    dao.update_spider_num(date_list)


def get_spider_num_group_by_date(request):
    # print "get_spider_num_group_by_date"
    type_str = ""
    type_ = str(request.GET.get("type"))
    if type_ != 'None':
        type_str = " AND t.type =" + type_
    # TODO不传type时  查所有
    spiders_1 = dao.get_spider_num_group_by_date(1, type_str)
    spiders_3 = dao.get_spider_num_group_by_date(3, type_str)
    spiders_num = dao.select_spider_num_up_to_date()
    length = spiders_1.__len__()
    spider_4_list = []
    spider_1_list = []
    spider_3_list = []

    for i in range(0, length):
        date = spiders_1[i][0]
        s_1 = spiders_1[i][1]
        s_3 = spiders_3[i][1]
        s_all = spiders_num[i][1]
        s_4 = s_all - s_1

        spider_1_list.append({"d": date, "n": s_1})
        spider_3_list.append({"d": date, "n": s_3})
        spider_4_list.append({"d": date, "n": s_4})

    res_list = [{"run": spider_1_list}, {"error": spider_3_list}, {"pause": spider_4_list}]
    j = JsonResponse(res_list, safe=False)
    return j


def get_spider_num_group_by_hour(request):
    date = request.GET.get("date")
    # date = "2017-09-06"

    spider_num_list = []
    for i in range(1, 7):
        type_ = i
        spider_num = dao.get_spider_num_group_by_hour(date, type_)
        spider_num_list.append(spider_num)

    res_list = []
    # for spider_num in spider_num_list:
    for index, spider_num in enumerate(spider_num_list):
        res = []
        # index = spider_num_list.index(spider_num)
        for s_n in spider_num:
            i = s_n[0]
            n = s_n[1]
            res.append({"h": i, "n": n})
        res_list.append({"t": index+1, "d": res})

    j = JsonResponse(res_list, safe=False)
    return j


def get_spider_num_group_by_month(request):
    date = request.GET.get("date")
    # date = "2017"
    spiders_1 = dao.get_spider_num_group_by_month(date, 1)
    spiders_3 = dao.get_spider_num_group_by_month(date, 3)
    spiders_num = dao.select_spider_num_up_to_month(date)
    length = spiders_num.__len__()
    month_start = int(spiders_num[0][0].split("-")[1])
    spider_4_list = []
    spider_1_list = []
    spider_3_list = []

    for i in range(0, length):
        i_fix = i+month_start
        month = spiders_1[i_fix][0]
        s_1 = spiders_1[i_fix][1]
        s_3 = spiders_3[i_fix][1]
        s_all = spiders_num[i][1]
        s_4 = s_all - s_1

        spider_1_list.append({"m": month, "n": s_1})
        spider_3_list.append({"m": month, "n": s_3})
        spider_4_list.append({"m": month, "n": s_4})

    res_list = [{"run": spider_1_list}, {"error": spider_3_list}, {"pause": spider_4_list}]
    j = JsonResponse(res_list, safe=False)
    return j
if __name__ == '__main__':
    get_date_to_update_spider_num()
