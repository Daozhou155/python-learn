# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/11
# 正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
import re

print(re.search(r'zhou', 'dao zhou.'))
print('dao zhou'.find('zhou'))
# .可以指代除换行符外的任何字符
print(re.search(r'.', 'dao zhou'))
print(re.search(r'\.', 'dao zhou.'))  # 用\转义
print(re.search(r'\d', 'dao 123 zhou'))  # 匹配数字
print(re.search(r'\d\d\d', 'dao 123 zhou'))  # 匹配数字
print(re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', '192.168.111.123'))
print(re.search(r'[a-z]', 'Dao Zhou'))
print(re.search(r'ab{3}c', 'abbbc'))
print(re.search(r'ab{3,10}c', 'abbbbbbbc'))
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '018'))
