# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/18
# Entry组件

from tkinter import *

root = Tk()

Label(root, text="账号：").grid(row=0, column=0)  # 第一行，第一列
Label(root, text="密码：").grid(row=1, column=0)

e1 = Entry(root)
e2 = Entry(root, show="*")

e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def show():
    print("账号：%s" % e1.get())
    print("密码：%s" % e2.get())


Button(root, text="确定", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="退出", width=10, command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()
