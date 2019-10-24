# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/22
# 文件分割
f = open("E:/xiabian.txt", encoding='GBK')

x = []
y = []

for eachline in f:
    if eachline[:6] != '======':
        # 我们进行字符串分割操作
        (a, spoken) = eachline.split('：', 1)
        if a == '道周':
            x.append(spoken)
        if a == '甲鱼':
            y.append(spoken)
    else:
        file_name_x = 'x' + '.txt'
        file_name_y = 'y' + '.txt'

        x_file = open(file_name_x, 'w')
        y_file = open(file_name_y, 'w')

        x_file.writelines(x)
        y_file.writelines(y)

        x_file.close()
        y_file.close()

        x = []
        y = []

file_name_x = 'x' + '.txt'
file_name_y = 'y' + '.txt'

x_file = open(file_name_x, 'w')
y_file = open(file_name_y, 'w')

x_file.writelines(x)
y_file.writelines(y)

x_file.close()
y_file.close()

f.close()
