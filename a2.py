#！/usr/bin/env python
#-*-coding:utf-8-*-
# author: zjr time:2019/8/18
#验证密码
count = 3
password = 'zjr'

while count:
    passwd = input("请输入密码")
    if passwd == password:
        print(' 密码正确 ')
        break
    else:
        print(' 密码错误！您还有', count-1, '次机会', end='')
        count-=1