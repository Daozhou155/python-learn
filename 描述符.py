# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/29
# 描述符就是将某种特殊类型的类的实例指派给另一个类的属性
# get，set，delete


class Mydecriptor:
    def __get__(self, instance, owner):
        print('getting...', self, instance, owner)

    def __set__(self, instance, value):
        print('setting...', self, instance, value)

    def __delete__(self, instance):
        print("deleting...", self, instance)


class Test:
    x = Mydecriptor()


t = Test()
t.x = 'iron-man'


# del t.x


class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)  # instance是owner的实例对象

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = MyProperty(getx, setx, delx)


c = C()
c.x = 'iron-man'
print(c.x)


