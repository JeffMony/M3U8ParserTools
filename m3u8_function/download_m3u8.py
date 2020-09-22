#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urlparse
import re

URL = 'http://video.yjf138.com:8091/20180812/6yl0Q2YZ/1500kb/hls/bm02h76314876.ts'

request = requests.get(URL, timeout=20)
with open('test.ts', 'wb') as output:
    output.write(request.content)