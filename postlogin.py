#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : postlogin.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1429099909
# Last Modified :
# Release By : Doom.zhou


import requests
import sys
from bs4 import BeautifulSoup
import logging


try:
    import http.client as http_client
except ImportError:
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1
logging.basicConfig() 
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
url = 'https://172.16.128.12/login.php?bodyY=521&bodyX=1678'
form_data = {
        'name': 'zhoulifeng582',
        'password': '5yixbDf6',
        'rule_0': '1',
        'rule_1': '1',
        'rule_2': '1',
        'rule_3': '0',
        'auto_len': '23',
        'min_len': '6',
        'Submit': b'\xb5\xc7 \xc2\xbc'
        }
cookies = {'sdmenu_my_menu': '1000000', 'PLDSSID': 'a2laucg5dc571oldi0vp4e8440'}
s = requests.session()
s.verify = False
s.headers = headers
s.post(url, cookies=cookies, data=form_data)
r = s.get('https://172.16.128.12/module/cmd/realtime_report.txt?xy=1429162541', cookies=cookies)
print('doom')
print(r.text)
s.close()
r = s.get('https://172.16.128.12/module/cmd/realtime_report.txt?xy=1429162541', cookies=cookies)
print('doom')
print(r.text)














sys.exit(0)

