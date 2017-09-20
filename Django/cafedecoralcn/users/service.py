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
from .models import DpMember,OrMember,MfwMember,TaMember

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



def get_or_memberNum(request):
    id = request.GET.get("id")
    res = dao.get_or_memberNum(id)
    num = res[0][0]
    d = {"num": num}
    j = JsonResponse(d, safe=False)
    return j

def get_dp_memberNum(request):
    id = request.GET.get("id")
    res = dao.get_dp_memberNum(id)
    num = res[0][0]
    d = {"num": num}
    j = JsonResponse(d, safe=False)
    return j

def get_ta_memberNum(request):
    id = request.GET.get("id")
    res = dao.get_ta_memberNum(id)
    num = res[0][0]
    d = {"num": num}
    j = JsonResponse(d, safe=False)
    return j

def get_mfw_memberNum(request):
    id = request.GET.get("id")
    res = dao.get_mfw_memberNum(id)
    num = res[0][0]
    d = {"num": num}
    j = JsonResponse(d, safe=False)
    return j

def get_dp_memNum(request):
    id = request.GET.get("id")
    res = dao.get_dp_memNum(id)
    num = res[0][0]
    d = {"num": num}
    j = JsonResponse(d, safe=False)
    return j

def get_dp_womemNum(request):
    id = request.GET.get("id")
    res = dao.get_dp_womemNum(id)
    num = res[0][0]
    d = {"num": num}
    j = JsonResponse(d, safe=False)
    return j

def get_mfw_memNum(request):
    id = request.GET.get("id")
    res = dao.get_mfw_memNum(id)
    num = res[0][0]
    d = {"num": num}
    j = JsonResponse(d, safe=False)
    return j

def get_mfw_womemNum(request):
    id = request.GET.get("id")
    res = dao.get_mfw_womemNum(id)
    num = res[0][0]
    d = {"num": num}
    j = JsonResponse(d, safe=False)
    return j

def get_or_favorite(request):
    id = request.GET.get("id")
    res_list = dao.get_or_favorite(id)
    length = res_list.__len__()
    shop_list = []
    for i in range(0, length):
        res = res_list[i]
        favoritr = res[0]
        d = {"favorite": favoritr}
        shop_list.append({"shop": d})
    j = JsonResponse(shop_list, safe=False)
    return j

def get_or_location(request):
    id = request.GET.get("id")
    res_list = dao.get_or_location(id)
    length = res_list.__len__()
    shop_list = []
    for i in range(0, length):
        res = res_list[i]
        favoritr = res[0]
        d = {"favorite": favoritr}
        shop_list.append({"shop": d})
    j = JsonResponse(shop_list, safe=False)
    return j

def get_dp_location(request):
    id = request.GET.get("id")
    res_list = dao.get_dp_location(id)
    length = res_list.__len__()
    shop_list = []
    for i in range(0, length):
        res = res_list[i]
        favoritr = res[0]
        d = {"favorite": favoritr}
        shop_list.append({"shop": d})
    j = JsonResponse(shop_list, safe=False)
    return j

def get_ta_location(request):
    id = request.GET.get("id")
    res_list = dao.get_ta_location(id)
    length = res_list.__len__()
    shop_list = []
    for i in range(0, length):
        res = res_list[i]
        favoritr = res[0]
        d = {"favorite": favoritr}
        shop_list.append({"shop": d})
    j = JsonResponse(shop_list, safe=False)
    return j

def get_mfw_location(request):
    id = request.GET.get("id")
    res_list = dao.get_mfw_location(id)
    length = res_list.__len__()
    shop_list = []
    for i in range(0, length):
        res = res_list[i]
        favoritr = res[0]
        d = {"favorite": favoritr}
        shop_list.append({"shop": d})
    j = JsonResponse(shop_list, safe=False)
    return j