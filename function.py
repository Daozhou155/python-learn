# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/19
def multi(num1, num2):
    """num1,num2是形参"""
    result = num1 ** num2
    print(result)


multi(num2=2, num1=8)  # 关键字参数
xc = multi.__doc__
print(xc)


def add(n1=0, n2=1, n3=6):  # 给默认参数，未赋值时输出
    return n1 + n2 + n3


print(add())
print(add(2, 8, 6))


# 收集参数
def test(*number):
    print('参数长度为：', len(number))
    print(number[0:2])


test(1, 5, 9, 6, 7, 3)


# 形参可以是元组
def MyFun(x, y):
    return x[0] * x[1] - y[0] * y[1]


print(MyFun((3, 4), (1, 2)))


def power(x, y):
    result = 1
    for i in range(y):
        result *= x

    return result


print(power(2, 3))
print(3 in range(3))  # range(3)包括0，1，2


def myFun(*params, base=3):
    result = 0
    for each in params:
        result += each
    if each == 5:
        return result
    else:
        result *= base
    return result


print(myFun(1, 2, 3, 4, base=3))


def fun(var):
    var = 1314
    print(var, end='')


var = 520
fun(var)
print(var)


# 统计字符串参数字母个数
def count(*parama):
    length = len(parama)
    for i in range(length):
        letter = 0
        for each in parama[i]:
            if each.isalpha():
                letter += 1
        print('字母个数为', letter)


count('I love dao zhou')
