# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/24
# 类,对象,属性
class Turtle:
    colorr = 'green'
    weight = 200
    legs = 4

    def climb(self):
        print('我正在爬')


tt = Turtle()
tt.climb()

# 封装
list1 = [1, 9, 6, 4, 5, 7, 3]
list1.sort()
print(list1)


# 继承，类Mylist继承list
class Mylist(list):
    pass


list2 = Mylist()
list2.append(2)
list2.append(5)
print(list2)


# 多态
class A:
    def fun(self):
        print('我是A')


class B:
    def fun(self):
        print('我是B')


a = A()
b = B()
a.fun()
b.fun()


class Ball:
    def setname(self, name):
        self.name = name

    def kick(self):
        print('我叫%s,谁踢我？' % self.name)


a = Ball()
a.setname('球A')
b = Ball()
a.setname('球B')
c = Ball()
c.setname('小甲鱼')
a.kick()
c.kick()


# __init__（）可以方便地自己对类的属性进行定义，__init__()方法又被称为构造器（constructor）
class C:
    def __init__(self, name):
        self.name = name

    def kick(self):
        print('我叫%s,谁踢我？' % self.name)


d = C('土豆')  # 不需要再调用函数
d.kick()


# 公有与私有
class Person:
    name = '道周'


p = Person()
print(p.name)


class Person1:
    __name = '道周'  # name前加双下划线表示私有

    def getname(self):
        return self.__name


p = Person1()
# print(p.__name)  # 不能访问
print(p.getname())
k = Person1()
print(k._Person1__name)  # 其实是将名字改为：_类名__变量名


# 继 承
class Parent:
    def hello(self):
        print('正在调用父类\基类\超类')


class Child(Parent):  # 如果子类定义与父类同名的方法或属性，则会覆盖父类对应的方法和属性
    pass


g = Parent()
g.hello()
h = Child()
h.hello()
