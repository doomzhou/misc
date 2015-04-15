#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : postlogin.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1429099909
# Last Modified :
# Release By : Doom.zhou


import requests
import sys
import bs4


data = {'name': 'zhoulifeng582', 'password': '5yixbDf6'}
#data = {'name': 'zhoulifeng582', 'password': '5yixbDf6', 'rule_0': '1', 'rule_1': '1', 'rule_2': '1', 'rule_3': '0', 'auto_len': '23', 'min_len': '6', 'Submit': '%B5%C7+%C2%BC'}
payload = {'bodyY': 670, 'bodyX': 1364}
with requests.session() as c:
    c.get('https://172.16.128.12/', params=payload, verify=False)
    cookies = dict(c.cookies)
    print(cookies)
    c.post('https://172.16.128.12/login.php',cookies=cookies, data=data, params=payload, verify=False)
    r = c.get('https://172.16.128.12/index.php', verify=False)
    r.encoding='gb2312'
    print(r.text)
sys.exit(2)
#s = requests.session()

s.post(url='https://172.16.128.12/login.php?bodyY=273&bodyX=1364', cookies=cookies, params=payload, verify=False)
r = s.get('https://172.16.128.12/module/cmd/realtime_report.txt?xy=1429101927', cookies=cookies,  verify=False)
print(r.text)
