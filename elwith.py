# ��/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/24
#判断最大公约数
def showmaxfactor(num):
    count = num //2
    while count >1:
        if num % count == 0:
            print('%d最大约数是%d' % (num, count))
            break
        count -=1
    else:
        print('%d是素数' % num)

num = int(input('请输入一个数：'))
showmaxfactor(num)

try:
    int('123')
except ValueError as reason:
    print('出错啦'+str(reason))
else:
    print('没有任何异常')

try:
    with open('data.txt', 'w') as f:#自动关闭打开的文件
        for eachline in f:
            print(eachline)
except OSError as reason:
    print('出错啦'+str(reason))

