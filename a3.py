# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time:2019/8/18
# 打印10到100以内所有的质数
i = 10
while i <= 100:
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(i)
        i += 1
    else:
        i += 1
