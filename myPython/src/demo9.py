# coding=utf-8
import time
import calendar

"""
Python日期和时间
"""
"""
Python提供了一个time和calendar模块可以用于格式化日期和时间
时间间隔是以秒为单位的浮点小数，从1970年1月1日午夜算起
"""

ticks = time.time()
print ticks

# 时间元组
localtime = time.localtime(time.time())
print localtime

# 格式化的时间
asctime = time.asctime(localtime)
print asctime

# 格式化日期
print time.localtime()
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
a = "Sat Jul 08 16:38:13 2017"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
print time.strptime(a, "%a %b %d %H:%M:%S %Y")

# 获取某月日历

cal = calendar.month(2017, 7)
print cal

# Time模块函数
# time.clock()
# time.sleep()
# time.strftime()
# time.strptime()
# time.time()

print time.timezone, time.tzname

# Calendar模块函数
print calendar.calendar(2017, w=2, l=1, c=6)
print calendar.timegm(localtime)

# 其他相关模块和函数
# detatime模块
# pytz模块
# dateutil模块