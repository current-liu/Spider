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
    res = Spider.objects.filter(edit_time__contains=run_date)
    response = serializers.serialize("json", res)
    return HttpResponse(response, content_type="application/json")
