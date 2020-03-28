#!/usr/bin/python

# import requests

# file_path='/home/jeffmony/developer/python/hls_type.txt'

# def get_mime_type(url):
#     try:
#         request = requests.get(url, timeout=10)
#         return request.headers['Content-Type']
#     except:
#         return 'unknown'

# file=open(file_path,'r')
# line=file.readline()
# while line:
#     url=line[:len(line)-1]
#     mime_type=get_mime_type(url)
#     if(mime_type=='application/force-download'):
#         print(url)
#     line=file.readline()

# file.close()


# import requests
# from urllib.parse import urlparse

# file_path='/home/jeffmony/developer/python/hls_type.txt'
# writed_file_path='/home/jeffmony/developer/python/hls_not_m3u8.txt'

# writed_file=open(writed_file_path,'w')
# file=open(file_path,'r')
# line=file.readline()
# while line:
#     url=line[:len(line)-1]
#     result=urlparse(url)
#     host=result.path
#     if(host.find('.')!=-1):
#         suffix=host[host.rindex('.'):]
#     else:
#         suffix='XXX'
#     if(suffix!='.m3u8'):
#         writed_file.write(line)
#     line=file.readline()

# writed_file.close()
# file.close()

# import requests

# file_path='/home/jeffmony/developer/python/hls_not_m3u8.txt'

# def sort_by_value(d):
#     return sorted(d.items(),key=lambda item:item[1], reverse = True)

# def get_mime_type(url):
#     try:
#         request=requests.get(url, timeout=10)
#         return request.headers['Content-Type']
#     except:
#         return 'unknown'

# dict={}
# file=open(file_path,'r')
# line=file.readline()
# while line:
#     url=line[:len(line)-1]
#     mime_type=get_mime_type(url)
#     if(dict.__contains__(mime_type)):
#         count=dict[mime_type]
#         count+=1
#         dict[mime_type]=count
#     else:
#         dict[mime_type]=1
#     line=file.readline()

# print(sort_by_value(dict))

# file.close()


import requests

file_path='/home/jeffmony/developer/python/hls_not_m3u8.txt'

def get_mime_type(url):
    try:
        request=requests.get(url, timeout=10)
        return request.headers['Content-Type']
    except:
        return 'unknown'

file=open(file_path,'r')
line=file.readline()
while line:
    url=line[:len(line)-1]
    mime_type=get_mime_type(url)
    if(mime_type=='text/html; charset=UTF-8' or mime_type=='text/html' or mime_type=='unknown'):
        print url
    line=file.readline()

file.close()