#！/usr/bin/env python
#-*-coding:utf-8-*-
# author: zjr time:2019/8/18
#判断闰年
temp = input('请输入一个年份')
while not temp.isdigit():
    temp = input(" 抱歉，您的输入有误，请输入一个整数： ")

year = int(temp)
if year/400 == 0:
    print(temp+'闰年')
elif (year/100 != 0 and year/4 == 0):
    print(temp+'闰年')
else:
    print('非闰年')

