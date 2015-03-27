#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : https_post.py
'''Purpose : add python3支持                                 '''
# Creation Date : 1427467785
# Last Modified :
# Release By : Doom.zhou


from requests import get
import re


if __name__ == '__main__':
    pass


class GetWanIp:
    def getip(self):
        try:
            wanip = self.visit("http://ip.taobao.com/service/getIpInfo.php?ip=myip")
        except:
           try:
               wanip = self.visit('http://ifconfig.me/ip')
           except:
               print("wanip is Error")
               wanip = '127.0.0.1'
        return wanip

    def visit(self, url):
        r = get(url, timeout = 5)
        r.encoding = 'utf-8'
        return re.search('(\d+\.){3}\d+', r.text).group(0)

def showhelp():
    print('------------------------------------help-------------->')
    print(GetWanIp().getip())
    pass


serverip = showhelp()
