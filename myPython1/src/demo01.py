# coding=utf-8
class Emp:
    "所有员工的基类"
    empCount = 0
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        Emp.empCount +=1
    def toString(self):
        print self.name, self.sex
        print self.__class__
e = Emp("lc", "male")
e.toString()
print e.name
e.age = 20
print e.age
# e = Emp("l", "m", 30)
print e.__doc__

"""python对象销毁（垃圾回收）
    Python使用了引用计数这一简单技术来跟踪和回收垃圾，在python内部
    记录着所有使用中的对象有多少引用"""

"""类的继承：
    1.在继承中基类的构造（__init__()）不会被调用，它需要在其派生类的
        构造中亲自专门调用。
    2.在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。
        区别于在类中调用普通函数时并不需要带上self参数
    3.Python总是首先查找对应类型的方法，如果它不能再派生类中中找到对应的
        方法，它才开始到基类中逐个查找"""

class Parent:
    parentAttr = 100
    def __init__(self):
        print "Parent's init()"
    def parentMethond(self):
        print "Parent's method"
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print "parent's member:", Parent.parentAttr

class Child(Parent):
    def __init__(self):
        print "Child's init()"
    def childMethod(self):
        print "child's method"

    __privateCount = 0
    publicCount = 0
    def count(self):
        self.__privateCount += 1
        self.publicCount += 1
        print self.__privateCount

c = Child()
c.childMethod()
c.parentMethond()
c.setAttr(200)
c.getAttr()

# 可以继承多个类
# issubclass()或者isinstance（）方法来检测

"""方法重写
    一些通用的功能，自己可以根据需求重写：
    __init__(self,[,args...])
    __del__(self)
    __repr__(self)
    __str__(self)
    __cmp__(self,x)    
    """

"""类属性与方法
"""
# 类的私有属性：__private_attrs:两个下划线开头，声明该属性为私有，不能再类的外部被使用或直接访问。
#   再类内部的方法中使用时 self.__private_attrs

# 类的方法：在类的内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self，
#    且为第一个参数

# 类的私有方法：参照类的私有属性
child = Child()
child.count()
child.count()
print child.publicCount
# print child.__privateCount 报错，实例不能访问私有变量
print child._Child__privateCount

"""
头尾双下划线：__foo__:定义的是特例方法，类似__init__()
单下划线：_foo：protected，只允许其本身与子类进行访问，不能用于from module import *
双下划线：__foo：private,只能是允许这个类本身进行访问"""
