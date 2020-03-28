#!/usr/bin/python

import requests

url='https://video.yjf138.com/20190323/JjDT1w3n/index.m3u8'
file_path='/home/jeffmony/developer/python/hls_type.txt'
writed_file_path='/home/jeffmony/developer/python/hls_crypto_file.txt'

def getHlsInfo(url):
    if (not url.startswith('http')) and (not url.startswith('https')):
        return 'Error protocol'
    try:
        request = requests.get(url, timeout=10)
        base_url = url[0:url.rindex('/')]
        host_url = url[0 : url.index('/', url.index('://')+3)]
        result=''
        for line in request.iter_lines():
            if line.endswith('.m3u8'):
                if line.startswith('/'):
                    return getHlsInfo(host_url+line)
                elif (line.startswith('http') or line.startswith('https')):
                    return getHlsInfo(line)
                else:
                    return getHlsInfo(base_url+'/'+line)
            if line.startswith('#EXT'):
                if line.startswith('#EXT-X-KEY'):
                    return url
                else:
                    continue
            else:
                continue
        return ''
    except:
        return 'bad url:'+url

writed_file=open(writed_file_path,'w')
file=open(file_path,'r')
line=file.readline()
while line:
    url=line[:len(line)-1]
    result=getHlsInfo(url)
    if(result!=''):
        print(url)
        writed_file.write(url+'\n')
    line=file.readline();

file.close()
writed_file.close();