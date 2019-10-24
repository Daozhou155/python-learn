# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/19
# 字符串
str1 = 'i love daozhou'
print(str1[:6])
print(str1.capitalize())  # 第一个字母大写
print(str1.casefold())  # 全部变小写
print(str1.center(40))  # 字符串居中，前后空40
print(str1.count('I'))  # 计数，区分大小写
print(str1.endswith('ou'))  # 判断是否以某字符串结尾
print(str1.find('ab'))
print(str1.find('ao'))  # 找字符串
print(str1.replace('daozhou', "shallow"))  # 替换字符串
print(str1.split('o'))  # 以选定的字符串分割切片，返回列表
print(str1.strip("u"))  # 定制删除字符
# 格式化
x = '{0} love {1} {2}'.format('I', 'dao', 'zhou')  # 位置参数
print(x)
y = '{a} love {b} {c}'.format(a='I', b='dao', c='zhou')  # 关键字参数
print(y)
z = '{0} love {b} {c}'.format('I', b='dao', c='zhou')  # 混合使用，位置参数在关键字参数之前
print(z)
n = '{0:.1f}{1}'.format(50.68, 'TB')  # 四舍五入保留一位小数
print(n)
m = '%c %c %c' % (97, 98, 99)  # ASC 码
print(m)
q = '%f' % 27.688  # 格式化定点数，六位小数
print(q)
w = '%5.2f' % 6.238  # 5是最小宽度，不够补空格，2是小数点后位数
print(w)
###################################?
str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
print(str1[::3])
str1 = '<a href="http://www.fishc.com/dvd"target="_blank"> 鱼C 资源打包</a>'
print(str1[-46:-32])
print(str1[20:-36])
h = "{{1}}".format(" 不打印", " 打印")
print(h)
j = '{0} {1:.2f}'.format('Pi = ', 3.1415926)
print(j)
