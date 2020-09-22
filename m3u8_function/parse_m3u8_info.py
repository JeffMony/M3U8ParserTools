#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urlparse

TAG_PREFIX='#EXT'
PLAYLIST_HEADER='#EXTM3U'
TAG_ENDLIST='#EXT-X-ENDLIST'
TAG_KEY='#EXT-X-KEY'
TAG_STREAM_INF='#EXT-X-STREAM-INF'

URL='https://cdn3.lajiao-bo.com/20200113/DGKlALM5/index.m3u8'

### 返回最终的m3u8文件
def parse_m3u8_info(url):
    val = urlparse.urlsplit(url)
    if (val.scheme != 'http') and (val.scheme != 'https'):
        return 'Error protocol'
    hostUrl = url[0:url.index(val.netloc)+len(val.netloc)]
    baseUrl = url[0:url.rindex('/')+1]
    request = requests.get(url, timeout=20)
    result = ''
    hasStreamInf = False
    for line in request.iter_lines():
        if (line.startswith(TAG_PREFIX)):
            result += line + '\n'
            if (line.startswith(TAG_STREAM_INF)):
                hasStreamInf = True
            continue
        if (hasStreamInf):
            return parse_m3u8_info(get_final_url(url, line))
        hasStreamInf = False
        result += get_final_url(url, line) + '\n'
    return result

### 根据m3u8中的分片写法得到完整的url
def get_final_url(url, line):
    val = urlparse.urlsplit(url)
    hostUrl = url[0:url.index(val.netloc)+len(val.netloc)]
    baseUrl = url[0:url.rindex('/')+1]
    if (line.startswith('/')):
        tempUrl = ''
        tempIndex = line.index('/', 1)
        if (tempIndex == -1):
            tempUrl = baseUrl + line[1:]
        else:
            tempUrl = line[0:tempIndex]
            tempIndex = url.index(tempUrl)
            if (tempIndex == -1):
                tempUrl = hostUrl + line[1:]
            else:
                tempUrl = url[0:tempIndex] + line
            return tempUrl
    if (line.startswith('http://') or line.startswith('https://')):
        return line
    return baseUrl + line

### 判断m3u8中是否存在#EXT-X-STREAM-INF
def has_ext_stream(url):
    val = urlparse.urlsplit(url)
    if (val.scheme != 'http') and (val.scheme != 'https'):
        return 'Error protocol'
    request = requests.get(url, timeout=20)
    for line in request.iter_lines():
        if (line.startswith(TAG_PREFIX)):
            if (line.startswith(TAG_STREAM_INF)):
                return True
    return False

### 判断m3u8中是否存在#EXT-X-KEY
def has_ext_key(url):
    val = urlparse.urlsplit(url)
    if (val.scheme != 'http') and (val.scheme != 'https'):
        return 'Error protocol'
    request = requests.get(url, timeout=20)
    for line in request.iter_lines():
        if (line.startswith(TAG_PREFIX)):
            if (line.startswith(TAG_KEY)):
                return True
    return False

result = parse_m3u8_info(URL)
print('M3U8文件内容如下:\n' + result)

hasExtStream = has_ext_stream(URL)
print('是否存在多路流: ---> ' + str(hasExtStream))

hasExtKey = has_ext_key(URL)
print('是否存在key: ---> ' + str(hasExtKey))

