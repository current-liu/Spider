# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Spider, SpiderStatus, Dict

# Register your models here.

# admin.site.register(Spider)
# admin.site.register(SpiderStatus)
# admin.site.register(Dict)


class SpiderStatusInLine(admin.TabularInline):
    model = SpiderStatus
    extra = 0


class SpiderAdmin(admin.ModelAdmin):
    fields = ["name", "create_time", "intro", "project", "target_site", "type"]
    inlines = [SpiderStatusInLine]
    list_display = ("name", "project", "type", "create_time")
    list_filter = ["project"]
    search_fields = ["name"]


class DictAdmin(admin.ModelAdmin):
    fields = ["table", "column", "value", "label"]
    list_display = ("table", "column", "value", "label")
    list_filter = ["table"]
    search_fields = ["label"]


admin.site.register(Spider, SpiderAdmin)
admin.site.register(Dict, DictAdmin)


