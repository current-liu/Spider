# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dict',
            name='value',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spider',
            name='type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spiderstatus',
            name='status',
            field=models.IntegerField(),
        ),
    ]