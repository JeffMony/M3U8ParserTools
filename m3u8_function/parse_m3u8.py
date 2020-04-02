#!/usr/bin/python
# -*- coding: UTF-8 -*-

## 将m3u8文件解析到本地


import requests

url='https://cdn3.lajiao-bo.com/20200113/DGKlALM5/index.m3u8'
m3u8_file_str='/Users/jeffmony/sources/M3U8ParserTools/m3u8_function/m3u8_info.txt'


def parseM3U8Info(url):
    if (not url.startswith('http')) and (not url.startswith('https')):
        return 'Error protocol'
    request = requests.get(url, timeout=10)
    base_url = url[0:url.rindex('/')]
    host_url = url[0 : url.index('/', url.index('://')+3)]
    result=''
    for line in request.iter_lines():
        print(line)
        if line.endswith('.m3u8'):
            if line.startswith('/'):
                return parseM3U8Info(host_url+line)
            elif (line.startswith('http') or line.startswith('https')):
                return parseM3U8Info(line)
            else:
                return parseM3U8Info(base_url+'/'+line)
        if line.startswith('#EXT'):
            if line.startswith('#EXT-X-KEY'):
                if line.find('URI'):
                    start_index=line.index('URI=')
                    end_index=line.index('\"', start_index+5)
                    prefix=line[:start_index+5]
                    suffix=line[end_index]
                    key=line[start_index+5:end_index]
                    key_result=''
                    if key.startswith('/'):
                        key_result=host_url+key
                    elif (key.startswith('http') or key.startswith('https')):
                        key_result=key
                    else:
                        key_result=base_url+'/'+key
                    result+=(prefix+key_result+suffix)+'\n'
            else:
                result+=line+'\n'
        elif line.startswith('/'):
            result+=host_url+line+'\n'
        elif (line.startswith('http') or line.startswith('https')):
            result+=line+'\n'
        else:
            result+=base_url+'/'+line+'\n'
    return result

m3u8_file=open(m3u8_file_str, 'w')
m3u8_file.write(parseM3U8Info(url))
m3u8_file.close()
