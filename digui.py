# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/20
# 非递归求阶乘
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


number = int(input('请输入一个正整数：'))
print(factorial(number))


# 递归求阶乘
def factor(n):
    if n == 1:
        return 1
    else:
        return n * factor(n - 1)


num = int(input('请输入一个正整数：'))
print(factor(num))
