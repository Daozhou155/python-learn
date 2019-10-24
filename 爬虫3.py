# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/10


import urllib.request
import urllib.parse
import json

# content = input("请输入要翻译的内容")
# url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
url = 'https://fanyi.baidu.com/sug'
data = {"kw": 'love'}
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')

print(html)

translate_results = json.loads(html)
print(translate_results)
