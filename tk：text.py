# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/23
# Text组件
from tkinter import *
# 插入其他种类的图,PhotoImage插入gif
from PIL import Image, ImageTk

root = Tk()

text1 = Text(root, width=100, height=50)
text1.pack()

# 插入文字
text1.insert(INSERT, "我的名字\n")
text1.insert(END, "道周")

# 插入图片
im = Image.open("C:\\Users\\A1\\Desktop\\cat.jpg")
photo = ImageTk.PhotoImage(im)


def show():
    print("谁在点我")
    text1.image_create(END, image=photo)


# 插入按钮
b1 = Button(text1, text="点我", command=show)
text1.window_create(INSERT, window=b1)

mainloop()
# index索引，mark标记
