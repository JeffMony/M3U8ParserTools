#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 剔除video-url-all.txt中的blob:的 video url数据

import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')


file_path=os.getcwd()+'/txtfiles/'
video_file_name=file_path + 'video-url-all.txt'
video_file_except_blob_name = file_path + '/video-url-except-blob.txt'
video_url_except_blob_file = open(video_file_except_blob_name, 'w')

video_url_file = open(video_file_name, 'r')
line=video_url_file.readline()
while line:
    url=line[:len(line)-1]
    if not(url.startswith('blob:')):
        video_url_except_blob_file.write(url+'\n')
    line=video_url_file.readline()

video_url_file.close()
video_url_except_blob_file.close()