# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/31
# 华氏度与摄氏度转换


class Celsius:
    def __init__(self, value=26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


temp = Temperature()
print(temp.cel)
temp.cel = 30
print(temp.fah)


