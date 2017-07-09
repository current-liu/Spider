# coding=utf-8

"""Python文件I/O"""
# 打印到屏幕 print

# 读取键盘输入
# raw_input、input

# str = raw_input("please input:")
# print "your input is: ", str

# input()和raw_input()基本类似，但input()可以接收一个
# Python表达式作为输入，并将运算结果返回
# str1 = input("please input:")
# print "your input is: ", str1

"""打开和关闭文件
    Python提供了必要的函数和方法进行默认情况下的文件基本操作。
    你可以用file对象做大部分的文件操作
    """
# open函数
fo = open("foo.txt", "wb")
print "file name:", fo.name
print "is closed?", fo.closed
print "mode:", fo.mode
print "softspace:"

# close()方法
# File对象的close()方法刷新缓冲区里任何还没写入的信息，并
# 关闭该文件，这之后便不能再进行写入。
# 当一个文件对象的引用被重新指定给另一个文件时，Python会关闭
# 之前的文件。用close()方法关闭文件是一个很好的习惯

fo.close()
print "fo.name:", fo.name
print "fo.mode:", fo.mode

# write()方法
# write()方法可以将任何字符串写入一个打开的文件。
# 不仅是文字，也可以是二进制数据
fo = open("foo.txt", "wb")
fo.write("Hello moto")
#fo.close()

# read()方法
fo = open("foo.txt")
str = fo.read()
print str

# 文件定位
print "position:", fo.tell()
str = fo.read(1)
print "the string readed:", str
