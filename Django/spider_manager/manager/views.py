# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.utils import timezone
from .models import Spider
from pandas import json


# Create your views here.


def index(request):
    return HttpResponse("You are at the manager index.")


class IndexView(generic.ListView):
    template_name = "manager/index.html"
    context_object_name = "latest_spider_list"

    def get_queryset(self):
        # return Spider.objects.order_by("-pub_date")[:5]
        return Spider.objects.order_by("-create_time")[:5]


def ajax(request):
    n = request.GET.get("id")
    print n
    ret = {'status': True, 'error': "null"}
    l = [1, 2, 3, 4, 5]
    r = {"l": n}
    # a = ["123", "456"]
    j_ret = json.dumps(ret)
    return JsonResponse(r)
    return HttpResponse(j_ret)
