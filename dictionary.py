# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/20
# 字典
name = ['a', 'b', 'c', 'd']
score = [89, 98, 100, 45]
print(score[name.index('b')])

# 创建和访问字典
dict1 = {'a': 89, 'b': 98, 'c': 100, 'd': 45}
print(dict1["c"])

dict3 = dict((('a', 89), ('b', 98), ('c', 100), ('d', 45)))
print(dict3)

dict4 = dict(a=89, b="daozhou")
print(dict4)
dict4['b'] = 'shallow'    # 替换
print(dict4)
dict4['c'] = '道周'       # 添加
print(dict4)

