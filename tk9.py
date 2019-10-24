# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/23
# 滚动条
from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=sb.set)

for i in range(1000):
    lb.insert(END, i)

lb.pack(side=LEFT, fill=BOTH)
sb.config(command=lb.yview)

mainloop()
