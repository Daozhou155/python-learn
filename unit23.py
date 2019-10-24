# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/21
result = []
def get_digital(n):
    if n > 0:
        result.insert(0, n%10)
        get_digital(n//10)

get_digital(12345)
print(result)

