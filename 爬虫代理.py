# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/11

import urllib.request
import random

url = 'http://www.whatismyip.com.tw'
# 1.参数是一个字典{‘类型’：‘代理ip：端口号’}
iplist = ['149.129.98.81:80', '221.178.176.25:3128', '114.239.1.46:9999', '218.75.102.198:8000']

proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})

# 2.定制创建一个opener

opener = urllib.request.build_opener(proxy_support)

opener.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
