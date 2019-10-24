# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/27
a = int('123')
b = int('456')
print(a + b)


# 运算符重载
class New_int(int):
    def __add__(self, other):
        return int.__sub__(self, other)

    def __sub__(self, other):
        return int.__add__(self, other)


x = New_int(4)
y = New_int(5)
print(x + y)
print(x - y)

#反运算
