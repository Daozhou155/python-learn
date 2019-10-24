# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/16
from tkinter import *

from PIL import ImageTk

root = Tk()

textLabel = Label(root, text="你好，\n我是道周",
                  justify=LEFT,
                  padx=10, pady=10)
textLabel.pack(side=LEFT)

# photo = PhotoImage(file="C:\\Users\\A1\\Desktop\\cat.jpg") #只能显示gif图片
photo = ImageTk.PhotoImage(file="C:\\Users\\A1\\Desktop\\cat.jpg")  # 可以显示jpg格式图片
imgLabel = Label(root, image=photo)
imgLabel.pack()

mainloop()
