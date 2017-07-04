# coding=utf-8
"""
Python循环语句
while
for
嵌套：在循环体中嵌套其他的循环
"""

'''
循环控制语句
break：终止循环
continue：跳出该次循环
pass：空语句，为了保持程序结构的完整性
'''

"""
while循环
while（boolean）：
    pass
else：
    pass
"""
# 简单语句组
# 类似 if 语句的语法，如果你的 while 循环体中只有一条语句，
# 你可以将该语句与while写在同一行中

flag = 1
while flag:
    print 'haha'
    flag+=1
    if flag>10: break
"""
Python for循环
可以遍历任何序列的项目，如一个列表或一个字符串
"""
for letter in 'Python':
    print 'this letter:', letter

"""
通过序列索引迭代
"""
fruits = ['banana', 'apple', 'mango']
# 返回列表的长度
print len(fruits)
# 返回一个序列的数
print range(len(fruits))
for index in range(len(fruits)):
    print 'this fruits:', fruits[index]

"""
循环使用else语句：
    循环正常执行完的情况下执行
"""
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num/i
            print '%d 等于 %d * %d' % (num, i, j)
            break
    else:
        print num, '是一个质数'

"""
Python pass语句
    空语句，保持程序结构的完整性，一般用作占位语句
"""