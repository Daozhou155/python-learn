# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/22
# 文件
fo = open("E:/zimu.txt", encoding='ISO-8859-1')  # 英文编码使用
# fo = open("E:/record.txt", encoding='GBK')         #中文编码使用
# fo = open("E:/record.txt", encoding='utf-8')
print("文件名为: ", fo.name)
line = fo.read()
print(line)
print(list(line))  # 将文件对象中的数据存放进列表

# 关闭文件
line2 = fo.read()  # 已经指向文件最后，读取不了
print(line2)
fo.close()

fo = open("E:/zimu.txt", encoding='ISO-8859-1')
line3 = fo.read(3)
print(line3)
print(fo.tell())  # 返回当前在文件中的位置，英文一个字符，中文三个字符
fo.seek(3, 0)  # 在文件中移动指针，从0、1、2（起始、当前、末尾）移动3个字节
print(fo.readline())  # 读取一行
fo.close()

f = open("E:/text.txt", 'w')  # 没有则创建一个文件，有则覆盖
f.write('我是道周')
f.close()  # 写完关闭文件，否则内容存在缓存区里，未写入
f = open("E:/text.txt", encoding='GBK')
l = f.read()
print(l)

# 将f中的数据保存到f2中
f = open("E:/text.txt")
f2 = open("E:/text8.txt", 'w')
f2.write(f.read())
f2.close()
f.close()

f2 = open("E:/text8.txt")
d = f2.read()
print(d)
