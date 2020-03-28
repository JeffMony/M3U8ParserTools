#!/usr/bin/python

import requests

file_path='/home/jeffmony/developer/python/hls_list.txt'
writed_file_path='/home/jeffmony/developer/python/hls_error.txt'

def get_status_code(url):
    try:
        request = requests.get(url, timeout=10)
        return request.status_code
    except:
        return -1000

writed_file=open(writed_file_path,'w')
file=open(file_path,'r')
line=file.readline()
while line:
    url=line[:len(line)-1]
    print(url)
    code=get_status_code(url)
    if(code!=200):
        writed_file.write(str(code)+':'+url+'\n')
    line=file.readline()

writed_file.close()
file.close()