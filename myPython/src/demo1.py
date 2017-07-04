# coding=utf-8
# Python变量类型
"""
变量赋值
Python中的变量赋值不需要类型声明
每个变量在使用前都必须赋值
"""
a = 100
b = 100.0
c = "lc"
print a
print b
print c

"""
多个变量赋值
"""
a = b = c = 1
print a, b, c

a, b, c = 1, 2, "au"
print a, b, c


# 标准数据类型

"""
Python数字 Nmbers：

不可改变的数据类型，改变则和分配一个新的对象
Python支持四种数字类型：
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）
"""
var1 = 1
var2 = 10
del var1, var2
# print var1

"""
Python字符串：Strings
"""
str1 = 'Iloveau'
print str1
print str1[0]
print str1[1:3]
print str1[2:]
print str1[-1]
print str1[-1:1]
print str1[-5:-3]
print str1 * 2
print str1 + "bixude"

"""
Python列表：List
列表可以完成大多数集合类的数据结构实现，
它支持字符，数字，字符串，还可以包含列表（即嵌套）
"""
list1 = ["au", 192, 2.3]
list2 = [123, "ll"]
print list1[0]
print list1[1:3]
print list1[2:]
print list2 * 2
print list1 + list2

"""
Python元组：Tuple
类似于List，但Tuple不能二次赋值，相当于只读列表
"""
tuple1 = ('au', 192, 907, 'john')
tuple2 = (123, 'king')
print tuple1[0]
print tuple1[1:3]
print tuple1[2:]
print tuple2 * 2
print tuple1 + tuple2

"""
Python字典：Dictionary
无序的对象集合，由索引和它对应的值value组成
"""
dict1 = {}
dict2 = {"name": "lc", "gf": "au"}
# dict["one"] = "this is one"
# dict[2] = "this is two"
# print dict[2]
print dict2
print dict2.keys()
print dict2.values()
# python的所有数据类型都是类，可以通过type（）查看该变量的数据类型
print(type(dict2))

"""
Python数据类型转换
将数据类型作为函数名即可
"""
a = 3
b = str(a)
print(type(b))
print b
