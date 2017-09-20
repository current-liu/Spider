# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class DpShop(models.Model):
    shopId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    feature = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    star = models.IntegerField()
    taste = models.IntegerField()
    environment = models.IntegerField()
    service = models.IntegerField()
    reviewNum = models.IntegerField()
    pic = models.CharField(max_length=255)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MfwShop(models.Model):
    shopId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)
    score = models.CharField(max_length=10)
    star = models.IntegerField()
    reviewNum = models.IntegerField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class OrShop(models.Model):
    shopId = models.IntegerField(primary_key=True)
    href = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    star = models.IntegerField()
    smiley_smiley = models.IntegerField()
    smiley_ok = models.IntegerField()
    smiley_cry = models.IntegerField()
    district = models.CharField(max_length=255)
    priceRange = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    introduction = models.TextField()
    payment = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)
    businessTime = models.CharField(max_length=255)
    seatNum = models.IntegerField()
    walk = models.CharField(max_length=255)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class TaShop(models.Model):
    shopId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length=255)
    ranking = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    tag = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)
    star = models.CharField(max_length=10)
    reviewNum = models.CharField(max_length=10)
    veryGood = models.CharField(max_length=10)
    good = models.CharField(max_length=10)
    common = models.CharField(max_length=10)
    bad = models.CharField(max_length=10)
    terrible = models.CharField(max_length=10)
    pic = models.CharField(max_length=255)

    def __str__(self):
        return self.name
