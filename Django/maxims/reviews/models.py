# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.


@python_2_unicode_compatible
class DpReview(models.Model):
    reviewId = models.IntegerField(primary_key=True)
    memberId = models.IntegerField()
    shopId = models.IntegerField()
    star = models.CharField(max_length=10)
    taste = models.IntegerField()
    environment = models.IntegerField()
    service = models.IntegerField()
    content = models.TextField()
    time = models.DateTimeField()
    location = models.CharField(max_length=255)
    likes = models.IntegerField()
    reply = models.IntegerField()

    def __str__(self):
        return self.content


@python_2_unicode_compatible
class MfwReview(models.Model):
    reviewId = models.IntegerField(primary_key=True)
    memberId = models.IntegerField()
    shopId = models.IntegerField()
    star = models.IntegerField()
    content = models.TextField()
    time = models.DateTimeField()
    likes = models.IntegerField()

    def __str__(self):
        return self.content


@python_2_unicode_compatible
class OrReview(models.Model):
    reviewId = models.IntegerField(primary_key=True)
    shopId = models.IntegerField()
    time = models.DateField()
    views = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField()
    memberId = models.IntegerField()
    memberName = models.CharField(max_length=20)
    smiley = models.CharField(max_length=10)
    taste = models.IntegerField()
    environment = models.IntegerField()
    services = models.IntegerField()
    health = models.IntegerField()
    quality = models.IntegerField()
    mealdate = models.DateField()
    diningpathway = models.CharField(max_length=20)
    consumption = models.CharField(max_length=50)
    recommend = models.IntegerField()

    def __str__(self):
        return self.content


@python_2_unicode_compatible
class TaReview(models.Model):
    reviewId = models.IntegerField(primary_key=True)
    memberId = models.IntegerField()
    memberName = models.CharField(max_length=255)
    shopId = models.IntegerField()
    star = models.IntegerField()
    title = models.IntegerField()
    content = models.TextField()
    time = models.DateField()

    def __str__(self):
        return self.content
