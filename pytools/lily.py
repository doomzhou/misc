#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : lily.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1427766502
# Last Modified :
# Release By : Doom.zhou


import requests
import sys
import imghdr


try:
    filename = str(sys.argv[1])
    imghdr.what(filename)
except Exception as e:
    plaint = ''
    for line in sys.stdin:
        plaint = plaint + line

    data = {'vimcn': plaint}
    print(requests.post('http://p.vim-cn.com/', data=data).text, end='')
    sys.exit(0)


imgdata = {'name': open(filename, 'rb')}
print(requests.post('http://img.vim-cn.com/', files=imgdata).text, end='')
