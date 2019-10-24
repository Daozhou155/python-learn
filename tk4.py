# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/16
from tkinter import *

from PIL import ImageTk

root = Tk()

photo = ImageTk.PhotoImage(file="C:\\Users\\A1\\Desktop\\bg.psd")
theLabel = Label(root,
                 text="挖掘机技术哪家强，\n中国山东找蓝翔",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=("宋体", 20),
                 fg="blue")
theLabel.pack()

mainloop()
