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
def sec_turn(total_sec):
    day = total_sec / 86400
    last_sec = total_sec - day * 86400
    hour = last_sec / 3600
    last_sec_1 = last_sec - hour * 3600
    minutes = last_sec_1 / 60
    sec = last_sec_1 % 60
    print 1

if __name__ == '__main__':
    # fun()
    # create_time1 = datetime.datetime.strptime(u"2000-01-01 12:00:00", '%Y-%m-%d %H:%M:%S')
    # create_time2 = datetime.datetime.strptime(u"2001-01-01 12:00:01", '%Y-%m-%d %H:%M:%S')
    # time2_1 = create_time2 - create_time1
    # print time2_1
    # for i in range(1,1):
    #     print i
    # sec_turn(100000)
    str = "qwertyuiop"
    str_sub = str[-8:-5]
    print str_sub in str
