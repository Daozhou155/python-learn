# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/20
# 函数嵌套
count = 4
def fun1():
    global count  # 把局部变量声明为全局变量
    count = 10
    print(count)


fun1()
print(count)


def funx(x):
    def funy(y):
        return x * y
    return funy


print(funx(5)(8))


def fun2():
    x = 5            #局部变量
    def fu2():
        nonlocal x   # 声明为非局部变量
        x *=x
        return x
    return fu2()

print(fun2())



