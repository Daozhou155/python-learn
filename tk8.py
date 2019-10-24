# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/23
# Listbox()
from tkinter import *

master = Tk()

# selecmode四种模式：SINGLE（单选）,BROWSE（单选，可拖动鼠标）,MULTIPLE（多选）,EXTENDED（多选，shfit、Ctrl或拖鼠标）
# height 为行数
theLB = Listbox(master, selectmode=MULTIPLE,height=11)
theLB.pack()

# for item in ["公鸡", "大鱼", '怪']:
#     theLB.insert(END, item)

for item in range(11):
    theLB.insert(END, item)

# 删除所有元素
# theLB.delete(0,END)
# 删除当前选中
theButton = Button(master, text="删除", command=lambda x=theLB: x.delete(ACTIVE))  # 删除当前选中
theButton.pack()

mainloop()
