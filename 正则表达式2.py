# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/12


import re

print(re.search(r'c|d', 'dao zhou'))
# 脱字符，匹配开头或结尾
print(re.search(r'^dao', 'dao zhou'))
print(re.search(r'zhou$', 'dao zhou'))

print(re.search(r'(dao)\1', 'daodao'))

print(re.search(r'.', 'dao.zhou'))
print(re.search(r'[.]', 'dao.zhou'))  # 使括号中的字符变为普通字符

print(re.findall(r'[a-z]', 'Dao Zhou'))
print(re.findall(r'[^a-z]', 'Dao Zhou'))  # ^放在开头表示取反
print(re.findall(r'[a-z^]', 'Dao Zhou'))

print("大括号表示匹配次数")
print(re.search(r'(dao){3}', 'daodaodao zhou'))
print(re.search(r'(dao){3,5}', 'daodaodao zhou'))  # 匹配3-5次
print(re.search(r'dao{3}', 'daooo zhou'))  # 匹配o三次

# *，+，？分别表示匹配前边的子表达式：0次或多次、一次或多次、0次或一次，默认贪婪模式
# *？，+？，？？表示非贪婪模式

result = re.search(r' (\w+) (\w+)', ' dao zhou')
print(result)
print(result.group())
print(result.group(1))
print(result.start(),result.end(),result.span())
