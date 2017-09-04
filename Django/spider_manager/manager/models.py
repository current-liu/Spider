# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=50)
    intro = models.TextField()
    create_time = models.DateTimeField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Spider(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    intro = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    target_site = models.CharField(max_length=500)
    type = models.IntegerField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class SpiderStatus(models.Model):
    spider = models.ForeignKey(Spider, on_delete=models.CASCADE)
    loc = models.CharField(max_length=200)
    status = models.IntegerField()
    log = models.TextField()
    operation_time = models.DateTimeField()
    edit_time = models.DateTimeField()

    def __str__(self):
        return str(self.status)


@python_2_unicode_compatible
class Dict(models.Model):

    column = models.CharField(max_length=20)
    value = models.IntegerField()
    label = models.CharField(max_length=20)

    def __str__(self):
        return str(self.column + "." + str(self.value) + "." + self.label)
