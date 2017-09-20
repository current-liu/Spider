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
from django.core import serializers
import datetime
import json
import dao
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import TruncYear, TruncMonth, TruncDay, TruncHour
import calendar

__author__ = 'liuchao'
__version__ = '1.0'


def ajax(request):
    n = request.GET.get("id")
    print n
    ret = {'status': True, 'error': "null"}
    l = [1, 2, 3, 4, 5]
    r = {"l": n}
    # a = ["123", "456"]

    return JsonResponse(r)

def get_or_reviewNum(request):
    id = request.GET.get(get_all_id().o_r)
    res = dao.get_or_reviewNum(id)
    num = res[0][0]
    d = {"num":num}
    j = JsonResponse(d, safe=False)
    return j

def get_dp_reviewNum(request):
    id = request.GET.get("id")
    res = dao.get_dp_reviewNum(id)
    num = res[0][0]
    d = {"num":num}
    j = JsonResponse(d, safe=False)
    return j

def get_ta_reviewNum(request):
    id = request.GET.get("id")
    res = dao.get_ta_reviewNum(id)
    num = res[0][0]
    d = {"num":num}
    j = JsonResponse(d, safe=False)
    return j

def get_mfw_reviewNum(request):
    id = request.GET.get("id")
    res = dao.get_mfw_reviewNum(id)
    num = res[0][0]
    d = {"num":num}
    j = JsonResponse(d, safe=False)
    return j

def get_all_id(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    o_r = res[0][0]
    mfw = res[0][1]
    td = res[0][2]
    dp = res[0][3]
    or_num = dao.get_or_reviewNum(o_r)
    mfw_num = dao.get_mfw_reviewNum(mfw)
    td_num = dao.get_ta_reviewNum(td)
    dp_num = dao.get_dp_reviewNum(dp)
    o = or_num[0][0]
    m = mfw_num[0][0]
    t = td_num[0][0]
    d = dp_num[0][0]
    w = {"o":o,"m":m,"t":t,"d":d}
    j = JsonResponse(w,safe=False)
    return j




