#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/9/5 0005 下午 1:39

base Info
"""
import dao
import datetime

__author__ = 'liuchao'
__version__ = '1.0'

today = datetime.datetime.today()
today_django = today + datetime.timedelta(hours=-8)
today_django_end = today + datetime.timedelta(hours=-5) + datetime.timedelta(days=5)


def get_time_django():
    today = datetime.datetime.today()
    today_django = today + datetime.timedelta(hours=-8)
    return today_django


def report_spider_start(spider_id, current_time):
    status = 1
    dao.insert_spider_status_start(spider_id, status, current_time)
    dao.update_spider_status(spider_id, status)


def report_spider_end(spider_id, current_time, log, start_time):
    status = 2
    operation_time = current_time - start_time
    days = operation_time.days
    seconds = operation_time.seconds
    operation_time_str = str(days)+":"+str(seconds)

    dao.insert_spider_status_end(spider_id, status, current_time, log, operation_time_str)
    dao.update_spider_status(spider_id, status)

def report_spider_error(spider_id, current_time, log, start_time):
    status = 3
    operation_time = current_time - start_time
    days = operation_time.days
    seconds = operation_time.seconds
    operation_time_str = str(days) + ":" + str(seconds)
    dao.insert_spider_status_end(spider_id, status, current_time, log, operation_time_str)
    dao.update_spider_status(spider_id, status)

if __name__ == '__main__':
    status = 1
    spider_id = 1
    current_time = today_django
    # dao.insert_spider_status_start(spider_id, status, edit_time)

    log = "complete"
    operation_time = today_django_end - today_django
    # dao.insert_spider_status_end(spider_id, status, current_time, log, operation_time)

    qqq = today_django_end - today_django_end
    s = operation_time.seconds
    m = operation_time.days
    print qqq
