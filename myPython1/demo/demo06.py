#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/17 0017 下午 2:21

base Info
"""
import datetime
__author__ = 'Administrator'
__version__ = '1.0'


today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")
print "%s" % today

print 1|0

# def fun():
#     try:
#         lis = [1, 2, 3, 4]
#     except BaseException, e:
#         print e
#
# for n in range(3):
#     x = len(lis)
#     y = lis.__len__()
#     print next(lis)

if __name__ == '__main__':
    # fun()
    create_time1 = datetime.datetime.strptime(u"2000-01-01 12:00:00", '%Y-%m-%d %H:%M:%S')
    create_time2 = datetime.datetime.strptime(u"2001-01-01 12:00:01", '%Y-%m-%d %H:%M:%S')
    time2_1 = create_time2 - create_time1
    print time2_1