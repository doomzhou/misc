#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : crawl.py
'''Purpose : One for all website crawl
Require: 
requests
bs4
Myemail&mylog
'''
# Creation Date : 2015-19-04
# Last Modified : Sun 19 Apr 2015 07:16:19 AM CST
# Release By : Doom.zhou


import requests
import sys
import re
import time
import random
from bs4 import BeautifulSoup
from mylog import logging, rootLogger
from urllib.parse import urlsplit


url_list = []
domain_list = []
other_url = []
paf_pattern = re.compile('.*(pinganfang|anhouse).*')
SLEEP_TIME = 36
SLEEP_TIME_SALT = 18


def crawl(url):
    new_list = []
    if url is None:
        url = 'http://www.pinganfang.com'
    logging.info(url)
#   step1: fetch home_page
    s = requests.session()
    try:
        home_page = s.get(url)
    except:
        pass
    soup = BeautifulSoup(home_page.text)
    for i in soup.select('a'):
        try:
            url = i.attrs.get('href')
            if paf_pattern.match(url):
                if url not in url_list:
                    url_list.append(url)
                    new_list.append(url)
                domain = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
                if domain not in domain_list:
                    domain_list.append(domain)
            elif re.match('.*javascript.*', url):
                pass
            else:
                other_url.append(url)
        except:
            pass
    return new_list


def listtofile(flist):
    f = open('tmp/urllist.t', 'a')
    for i in flist:
        f.write("%s\n" % i)
    f.close()


if __name__ == '__main__':
    rootLogger.setLevel(logging.INFO)
    logging.info('main')
    url_list_main = []
    if len(sys.argv[1:]) == 0:
        logging.info("Usage: crawl <url>")
        url_list_main += crawl(None)
        listtofile(url_list_main)
        num = len(url_list_main)
        for i in url_list_main:
            listtofile(url_list_main[num:])
            num = len(url_list_main)
            url_list_main += crawl(i)
            time.sleep(SLEEP_TIME + random.randint(0, SLEEP_TIME_SALT))
    else:
        crawl(sys.argv[1:])
