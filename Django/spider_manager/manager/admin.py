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
    fields = ["name", "create_time", "intro", "project", "target_site", "type"]
    inlines = [SpiderStatusInLine]
    list_display = ("name", "project", "type", "create_time")
    list_filter = ["project"]
    search_fields = ["name"]


class SpiderInLine(admin.TabularInline):
    model = Spider
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    fields = ["name", "intro", "create_time"]
    inlines = [SpiderInLine]
    list_display = ("name", "intro", "create_time")
    list_filter = ["create_time"]
    search_fields = ["name"]

class DictAdmin(admin.ModelAdmin):
    fields = ["column", "value", "label"]
    list_display = ("column", "value", "label")
    list_filter = ["column"]
    search_fields = ["label"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Spider, SpiderAdmin)
admin.site.register(Dict, DictAdmin)


