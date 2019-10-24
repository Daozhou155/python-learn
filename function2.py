# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/20
# 函数返回值
def back():
    return [1, 'daozhou', 2]


print(back())

# 局部变量与全局变量
def discount(price,rate):
    old_price = 50
    print('修改后的原价：', old_price)
    final_price = price*rate
    return final_price


old_price = float(input("请输入原价："))
rate = float(input("请输入折扣率："))
new_price = discount(old_price, rate)
print('原价：', old_price)
print("打折后的价格为：", new_price)

