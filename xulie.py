# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/19
# 序列
a = 'I love dao zhou'
a = list(a)  # 字符串转列表
print(a)
b = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
b = list(b)  # 元组转列表
print(b)
c = len(b)
print(c)
print(max(b))  # 返回最大值，字符比较ASC2码
d = ['a', 'b', 'c']
print(min(d))  # 返回最小值，字符比较ASC2码
# 从小到大排序，反转,求和
print(sorted(b))
print(reversed(b))
print(list(reversed(b)))
print(sum(b))
print(list(enumerate(b)))
x = [1, 2, 3, 4, 5, 6]
y = ['a', 'b', 'c', 8]
print(list(zip(x,y)))
