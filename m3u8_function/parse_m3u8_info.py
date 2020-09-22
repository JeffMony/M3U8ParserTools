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

result = parse_m3u8_info(URL)
print(result)