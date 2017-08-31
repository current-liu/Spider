# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Spider(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    intro = models.TextField()
    project = models.CharField(max_length=100)
    target_site = models.CharField(max_length=200)
    type = models.IntegerField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class SpiderStatus(models.Model):
    spider = models.ForeignKey(Spider, on_delete=models.CASCADE)
    loc = models.CharField(max_length=200)
    status = models.IntegerField()
    log = models.TextField()
    edit_time = models.DateTimeField()

    def __str__(self):
        return str(self.status)


@python_2_unicode_compatible
class Dict(models.Model):
    table = models.CharField(max_length=20)
    column = models.CharField(max_length=20)
    value = models.IntegerField()
    label = models.CharField(max_length=20)

    def __str__(self):
        return str(self.table + "." + self.column)
