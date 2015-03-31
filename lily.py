#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : lily.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1427766502
# Last Modified :
# Release By : Doom.zhou


import requests
import sys
import os


cmd = str(sys.argv[1])
plaint = os.popen(cmd).read()
data = {'vimcn': plaint}
print(data)
print(requests.post('http://p.vim-cn.com/', data=data).text)
