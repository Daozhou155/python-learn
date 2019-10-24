# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time:2019/8/18
# 列表元素提取
list1 = [1, 2, ['a', 'b'], 123]
print(list1[2][1])
# 列表元素计数，不能计算列表中的列表
list2 = [123, 456, 789, [123, 111]]
list2 *= 5
a = list2.count(123)
print(a)
# 列表元素位置
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list3.index(3, 0, 10))
# 列表反转
list3.reverse()
print(list3)
# 列表排序
list4 = [6, 2, 9, 24, 3, 75, 0, 48, 4]
list4.sort()  # 从小到大
print(list4)
list4.sort(reverse=True)  # 从大到小
print(list4)
# 列表分片
list5 = [1, 2, 3, 6, 5, 4]
list6 = list5[0:2]
print(list6)
