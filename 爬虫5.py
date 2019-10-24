# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/11


import urllib.request
import urllib.parse
import json

# content = input("请输入要翻译的内容")
# url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"


url = 'https://fanyi.baidu.com/sug'

# 隐藏1

# head = {}
# head['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

data = {"kw": 'love'}
data = urllib.parse.urlencode(data).encode('utf-8')
#隐藏2
response = urllib.request.urlopen(url, data)
#response.addheaders=[('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')]
html = response.read().decode('utf-8')

print(html)

translate_results = json.loads(html)
print(translate_results)
