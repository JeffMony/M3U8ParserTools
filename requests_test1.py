#!/usr/bin/python

import requests

hls_file_path='/home/jeffmony/developer/python/hls_list.txt'
dest_hls_type_file_path='/home/jeffmony/developer/python/hls_type.txt'

file = open(hls_file_path)
dest_file = open(dest_hls_type_file_path, 'a')
line = file.readline()
while line:
    line=line[:len(line)-1]
    try:
        request=requests.get(line, timeout=10)
        code=request.status_code
        if (code==200):
            dest_file.write(line+'\n')
    except:
        print 'unknown'
    line = file.readline()

file.close()
dest_file.close()
