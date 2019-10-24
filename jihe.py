# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/21
# 集合：内部元素唯一
num = {1, 3, 5, 7, 8, 7, 8, 9}
print(num)
set1 = {1, 2, 3, 4, 5, 6, 5, 4}
print(set1)

#去掉列表中的重复元素
num1 = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6]
set2 = set(num1)
num2 = list(set2)
print(num2)

#判断、添加、移除,冻结集合元素
print(1 in set2)
set2.add(9)
print(set2)
set2.remove(1)
print(set2)
set4 = frozenset([1, 2, 3, 4])#集合不可变
print(set4)
print(len(set4)) # 确定集合内的元素，集合是无序的
