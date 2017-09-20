# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class DpMember(models.Model):
    memberId = models.IntegerField(primary_key=True)
    pic = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    contribution = models.IntegerField()
    contrReview = models.CharField(max_length=20)
    contrShop = models.CharField(max_length=20)
    contrPic = models.CharField(max_length=20)
    contrInfo = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    levels = models.CharField(max_length=255)
    regtime = models.CharField(max_length=255)
    follows = models.IntegerField()
    fans = models.IntegerField()
    interactive = models.IntegerField()
    review = models.IntegerField()
    favourite = models.IntegerField()
    checkin = models.IntegerField()
    picture = models.IntegerField()
    mylist = models.IntegerField()
    post = models.IntegerField()
    birthday = models.CharField(max_length=50)
    loveState = models.CharField(max_length=50)
    jobs = models.CharField(max_length=50)
    birthplace = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MfwMember(models.Model):
    memberId = models.IntegerField(primary_key=True)
    pic = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=20)
    vip = models.IntegerField()
    duo = models.IntegerField()
    zhiluren = models.IntegerField()
    location = models.CharField(max_length=50)
    level = models.IntegerField()
    follows = models.IntegerField()
    fans = models.IntegerField()
    profile = models.TextField()
    review = models.CharField(max_length=225)
    contribution = models.CharField(max_length=225)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class OrMember(models.Model):
    memberId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    badge = models.CharField(max_length=20)
    follows = models.IntegerField()
    fans = models.IntegerField()
    reviewNum = models.IntegerField()
    regtime = models.CharField(max_length=50)
    actionZone = models.CharField(max_length=100)
    workPlace = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    favorite = models.CharField(max_length=255)
    firWritten = models.IntegerField()
    pic = models.CharField(max_length=255)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class TaMember(models.Model):
    memberId = models.IntegerField(primary_key=True)
    pic = models.CharField(max_length=225)
    name = models.CharField(max_length=100)
    regtime = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    photos = models.CharField(max_length=10)
    potints = models.CharField(max_length=10)
    levels = models.CharField(max_length=10)
    badges = models.CharField(max_length=10)

    def __str__(self):
        return self.name
