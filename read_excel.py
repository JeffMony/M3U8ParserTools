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

excel_file_path='/home/jeffmony/share/hls测试站点统计.xlsx'
dest_file_path='/home/jeffmony/developer/python/hls.txt'

excel_data = xlrd.open_workbook(excel_file_path)
table = excel_data.sheets()[0]
nrows = table.nrows


file = open(dest_file_path, 'a')

for index in range(1, nrows):
    item=table.cell(index,1).value
    code=responseOk(item)
    if code == 200:
        print item
        file.write(item+'\n')

file.close()