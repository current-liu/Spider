# coding=utf-8
"""Python模块odule:
一个Python文件，.py，包含了Python对象定义和语句
"""
import math

# From ... import 从模块中导入一个指定的部分到当前命名空间
# From ... import* 把一个模块中的所有内容导入当前的命名空间



"""命名空间和作用域
变量是拥有匹配对象的名字（标识符）。命名空间是一个包含了
变量名称们（键）和它们各自相应地对象们（值）的字典。
一个Python表达式可以访问局部命名款空间和全局命名空间里的
变量。如果一个局部变量和一个全局变量重名，则局部变量会
覆盖全局变量
"""

Money = 4000


def addMoney():
    global Money
    Money += 1

# dir()
# dir()函数返回一个排好序的字符串列表，内容是一个模块里定义过的名字
content = dir(math)
print content

# globals()和local()
# reload() 重新导入之前导入过的模块

print Money
addMoney()
print Money

import demo91
demo91.printS("import")