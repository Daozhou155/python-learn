# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/22
# 模块
import random  # 输入模块

secret = random.randint(1, 10)
print(secret)

# os模块
import os

print(os.getcwd())  # 返回当前工作目录
print(os.listdir('E:\\'))  # 列举制定目录中的文件
# print(os.mkdir('E:\\A'))
# print(os.mkdir('E:\\A\\B'))         #创建单层目录，文件已存在不能再创建
# print(os.makedirs('E:\\A\\C'))      #递归创建多层目录，文件已存在不能再创建
# print(os.remove())                  #删除文件
# print(os.rmdir('E:\\A\\B'))  #删除单层目录，前提目录是空的
# print(os.removedirs('E:\\A\\C'))  #逐层删除目录，前提目录是空的
print(os.system('cmd'))    #运行系统shell


