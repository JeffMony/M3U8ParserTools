#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 将excel 中信息导入到 txt文件中
# video-url-all.xlsx是线上提取的视频url的汇总，非常重要的数据

import xlrd
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

file_path=os.getcwd()+'/excel_files/'

excel_name='video-url-all.xlsx'
video_url_all='video-url-all.txt'

excel_file_str=file_path+excel_name
excel_data = xlrd.open_workbook(excel_file_str)
table = excel_data.sheets()[0]
nrows = table.nrows

video_url_all_file=open(file_path+video_url_all, 'w')

for index in range(1, nrows):
    item=table.cell(index,1).value
    video_url_all_file.write(item+'\n')

video_url_all_file.close()