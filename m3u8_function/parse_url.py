#!/usr/bin/python
# -*- coding: UTF-8 -*-

## 将网络url中的信息保存到本地


import requests

url='http://dov.mkanav1.com/20200203/UxM4G8Wt/index.m3u8'

def parseUrlInfo(url):
    if (not url.startswith('http')) and (not url.startswith('https')):
        return 'Error protocol'
    request = requests.get(url, timeout=10)
    print request.status_code
    result=''
    for line in request.iter_lines():
        print(line)
        result+=line+'\n'
    return result

print(parseUrlInfo(url))