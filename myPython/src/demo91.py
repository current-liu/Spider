# coding=utf-8
"""
Python函数
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码
"""


# def functionname(parameters):
#     "函数_文档字符串"
#     function_suite
#     return [expression]

# this is a fun
def printme(str):
    """fun"""
    print str
    return


printme("this is fun printme()")

"""
参数传递
"""
# 在Python中，string,tuples,numbers是不可更改的对象
# list,dict等是可以修改的对象
# 不可变对象a作为参数传递到函数里后，函数外部的a不会守影响
# 可变参数a则会

"""
参数：
以下是调用函数时可使用的正式参数类型：
必备参数
关键字参数
默认参数
不定长参数
"""


# 必备参数须以正确的顺序传入函数

# 关键字参数允许函数调用时参数的顺序与声明时不一致
def printinfo(name, age):
    print "Name: ", name
    print "Age:", age
    return


printinfo(age=10, name="miki")
printinfo(10, "kimi")


# 默认参数：如果没有传入，则会使用默认值
def printInfo(name, sex="male"):
    print name
    print sex
    return


printInfo("tom")


# 不定长参数
def printS(name, *vartuple):
    print name
    for var in vartuple:
        print var
    return


printS("cat", 'mao', "zhuazi")

"""
匿名函数 lambda：
lambda只是一个表达式，函数体比def简单得多
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
"""

sss = lambda a, b: a + b
print sss(1, 1)

"""return语句
    return退出语句，不带参数的return返回None
"""
r = printS(1)
print r

"""变量作用域
全局变量：定义在函数外的，拥有全局作用域
局部变量：作用在函数内部，在函数内部被访问
"""
total = 0


def sum(arg1, arg2):
    total = arg1 + arg2
    print "函数内是局部变量：", total
    return total
sum(1, 2)
print "函数外是全局变量", total
