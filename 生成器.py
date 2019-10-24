# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/9


def myGen():
    print("生成器被执行！")
    yield 1
    yield 2


myG = myGen()
print(next(myG))
print(next(myG))

#生成器
a = [i for i in range(100) if not (i % 2) and i % 3]
print(a)
b = {i: i % 2 == 0 for i in range(10)}
print(b)
c = {i for i in [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 8, 9]}
print(c)
e = (i for i in range(10))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
f = sum(i for i in range(101))
print(f)

