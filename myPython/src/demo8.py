# coding=utf-8

"""
字典Dictionary
字典是另一种可变容器模型，且可存储任意类型对象
"""
dict1 = {'name': 192, 'sex': 'male'}

#访问
print dict1['name']

#修改
dict1['name'] = 'au'
dict1['b'] = "l"

print dict1['name'], dict1["b"]

# 删除
del dict1['name']
dict1.clear()

# 字典键的特性
# 1.不可重复
# 2.只能是不可改变的对象

dic1 = {['name']: 'zara', 'age': 7}
print dict1['name']

"""字典内置函数&方法
    cmp()
    len()
    str()
    type()
    
    dict.clear()
    dict.copy()
    dict.fromkeys(seq[,val])
    dict.get(key,default=None)
    dict.has_key(key)
    dict.items()
    dict.keys()
    dict.setdefault(key,default=None)
    dict.update(dict2)
    dict.values()
    pop(key[,default])
    popitem()"""