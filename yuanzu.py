# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/18
# 元组创建与访问
name1 = (1, 2, 3, 4, 5, 6)
print(name1[2])
print(name1[3:5])
name2 = name1[:]
print(name2)
# 元组关键是逗号
temp = (2)          #整形
print(type(temp))
temp=[]             #列表
print(type(temp))
temp = (2,)         #元组
print(type(temp))
temp = 1,           #元组
print(type(temp))
print(8*(8,))
# 更新和删除元组
temp = ('a', 'b', 'd')
temp = temp[0:2] + ('c',) + temp[2:]
print(temp)
# del temp 删除元组






