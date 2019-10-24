# ！/usr/bin/env python
# -*-coding:utf-8-*-
# author: zjr time: 2019/10/14
# 从贴吧爬图片

import urllib.request
import re


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('user-agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html


def get_imag(html):
    #图片正则化表达式
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p, html)

    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)


if __name__ == '__main__':
    url = "https://tieba.baidu.com/p/6295817568"
    get_imag(open_url(url))


# 爬ip
def get_ip(html):
    #ip正则化表达式
    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    iplist = re.findall(p, html)

    for each in iplist:
        print(each)


if __name__ == '__main__':
    url = "https://www.kuaidaili.com/free/inha"
    get_ip(open_url(url))
