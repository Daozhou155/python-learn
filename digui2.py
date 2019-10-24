# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/20
# 斐波那契数列
#迭代法
def fab(n):
    a = 1
    b = 1
    c = 1

    if n < 1:
        print("输入错误")
        return -1

    while (n-2) > 0:
        c = a+b
        a = b
        b = c
        n -= 1

    return c

result = fab(40)
print(result)

#递归法
def fb(n):
    if n < 1:
        print('输入错误')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fb(n-2)+fb(n-1)

    return result
s = fb(40)
print(s)
#同样求40，递归比迭代慢很多
