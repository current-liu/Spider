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
import jieba
import nltk
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



# def get_or_reviewNum(request):
#     id = request.GET.get(get_all_id().o_r)
#     res = dao.get_or_reviewNum(id)
#     num = res[0][0]
#     d = {"num":num}
#     j = JsonResponse(d, safe=False)
#     return j
#
# def get_dp_reviewNum(request):
#     id = request.GET.get("id")
#     res = dao.get_dp_reviewNum(id)
#     num = res[0][0]
#     d = {"num":num}
#     j = JsonResponse(d, safe=False)
#     return j
#
# def get_ta_reviewNum(request):
#     id = request.GET.get("id")
#     res = dao.get_ta_reviewNum(id)
#     num = res[0][0]
#     d = {"num":num}
#     j = JsonResponse(d, safe=False)
#     return j
#
# def get_mfw_reviewNum(request):
#     id = request.GET.get("id")
#     res = dao.get_mfw_reviewNum(id)
#     num = res[0][0]
#     d = {"num":num}
#     j = JsonResponse(d, safe=False)
#     return j


def get_all_id(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    o_r = res[0][1]
    if o_r is None:
        o = 0
    else:
        or_num = dao.get_or_reviewNum(o_r)
        o = or_num[0][0]
    mfw = res[0][2]
    if mfw is None:
        m = 0
    else:
        mfw_num = dao.get_mfw_reviewNum(mfw)
        m = mfw_num[0][0]
    td = res[0][3]
    if td is None:
        t = 0
    else:
        td_num = dao.get_ta_reviewNum(td)
        t = td_num[0][0]
    dp = res[0][4]
    if dp is None:
        d = 0
    else:
        dp_num = dao.get_dp_reviewNum(dp)
        d = dp_num[0][0]
    w = {"o": o, "m": m, "t": t, "d": d}
    j = JsonResponse(w, safe=False)
    return j



def get_ta_review(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    ta = res[0][3]
    if ta is None:
        f = 0
        d = {"f": f}
        j = JsonResponse(d, safe=False)
        return j
    else:
        res_list = dao.get_ta_review(ta)
        length = res_list.__len__()
        review_list = ""
        for i in range(0, length):
            res = res_list[i]
            f = res[0]
            review_list += f
        strs = str(review_list).replace("，","").replace("。","").replace(" ","").replace(",","").replace("的","").replace("！","").replace("是","").replace("了","").replace("有","").replace("、","").replace(".","")
        text1 = jieba.cut_for_search(strs)
        fd = nltk.FreqDist(text1)
        keys = fd.keys()
        item = fd.iteritems()
        print ' '.join(keys)
        dicts = dict(item)
        sort_dict = sorted(dicts.iteritems(), key=lambda d: d[1], reverse=True)
        k_v = []
        for i in range(0, sort_dict.__len__()):
            k = sort_dict[i][0]
            v = sort_dict[i][1]
            k_v.append({"k": k, "v": v})
        print sort_dict

    j = JsonResponse(k_v, safe=False)
    return j

def get_or_review(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    ta = res[0][1]
    if ta is None:
        f = 0
        d = {"f": f}
        j = JsonResponse(d, safe=False)
        return j
    else:
        res_list = dao.get_or_review(ta)
        length = res_list.__len__()
        review_list = ""
        for i in range(0, length):
            res = res_list[i]
            f = res[0]
            review_list += f
        strs = str(review_list).replace("，","").replace("。","").replace(" ","").replace(",","").replace("的","").replace("！","").replace("是","").replace("了","").replace("有","").replace("、","").replace(".","")
        text1 = jieba.cut_for_search(strs)
        fd = nltk.FreqDist(text1)
        keys = fd.keys()
        item = fd.iteritems()
        print ' '.join(keys)
        dicts = dict(item)
        sort_dict = sorted(dicts.iteritems(), key=lambda d: d[1], reverse=True)
        k_v = []
        for i in range(0, sort_dict.__len__()):
            k = sort_dict[i][0]
            v = sort_dict[i][1]
            k_v.append({"k": k, "v": v})
        print sort_dict

    j = JsonResponse(k_v, safe=False)
    return j

def get_dp_review(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    ta = res[0][4]
    if ta is None:
        f = 0
        d = {"f": f}
        j = JsonResponse(d, safe=False)
        return j
    else:
        res_list = dao.get_dp_review(ta)
        length = res_list.__len__()
        review_list = ""
        for i in range(0, length):
            res = res_list[i]
            f = res[0]
            review_list += f
        strs = str(review_list).replace("，","").replace("。","").replace(" ","").replace(",","").replace("的","").replace("！","").replace("是","").replace("了","").replace("有","").replace("、","").replace(".","")
        text1 = jieba.cut_for_search(strs)
        fd = nltk.FreqDist(text1)
        keys = fd.keys()
        item = fd.iteritems()
        print ' '.join(keys)
        dicts = dict(item)
        sort_dict = sorted(dicts.iteritems(), key=lambda d: d[1], reverse=True)
        k_v = []
        for i in range(0, sort_dict.__len__()):
            k = sort_dict[i][0]
            v = sort_dict[i][1]
            k_v.append({"k": k, "v": v})
        print sort_dict

    j = JsonResponse(k_v, safe=False)
    return j

def get_mfw_review(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    ta = res[0][2]
    if ta is None:
        f = 0
        d = {"f": f}
        j = JsonResponse(d, safe=False)
        return j
    else:
        res_list = dao.get_mfw_review(ta)
        length = res_list.__len__()
        review_list = ""
        for i in range(0, length):
            res = res_list[i]
            f = res[0]
            review_list += f
        strs = str(review_list).replace("，","").replace("。","").replace(" ","").replace(",","").replace("的","").replace("！","").replace("是","").replace("了","").replace("有","").replace("、","").replace(".","")
        text1 = jieba.cut_for_search(strs)
        fd = nltk.FreqDist(text1)
        keys = fd.keys()
        item = fd.iteritems()
        print ' '.join(keys)
        dicts = dict(item)
        sort_dict = sorted(dicts.iteritems(), key=lambda d: d[1], reverse=True)
        k_v = []
        for i in range(0, sort_dict.__len__()):
            k = sort_dict[i][0]
            v = sort_dict[i][1]
            k_v.append({"k": k, "v": v})
        print sort_dict

    j = JsonResponse(k_v, safe=False)
    return j

def get_all_reviewNum(request):
    id = request.GET.get("id")
    res = dao.get_all_id(id)
    o_r = res[0][1]
    or_list = []
    if o_r is None:
        or_month = 0
        or_list = {or_month}
    else:
        or_num = dao.get_or_month_review(o_r)
        for i in range(0, or_num.__len__()):
            or_month = or_num[i][0]
            or_list.append(or_month)
    mfw = res[0][2]
    mfw_list = []
    if mfw is None:
        mfw_month = 0
        mfw_list = { mfw_month}
    else:
        mfw_num = dao.get_mfw_month_review(mfw)
        for i in range(0, mfw_num.__len__()):
            mfw_month = mfw_num[i][0]
            mfw_list.append(mfw_month)
    ta = res[0][3]
    ta_list = []
    if ta is None:
        ta_month = 0
        ta_list = {ta_month}
    else:
        ta_num = dao.get_ta_month_review(ta)
        for i in range(0, ta_num.__len__()):
            ta_month = ta_num[i][0]
            ta_list.append(ta_month)
    dp = res[0][4]
    dp_list = []
    if dp is None:
        dp_month = 0
        dp_list = {dp_month}
    else:
        dp_num = dao.get_dp_month_review(dp)
        for i in range(0, dp_num.__len__()):
            dp_month = dp_num[i][0]
            dp_list.append(dp_month)
    all_list = dp_list + ta_list + or_list + mfw_list
    fav_stat = {}
    for i in range(0, all_list.__len__()):
        x = all_list[i]
        try:
            n = fav_stat[x]
            fav_stat[x] = n + 1
        except Exception, e:
            fav_stat[x] = 1

    dict = sorted(fav_stat.items(), key=lambda e: e[0])
    favorite_list = []
    for i in range(0, dict.__len__()):
        obj = dict[i]
        key = obj[0]
        value = obj[1]
        d = {"k": key, "v": value}
        favorite_list.append(d)
    j = JsonResponse(favorite_list, safe=False)
    return j

