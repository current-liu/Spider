# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DpReview',
            fields=[
                ('reviewId', models.IntegerField(primary_key=True, serialize=False)),
                ('memberId', models.IntegerField()),
                ('shopId', models.IntegerField()),
                ('star', models.CharField(max_length=10)),
                ('taste', models.IntegerField()),
                ('environment', models.IntegerField()),
                ('service', models.IntegerField()),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('likes', models.IntegerField()),
                ('reply', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MfwReview',
            fields=[
                ('reviewId', models.IntegerField(primary_key=True, serialize=False)),
                ('memberId', models.IntegerField()),
                ('shopId', models.IntegerField()),
                ('star', models.IntegerField()),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
                ('likes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrReview',
            fields=[
                ('reviewId', models.IntegerField(primary_key=True, serialize=False)),
                ('shopId', models.IntegerField()),
                ('time', models.DateField()),
                ('views', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('memberId', models.IntegerField()),
                ('memberName', models.CharField(max_length=20)),
                ('smiley', models.CharField(max_length=10)),
                ('taste', models.IntegerField()),
                ('environment', models.IntegerField()),
                ('services', models.IntegerField()),
                ('health', models.IntegerField()),
                ('quality', models.IntegerField()),
                ('mealdate', models.DateField()),
                ('diningpathway', models.CharField(max_length=20)),
                ('consumption', models.CharField(max_length=50)),
                ('recommend', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TaReview',
            fields=[
                ('reviewId', models.IntegerField(primary_key=True, serialize=False)),
                ('memberId', models.IntegerField()),
                ('memberName', models.CharField(max_length=255)),
                ('shopId', models.IntegerField()),
                ('star', models.IntegerField()),
                ('title', models.IntegerField()),
                ('content', models.TextField()),
                ('time', models.DateField()),
            ],
        ),
    ]
