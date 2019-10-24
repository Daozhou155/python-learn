# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/23
# Scale：范围滚动
from tkinter import *

root = Tk()
# 间隔,分辨率设置
s1 = Scale(root, from_=0, to=42, tickinterval=5, resolution=5, length=200)
s1.pack()

s2 = Scale(root, from_=0, to=200, tickinterval=10, orient=HORIZONTAL, length=600)
s2.pack()


def show():
    print(s1.get(), s2.get())


Button(root, text="获取位置", command=show).pack()

mainloop()
