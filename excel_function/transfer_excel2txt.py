#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd
import sys
import requests

reload(sys)
sys.setdefaultencoding('utf8')

def responseOk(url):
    try:
        request=requests.get(url, timeout=10)
        code=request.status_code
        return code
    except:
        return -100

file_path='/Users/jeffmony/sources/M3U8ParserTools/excel_function/files/'

excel='video-url-all.xlsx'
video_url_200='video-url-200.txt'
video_url_other="video-url-other.txt"

excel_file_str=file_path+excel
excel_data = xlrd.open_workbook(excel_file_str)
table = excel_data.sheets()[0]
nrows = table.nrows

video_url_200_file=open(file_path+video_url_200, 'a')
video_url_other_file=open(file_path+video_url_other, 'a')

for index in range(1, nrows):
    item=table.cell(index,1).value
    code=responseOk(item)
    if code == 200:
        video_url_200_file.write(item+'\n')
    else:
        video_url_other_file.write(item+'\n')
    print code, '<---->', item

video_url_200_file.close()
video_url_other_file.close();