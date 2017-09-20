#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/9/1 0001 上午 9:31

base Info
"""

from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
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
from .models import DpShop, TaShop, OrShop, MfwShop

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


def get_dp_shops(request):
    res = DpShop.objects.filter()
    response = serializers.serialize("json", res)
    return HttpResponse(response, content_type="application/json")



def get_dp_star(request):
    star = request.GET.get("star")
    spiders = DpShop.objects.values("shopId", "name", "star", "taste", "environment", "service").get(shopId=559195)
    res = (spiders,)
    j = JsonResponse(res, safe=False)
    return j




def selete_shop_all_star(request):
    all_star = request.GET.get("all_star")
    res = dao.selete_shop_all_star()
    shopId = res[0][0]
    name = res[0][1]
    star = res[0][2]
    taste = res[0][3]
    environment = res[0][4]
    service = res[0][5]
    d = {"shopId": shopId, "name": name, "star": star, "taste": taste, "environment": environment, "service": service}
    j = JsonResponse(d, safe=False)
    return j


def selete_shop_all(request):

    res_list = dao.selete_shop_all()
    length = res_list.__len__()
    shop_list = []
    for i in range(0, length):
        res = res_list[i]
        id = res[0]
        shopName = res[1]
        o_r = res[2]
        mfw = res[3]
        ta = res[4]
        dp = res[5]
        d = {"id": id, "shopName": shopName, "o_r": o_r, "dp": dp, "mfw": mfw, "ta": ta}
        shop_list.append({"shop": d})
    j = JsonResponse(shop_list, safe=False)
    return j


def get_all_shop_info(request):

    pass