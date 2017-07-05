# coding=utf-8
"""
Python字符串
"""
"""
访问字符串中的值
"""
var1 = 'HelloWorld'
print var1[0], var1[1:5]

"""
字符串更新
可以对已经存在的字符串进行修改，并赋值给另一个变量
"""
str1 = "Hello World"
print str1[:6]+"baby"

"""
转义字符
\ \\ \' \" 
\a \b \e \000 
\n \v \t \r \f
# \oyy  \other
"""

"""
字符串运算符
+ * 
[] [:]
in      not in
r/R %
"""

"""
字符串格式化
最基本的用法是将一个值插入到一个有字符串格式符%s的字符串中
"""
print "My name is %s and weight is %d kg" % ("lc", 85)

"""
三引号（triple quotes）
三引号可以将复杂的字符串进行赋值：
允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
保持WYSIWYG
"""
"""
Unicode字符串
"""
print u"Hello\u0020World"

"""
字符串内建函数
"""
string = "Hello World"
n = string.count("o")
print n
string.endswith("d")
string.find("H")
string.format()
string.index()
string.join()
string.replace()
string.split()
string.translate()
