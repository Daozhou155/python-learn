# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/19
#列表
list1 = [1, [1, 2, [' 小甲鱼']], 3, 5, 8, 13, 18]
list1[1][2][0] = ' 小鱿鱼'  # 列表替换
print(list1)
list2 = [1, 3, 5, 9, 7, 4]
list2.sort()
print(list2)  # 列表排序
list2.reverse()
print(list2)  # 列表逆排序=list2.sort(reverse=True)
list2.clear()  # 清空列表元素
print(list2)
#元组
x, y, z = 1, 2, 3
print(type(x))
h = x, y, z
print(type(h)) #单个x是整形，多对象逗号分割组成的h是元组

