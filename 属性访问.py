# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/29


class C:
    def __getattribute__(self, name):
        print('getattribute')
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print('getattr')

    def __setattr__(self, name, value):
        print('setattr')
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print('delattr')
        super().__delattr__(name)


c = C()
print(c.x)
c.x = 1
print(c.x)
del c.x
print(c.x)


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.height = value
        else:
            super().__setattr__(key, value)  # self.__dict__[key] = value

    def getarea(self):
        return self.width * self.height


r1 = Rectangle(4, 5)
print(r1.getarea())
r1.square = 10
print(r1.width)
print(r1.height)
print(r1.getarea())
