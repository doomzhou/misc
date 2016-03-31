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
import os
import time
import random
import json
import sys
import re
from bs4 import BeautifulSoup

proxies = {
        #'http': 'http://120.198.231.22:8080'
        'http': 'http://120.52.73.149:8088'
    }
headers = {
    'User-Agent': 'Mozilla/5.0\
    (X11; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
    'Accept': 'text/html\
    ,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def main():
    start = 1439427
    end = 925000
    gugufilename = './tmp/gugu.t'
    if os.path.exists(gugufilename):
        start = os.popen('tail -1 %s' % gugufilename).read().split()[0]
        start = int(start)
        pass
    else:
        with open(gugufilename, 'w') as f:
            f.write("%s,%s\n" % (start, end))

    url = 'http://gu-gu.com/chkqx2.aspx'
    showimgurl = 'http://gu-gu.com/ShowImg.aspx?filename=%s'
    randomnum = random.random()
    s = requests.session()
    s.proxies = proxies
    s.headers = headers

    if not is_proxy_ok(proxies['http'], s):
        print("proxies error exit")
        sys.exit(2)
    

    for i in range(start, end, -1):
        time.sleep(1 * random.random())         #sleep 3s
        form_data = {
            "Action": "post", "mpid": i,
            "ran": randomnum
        }
        pr = s.post(url, data=form_data)
        prkey = pr.text.split(":")[1]
        imgr = s.get(showimgurl % prkey)
        soup = BeautifulSoup(imgr.text, 'html.parser')

        with open(gugufilename, 'a') as ff:
            ff.write('%d %s\n' % (i, soup.find('img')['src']))
        #print(soup.find('img')['src'])

def is_proxy_ok(proxies, s):
    r = s.get('http://ipinfo.io/json')
    try:
        ip = json.loads(r.text)['ip']
    except:
        ip = "None"
    return re.findall(ip, proxies)


if __name__ == '__main__':
    main()
