# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20170921_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tashop',
            name='star',
            field=models.IntegerField(),
        ),
    ]
