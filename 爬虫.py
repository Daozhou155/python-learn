# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/10


import urllib.request

response = urllib.request.urlopen("http://www.fishc.com")
html = response.read()
print(html)
html = html.decode('utf-8')  # 解码
print(html)
