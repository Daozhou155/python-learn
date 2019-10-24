# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/8/24
# 图形用户界面：三种导入方式，建议使用第三种
import easygui

easygui.msgbox('嗨，道周')

from easygui import *

msgbox('你好')

import easygui as g

g.msgbox('你好，道周')
