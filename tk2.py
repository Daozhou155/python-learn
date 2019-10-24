# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/15
import tkinter as tk


def say_hi():
    print("你好，我是道周")


class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=10, pady=10)  # 调整按钮位置

        self.hi_there = tk.Button(frame, text="打招呼", bg="black", fg='blue', command=say_hi)  # say_hi不加括号
        self.hi_there.pack()


root = tk.Tk()
app = APP(root)

root.mainloop()
