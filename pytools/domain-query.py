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
import random
import time

cssselector = 'div div div div ul li div span.status'


def getletter():
    return chr(random.randint(0, 26) + 97)


driver = webdriver.PhantomJS()
while True:
    i = getletter() + getletter() + getletter() + getletter()
    url = 'http://wanwang.aliyun.com/domain/searchresult/?keyword=%s&suffix=.com' % i
    time.sleep(1)
    try:
        driver.get(url)
        result = driver.find_element_by_css_selector(
                cssselector) .get_attribute('innerHTML')
        logging.warning('%s-%s' % (i, result))
    except Exception as e:
        driver.quit()
        driver = webdriver.PhantomJS()
        print(e)
