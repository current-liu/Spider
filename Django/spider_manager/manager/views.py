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



