# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/26

# 构造
# __init__(self)
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getperi(self):
        return (self.x + self.y) * 2

    def getarea(self):
        return self.x * self.y


r = Rectangle(8, 9)
print(r.getperi())
print(r.getarea())


# _new_({,...])
class Capstr(str):  # 继承str类，不可改，不能用__init__
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


a = Capstr('I am daozhou')
print(a)


# 析构
class C:
    def __init__(self):
        print('我是--init--方法')

    def __del__(self):
        print('我是--del--方法')


c1 = C()
c2 = c1
c3 = c2
print(c1)
del c3
del c2
del c1


