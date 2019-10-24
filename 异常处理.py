# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/14
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# req = Request("http://www.fishc.com/ooxx.html")#服务器无响应
req = Request("http://www.ooxx-fishc.com")  # 无法连接服务器
# 异常处理1
try:
    response = urlopen(req)
except HTTPError as e:
    print("服务器无响应")
    print('Error code:', e.code)
except URLError as f:
    print("无法连接服务器")
    print("Reason:", f.reason)
# else :
# 正常
# 异常处理2
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, "reason"):
        print('无法连接服务器2')
        print("Reason:", e.reason)
    elif hasattr(e, 'code'):
        print("服务器无响应2")
        print('Error code:', e.code)
