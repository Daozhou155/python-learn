# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/16
from tkinter import *

from PIL import ImageTk


def callback():
    var.set("骗子")


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("你好，\n我是道周")

textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)
textLabel.pack(side=LEFT)

photo = ImageTk.PhotoImage(file="C:\\Users\\A1\\Desktop\\cat.jpg")
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text="我也是道周", command=callback)
theButton.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()
