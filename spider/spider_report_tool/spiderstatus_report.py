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
# today_django = today + datetime.timedelta(hours=-8)
today_django = today
today_django_end = today + datetime.timedelta(hours=-5) + datetime.timedelta(days=5)


def get_time_django():
    today = datetime.datetime.today()
    # today_django = today + datetime.timedelta(hours=-8)
    return today


def report_spider_start(spider_id, current_time):
    status = 1
    log = "start"
    dao.insert_spider_status_start(spider_id, status, current_time, log)
    dao.update_spider_status(spider_id, status)


def report_spider_start_fix(spider_id, current_time):
    status = 1
    log = "start_fix"
    dao.insert_spider_status_start(spider_id, status, current_time, log)


# def report_spider_end(spider_id, current_time, log, start_time):
#     status = 2
#     operation_time = current_time - start_time
#     days = operation_time.days
#     seconds = operation_time.seconds
#     operation_time_str = str(days) + ":" + str(seconds)
#
#     dao.insert_spider_status_end(spider_id, status, current_time, log, operation_time_str)
#     dao.update_spider_status(spider_id, status)


def report_spider_end(spider_id, end_time, log, start_time):
    status = 2

    day_0 = start_time.day
    day_1 = end_time.day
    day_n = day_1 - day_0
    if day_n == 0:
        # 此次运行没有跨天
        # 当天运行了多少秒
        operation_time_str = get_second_from_start_to_end(start_time, end_time)
        dao.insert_spider_status_end(spider_id, status, end_time, log, operation_time_str)
        dao.update_spider_status(spider_id, 2)

    else:
        # 此次运行跨天了，在凌晨时刻前一秒，补一个结束记录;在凌晨补一个开始记录
        start_time_fix = datetime.datetime(end_time.year, end_time.month, end_time.day, 0, 0, 0)
        end_time_fix = start_time_fix + datetime.timedelta(seconds=-1)

        log_fix_end = "end_fix"

        report_spider_start_fix(spider_id, start_time_fix)

        report_spider_end(spider_id, end_time, log_fix_end, start_time_fix)

        # 递归
        report_spider_end(spider_id, end_time_fix, log_fix_end, start_time)


def report_spider_error(spider_id, end_time, log, start_time):
    report_spider_end(spider_id, end_time, log, start_time)

    dao.update_spider_status(spider_id, 3)
    dao.update_spiderstatus_status(spider_id, 3)


def get_second_from_start_to_end(start, end):
    operation_time = end - start
    seconds = operation_time.seconds
    operation_time_str = str(seconds)
    return operation_time_str


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

    start_time_fix = datetime.datetime(current_time.year, current_time.month, current_time.day, 0, 0,
                                       0) + + datetime.timedelta(seconds=-1)

    report_spider_error(spider_id, today_django_end, log, today_django)
