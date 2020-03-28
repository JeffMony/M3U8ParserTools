#!/usr/bin/python

import requests

url='https://jiuktp.com/v/c56d102e73d14b7a8e6ff172eda90ac5/index.m3u8'
file_path='/home/jeffmony/developer/python/hls_info.txt'


def getHlsInfo(url):
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
                return getHlsInfo(host_url+line)
            elif (line.startswith('http') or line.startswith('https')):
                return getHlsInfo(line)
            else:
                return getHlsInfo(base_url+'/'+line)
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

writed_file=open(file_path, 'w')
writed_file.write(getHlsInfo(url))
writed_file.close()

# try:
#     request=requests.get(url, timeout=10)
#     print(request.status_code)
#     print(request.headers)
# except:
#     print('bad')
