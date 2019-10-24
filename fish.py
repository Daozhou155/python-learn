# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/25
# 游戏
import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print('我的位置：', self.x, self.y)


class Goldfish(Fish):
    pass


class Carp(Fish):
    pass


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        self.hungry = True
        Fish.__init__(self)  # super().__init__()也可以实现

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有的吃')
            self.hungry = False
        else:
            print('太撑了，吃不下了')


fish = Fish()
fish.move()
goldfish = Goldfish()
goldfish.move()
shark = Shark()
shark.eat()
shark.move()


# 多重继承
class Base1:
    def foo1(self):
        print('我喂自己袋盐')


class Base2:
    def foo2(self):
        print('我也喂自己袋盐')


class C(Base1, Base2):
    pass


c = C()
c.foo1()
c.foo2()
