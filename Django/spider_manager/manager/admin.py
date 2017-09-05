# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Spider, SpiderStatus, Dict, Project

# Register your models here.

# admin.site.register(Spider)
# admin.site.register(SpiderStatus)
# admin.site.register(Dict)


class SpiderStatusInLine(admin.TabularInline):
    model = SpiderStatus
    extra = 0


class SpiderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "project", "type", "loc", "create_time")
    fields = ["name", "create_time", "intro", "project", "target_site", "loc", "type"]
    inlines = [SpiderStatusInLine]
    list_filter = ["project"]
    search_fields = ["name"]


class SpiderInLine(admin.TabularInline):
    model = Spider
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "intro", "create_time")
    fields = ["name", "intro", "create_time"]
    inlines = [SpiderInLine]
    list_filter = ["create_time"]
    search_fields = ["name"]

class DictAdmin(admin.ModelAdmin):
    list_display = ("id", "column", "value", "label")
    fields = ["column", "value", "label"]
    list_filter = ["column"]
    search_fields = ["label"]


class SpiderStatusAdmin(admin.ModelAdmin):
    list_display = ["id", "spider_id", "status", "log", "operation_time", "edit_time"]
    fields = ["status", "log", "operation_time", "edit_time"]
    list_filter = ["spider_id", "edit_time"]
    search_fields = ["log"]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Spider, SpiderAdmin)
admin.site.register(Dict, DictAdmin)
admin.site.register(SpiderStatus, SpiderStatusAdmin)


