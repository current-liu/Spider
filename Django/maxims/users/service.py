#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/9/1 0001 上午 9:31

base Info
"""

from __future__ import unicode_literals
import re
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
from .models import DpMember, OrMember, MfwMember, TaMember

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


def get_or_location(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    shop_list = []
    o_r = res[0][1]
    if o_r is None:
        location = 0
        num = 0
        d = {"name": location,"value":num}
        shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j
    else:
        res_list = dao.get_or_location(o_r)
        length = res_list.__len__()
        for i in range(0, length):
            res = res_list[i]
            location = res[0].replace(" ","")
            num  = res[1]
            d = {"name": location,"value":num}
            shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j


def get_dp_location(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    shop_list = []
    dp = res[0][4]
    if dp is None:
        location = 0
        num = 0
        d = {"name": location,"value":num}
        shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j
    else:
        res_list = dao.get_dp_location(dp)
        length = res_list.__len__()
        for i in range(0, length):
            res = res_list[i]
            location = res[0]
            num  = res[1]
            d = {"name": location,"value":num}
            shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j


def get_ta_location(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    shop_list = []
    ta = res[0][3]
    if ta is None:
        location = 0
        num = 0
        d = {"name": location,"value":num}
        shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j
    else:
        res_list = dao.get_ta_location(ta)
        length = res_list.__len__()
        for i in range(0, length):
            res = res_list[i]
            location = res[0]
            num  = res[1]
            d = {"name": location,"value":num}
            shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j


def get_mfw_location(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    shop_list = []
    mfw = res[0][2]
    if mfw is None:
        location = 0
        num = 0
        d = {"name": location,"value":num}
        shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j
    else:
        res_list = dao.get_mfw_location(mfw)
        length = res_list.__len__()
        for i in range(0, length):
            res = res_list[i]
            location = res[0]
            num  = res[1]
            d = {"name": location,"value":num}
            shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j


def get_all_memberNum(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    o_r = res[0][1]
    if o_r is None:
        o = 0
    else:
        or_num = dao.get_or_memberNum(o_r)
        o = or_num[0][0]
    mfw = res[0][2]
    if mfw is None:
        m = 0
    else:
        mfw_num = dao.get_mfw_memberNum(mfw)
        m = mfw_num[0][0]
    td = res[0][3]
    if td is None:
        t = 0
    else:
        td_num = dao.get_ta_memberNum(td)
        t = td_num[0][0]
    dp = res[0][4]
    if dp is None:
        d = 0
    else:
        dp_num = dao.get_dp_memberNum(dp)
        d = dp_num[0][0]
    w = {"o": o, "m": m, "t": t, "d": d}
    j = JsonResponse(w, safe=False)
    return j


def get_all_sex(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    mfw = res[0][2]
    if mfw is None:
        m_w = 0
        m_m = 0
    else:
        mfw_w = dao.get_mfw_womemNum(mfw)
        mfw_m = dao.get_mfw_memNum(mfw)
        m_w = mfw_w[0][0]
        m_m = mfw_m[0][0]
    dp = res[0][4]
    if dp is None:
        d_w = 0
        d_m = 0
    else:
        dp_w = dao.get_dp_womemNum(dp)
        dp_m = dao.get_dp_memNum(dp)
        d_w = dp_w[0][0]
        d_m = dp_m[0][0]
    w = {"m_w": m_w, "m_m": m_m, "d_w": d_w, "d_m": d_m}
    j = JsonResponse(w, safe=False)
    return j


def get_or_favorite(request):
    id = request.GET.get("id")
    # id = 6
    res = dao.get_all_id(id)
    o_r = res[0][1]
    if o_r is None:
        f = 0
        d = {"f": f}
        j = JsonResponse(d, safe=False)
        return j
    else:
        res_list = dao.get_or_favorite(o_r)
        length = res_list.__len__()
        fav_stat = {}
        for i in range(0, length):
            res = res_list[i]
            f = res[0]
            f_1 = f.replace("\n", "").replace('"', "").replace('“', "").replace('”', "").replace(' ', "")
            # f_1 = "你好，a,x/s"
            f_2 = re.split('/|,|，', f_1)
            # f_2 = f_1.split("/", "，")
            for i in range(0, f_2.__len__()):
                x = f_2[i]
                try:
                    n = fav_stat[x]
                    fav_stat[x] = n + 1
                except Exception, e:
                    fav_stat[x] = 1

        # sort by value
        dict = sorted(fav_stat.items(), key=lambda e: e[1], reverse=True)
        favorite_list = []
        for i in range(0, dict.__len__()):
            obj = dict[i]
            key = obj[0]
            value = obj[1]
            d = {"k": key, "v": value}
            favorite_list.append(d)
        j = JsonResponse(favorite_list, safe=False)
        return j

def get_dp_province(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    shop_list = []
    dp = res[0][4]
    if dp is None:
        location = 0
        num = 0
        d = {"name": location,"value":num}
        shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j
    else:
        res_list = dao.get_dp_province(dp)
        length = res_list.__len__()
        for i in range(0, length):
            res = res_list[i]
            location = res[0]
            num  = res[1]
            d = {"name": location,"value":num}
            shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j

def get_mfw_province(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    shop_list = []
    mfw = res[0][2]
    if mfw is None:
        location = 0
        num = 0
        d = {"name": location,"value":num}
        shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j
    else:
        res_list = dao.get_mfw_province(mfw)
        length = res_list.__len__()
        for i in range(0, length):
            res = res_list[i]
            location = res[0]
            num  = res[1]
            d = {"name": location,"value":num}
            shop_list.append(d)
        j = JsonResponse(shop_list, safe=False)
        return j