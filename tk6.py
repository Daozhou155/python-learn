# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/16
# Checkbutton组件
from tkinter import *

'''
root = Tk()

v = IntVar()

c = Checkbutton(root, text="测试", variable=v)
c.pack()

la = Label(root, textvariable=v)
la.pack()

mainloop()
'''
'''
root = Tk()
girls = ['西施', "杨玉环", '王昭君', "貂蝉"]

v = []
for girl in girls:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v[-1])
    b.pack(anchor=W)

mainloop()
'''
# Radiobutton
'''
root = Tk()

v = IntVar()

# Radiobutton(root, text='one', variable=v, value=1).pack(anchor=W)
# Radiobutton(root, text='two', variable=v, value=2).pack(anchor=W)
# Radiobutton(root, text='three', variable=v, value=3).pack(anchor=W)

LANGS = [("A", 1), ("B", 2), ("C", 3), ("D", 4)]
v = IntVar()
v.set(1)

for lang, num in LANGS:
    b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)  # 方形按钮
    b.pack(fill=X)  # 横向填充

mainloop()
'''
# LabelFrame
root = Tk()
group = LabelFrame(root, text="正确答案是？", padx=5, pady=5)
group.pack(padx=10, pady=10)

LANGS = [("A", 1), ("B", 2), ("C", 3), ("D", 4)]
v = IntVar()

for lang, num in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=num)
    b.pack(anchor=W)  # 横向填充

mainloop()
