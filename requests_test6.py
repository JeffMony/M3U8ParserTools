#!/usr/bin/python

import requests
import threading

file_path='/home/jeffmony/developer/python/test.txt'

class my_thread (threading.Thread):
    def __init__(self, list):
        threading.Thread.__init__(self)
        self.list = list
    def run(self):
        process_data(self.list)


def get_mime_type(url):
    try:
        request = requests.get(url, timeout=10)
        return request.headers['Content-Type']
    except:
        print url
        return 'unknown'

def process_data(list):
    dict={}
    for url in list:
        mime_type=get_mime_type(url)
        if dict.__contains__(mime_type):
            count=dict.get(mime_type)
            count+=1
            dict[mime_type]=count
        else:
            dict[mime_type]=1
    print(dict)

line_count=0
url_list=[]
file=open(file_path,'r')
line=file.readline()
while line:
    if line_count<50:
        url=line[:len(line)-1]
        url_list.append(url)
    else:
        thread=my_thread(url_list)
        thread.start()
        thread.join()
        line_count=0
        url_list=[]
    line_count+=1
    line=file.readline()

if len(url_list) > 0:
    thread=my_thread(url_list)
    thread.start()
    thread.join()
    url_list=[]

file.close()
