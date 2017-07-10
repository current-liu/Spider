# coding=utf-8
"""
Python列表（List）
序列是Python中最基本的数据结构。序列中的每个元素都会分配一个索引来记录它的位置。
Python有6个序列的内置类型，列表和元组是最常见的。
"""
list1 = ['physics', 1997, 1984]
list2 = ['physics', 1997, 1984]
print list1[0]
print list1[1:3]

"""
更新List
"""
list1[1] = 'haha'
print list1[1]

"""
删除列表元素
"""
del list1[2]
#print list1[2]

"""
Python列表的函数&方法
"""
cmp(list1, list2)
len()
max()
min()
list(seq)

l = [2017, 2018]
l.append()
l.count()
l.extend()
l.index()
l.insert()
l.pop()
l.remove()
l.remove()
l.sort()


"""
元组Tuple
Tuple与List类似，但元组的元素不能修改
"""
tup1 = ()
tup2 = (au,) #只有一个元素时，‘，’不能少

"""
修改元组、删除元组
"""
tup3 = tup1 + tup2
del tup3


"""
无关闭分隔符
任意无符号的对象，以对号隔开，默认为元组
"""
# 啥意思

"""
Tuple内置函数
"""
cmp()
len()
max()
min()
tuple(seq)




