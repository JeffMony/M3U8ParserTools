#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 解析video-url-except-blob.txt 中response code =200的数据

import sys
import requests
import os

reload(sys)
sys.setdefaultencoding('utf8')

def responseOk(url):
    try:
        request=requests.get(url, timeout=10)
        code=request.status_code
        return code
    except:
        return -100


file_path=os.getcwd()+'/txtfiles/'
video_file_except_blob_name = file_path + '/video-url-except-blob.txt'
video_url_except_blob_file = open(video_file_except_blob_name, 'r')

video_url_200_file = open(file_path + '/video-url-200.txt', 'w')

line=video_url_except_blob_file.readline()
while line:
    url=line[:len(line)-1]
    code=responseOk(url)
    if code==200:
        video_url_200_file.write(url+'\n')
    print code, '<---->', url
    line=video_url_except_blob_file.readline()

video_url_except_blob_file.close()
video_url_200_file.close()