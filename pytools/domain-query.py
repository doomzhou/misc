#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : domain-query.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1444094914
# Last Modified :
# Release By : Doom.zhou
###############################################################################


from selenium import webdriver
from mylog import logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import time

cssselector = 'div div div div ul li div span.status'


def getletter():
    return chr(random.randint(0, 26) + 97)


user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Archlinux) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Mozilla/5.0 (X11; " +
    "Linux x86_64;rv:35.0) Gecko/20100101 Firefox/35.0"
)
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent
driver = webdriver.PhantomJS(desired_capabilities=dcap)
for j in range(1, 500):
    i = getletter() + getletter() + getletter() + getletter()
    url = 'http://wanwang.aliyun.com/domain/searchresult/?keyword=%s&suffix=.com' % i
    time.sleep(1)
    try:
        driver.get(url)
        print(j, i)
        result = driver.find_element_by_css_selector(
                cssselector) .get_attribute('innerHTML')
        logging.warning('%s-%s' % (i, result))
    except Exception as e:
        driver.quit()
        driver = webdriver.PhantomJS(desired_capabilities=dcap)
        print(e)
