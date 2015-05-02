#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : zhihu.py
'''Purpose : Intro sth                                 '''
# Creation Date : 2015-02-05
# Last Modified :
# Release By : Doom.zhou


import sys
import requests
from bs4 import BeautifulSoup
from mylog import logging


PASS = ''


def login():
    url = 'http://www.zhihu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:35.0)\
                Gecko/20100101 Firefox/37.0',
        'Accept': 'text/html,application/xhtml+xml,\
                application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://www.zhihu.com/',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
    s = requests.session()
    s.headers = headers
    r = s.get(url)
    soup = BeautifulSoup(r.text)
    dxsrf = soup.select('div form input:nth-of-type(6)')[0]['value']
    data = {
        '_xsrf': dxsrf,
        'email': 'zzepaigh@gmail.com',
        'password': PASS,
        'rememberme': 'y'}
    logurl = 'http://www.zhihu.com/login'
    r1 = s.post(logurl, data=data)
    r = s.get('http://www.zhihu.com/inbox')
    print(r1.content)
    print(r.url)
    pass


if __name__ == '__main__':
    if PASS == '':
        logging.warning('Input your Zhihu password first')
        sys.exit(0)
    else:
        login()
