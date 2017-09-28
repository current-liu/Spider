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
import dao, dao_lc
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


def get_all_shop_appraise(request):
    # 0:全部;1：大陆；2:香港
    area = str(request.GET.get("area"))
    res = dao_lc.get_all_shop_ids()
    shop_appraise_list = []
    for r in res:
        shop_appraise = get_star_and_more_by_id(r)
        if area == "0":
            shop_appraise_0 = shop_appraise
            del shop_appraise_0["star_hk"]
            del shop_appraise_0["star_main"]
            shop_appraise_list.append(shop_appraise_0)

        elif area == "1":
            shop_appraise_1 = shop_appraise
            star_1 = shop_appraise_1["star_main"]
            if star_1 != -1:
                del shop_appraise_1["star_hk"]
                del shop_appraise_1["star_all"]
                shop_appraise_list.append(shop_appraise_1)

        elif area == "2":
            shop_appraise_2 = shop_appraise
            star_2 = shop_appraise_2["star_hk"]
            if star_2 != -1:
                id = shop_appraise_2["id"]
                name = shop_appraise_2["name"]
                shop_appraise_list.append({"id": id, "name": name, "star_hk": star_2})
        else:
            shop_appraise_list.append({"name": "area error not in 0、1、2"})

    j = JsonResponse(shop_appraise_list, safe=False)
    return j


def get_star_and_more_by_id(shop_ids_in_4_pla):
    """没有的平台，id应传入0"""

    id = shop_ids_in_4_pla[0]
    print id
    name = shop_ids_in_4_pla[1]
    # 大陆
    dp = shop_ids_in_4_pla[2]
    mfw = shop_ids_in_4_pla[4]

    # 香港
    o_r = shop_ids_in_4_pla[3]
    ta = shop_ids_in_4_pla[5]

    star_list_hk = []
    if o_r != 0:
        star_or_str = dao_lc.get_shop_star_from_pla("or", o_r)[0][0]
        star_or = float(star_or_str)
        if star_or > 0:
            star_list_hk.append(star_or)
    if ta != 0:
        star_ta = float(dao_lc.get_shop_star_from_pla("ta", ta)[0][0])
        if star_ta > 0:
            star_list_hk.append(star_ta)

    star_list_main = []
    if mfw != 0:
        star_mfw_str = dao_lc.get_shop_star_from_pla("mfw", mfw)
        star_mfw = float(star_mfw_str[0][0])
        if star_mfw > 0:
            star_list_main.append(star_mfw)

    taste = -1
    environment = -1
    service = -1
    if dp != 0:
        dp_star_and_more = dao_lc.get_shop_star_and_more_from_dp(dp)[0]
        star_dp = float(dp_star_and_more[0])
        taste = dp_star_and_more[1]
        environment = dp_star_and_more[2]
        service = dp_star_and_more[3]
        if star_dp > 0:
            star_list_main.append(star_dp)

    num_hk = star_list_hk.__len__()
    star_total_hk = 0
    if num_hk == 0:
        star_avg_hk = -1
    else:
        for i in range(0, num_hk):
            star_total_hk += star_list_hk[i]
        star_avg_hk = star_total_hk / num_hk

    num_main = star_list_main.__len__()
    star_total_main = 0
    if num_main == 0:
        star_avg_main = -1
    else:
        for i in range(0, num_main):
            star_total_main += star_list_main[i]
        star_avg_main = star_total_main / num_main

    star_total_all = star_total_hk + star_total_main
    num_all = num_hk + num_main
    if num_all == 0:
        star_avg_all = -1
    else:
        star_avg_all = star_total_all / num_all

    shop_appraise = {"id": id, "name": name, "star_all": star_avg_all, "star_hk": star_avg_hk,
                     "star_main": star_avg_main, "taste_main": taste, "envir_main": environment,
                     "service_main": service}
    return shop_appraise


def selete_shop_all_info(request):
    id = request.GET.get("id")
    # id = r[0]
    # print id
    # name = r[1]
    # # 大陆
    # dp = r[2]
    # mfw = r[4]
    #
    # # 香港
    # o_r = r[3]
    # ta = r[5]

    idd_list = dao.get_all_id(id)
    idd = idd_list[0]
    dp =idd[4]
    o_r =idd[1]
    mfw =idd[2]
    ta = idd[3]
    res_list = dao.selete_shop_all_info(id)
    res = res_list[0]
    name = res[1]
    addr = res[2]
    tel = res[3]

    id_list = [id, "", dp, o_r, mfw, ta]
    shop_appraise = get_star_and_more_by_id(id_list)
    star = shop_appraise["star_all"]


    if o_r != 0:
        picture = dao.selete_or_pic(o_r)
        pic = picture[0][0]
    elif mfw != 0:
        picture = dao.selete_mfw_pic(mfw)
        pic = picture[0][0]
    elif ta != 0:
        picture = dao.selete_ta_pic(ta)
        pic = picture[0][0]
    elif dp != 0:
        picture = dao.selete_dp_pic(dp)
        pic = picture[0][0]
    else:
        pic = -1


    d = {"name": name, "addr": addr, "tel": tel, "star": star, "pic":pic}
    j = JsonResponse(d, safe=False)
    return j
