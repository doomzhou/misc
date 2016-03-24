#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : gugu.py
'''Purpose : gugu'''
# Creation Date : 1458809690
# Last Modified :
# Release By : Doom.zhou
###############################################################################


import requests
import random
from bs4 import BeautifulSoup

proxies = {
        'http': 'http://203.195.160.14:8080'
    }

def main():
    url = 'http://gu-gu.com/chkqx2.aspx'
    showimgurl = 'http://gu-gu.com/ShowImg.aspx?filename=%s'
    randomnum = random.random()
    s = requests.session()
    s.proxies = proxies
    form_data = {
        "Action": "post", "mpid": '1411600',
        "ran": randomnum
    }
    pr = s.post(url, data=form_data)
    prkey = pr.text.split(":")[1]
    imgr = s.get(showimgurl % prkey)
    soup = BeautifulSoup(imgr.text, 'html.parser')
    print(soup.find('img')['src'])




if __name__ == '__main__':
    main()
