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


def get_spiderstatus(request):
    spider_id = request.GET.get("id")
    print "spider_id: " + str(spider_id)
    spider = Spider.objects.get(pk=spider_id)
    spiderstatus = spider.spiderstatus_set.all()
    response = serializers.serialize("json", (spiderstatus))
    return HttpResponse(response, content_type="application/json")


def get_spider_group_by_status(request):
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


def get_spider_on_month_every_day(request):
    month = request.GET.get("date")
    print ""
    spiders = Spider.objects.filter(spiderstatus__edit_time__contains=month)
    spiders_distinct = Spider.objects.filter(spiderstatus__edit_time__contains=month).distinct()
    spiders_day = spiders.filter(spiderstatus__edit_time__day=1)
    response = serializers.serialize("json", spiders_distinct)
    str_0 = unicode(response.replace("[", "").replace("]", ""))
    str_1 = unicode(response)
    # str_json = '[{' + u'"month":' + '{'+str_0 + '}},' + u'{"month1":' + '{'+str_0 + '}}]'
    str_json = '[fsafsaf]'
    # return HttpResponse(str_json, content_type="application/json")
    return JsonResponse(str_json)


def get_spider_on_year_every_month(request):
    year = request.GET.get("date")
    year = 2017
    spiders = Spider.objects.filter(spiderstatus__edit_time__year=year).distinct()
    spiders_month = SpiderStatus.objects.values("spider_id").annotate(dcount=Count(edit_time__month))
    response = serializers.serialize("json", spiders_distinct)
    str_0 = unicode(response.replace("[", "").replace("]", ""))
    str_1 = unicode(response)
    # str_json = '[{' + u'"month":' + '{'+str_0 + '}},' + u'{"month1":' + '{'+str_0 + '}}]'
    str_json = '[fsafsaf]'
    # return HttpResponse(str_json, content_type="application/json")
    return JsonResponse(str_json)


if __name__ == '__main__':
    get_spider_on_month_every_day("")
