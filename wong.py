#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : wong.py
'''Purpose : Fetch sth for wong '''
# Creation Date : 1429341643
# Last Modified :
# Release By : Doom.zhou


from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from myemail import mailsender
import sys
import time

def jpfetch(olditem):
    url = '''http://s.jipiao.trip.taobao.com/flight_search_result.htm?tripType=0&\
            depCityName=%C9%CF%BA%A3&depCity=&arrCityName=%BD%D2%D1%F4&arrCity=&\
            depDate=2015-04-21&arrDate='''

    driver = webdriver.PhantomJS()
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_class_name('text').click()
    soup = BeautifulSoup(driver.page_source)
    target = soup.select('table tbody tr td div div table tbody tr td a span')
    today = int(datetime.strftime(datetime.now(), '%d'))
    item = []
    for i in target:
        print(i)
        item.append({today: BeautifulSoup(str(i)).text})
        today += 1
    if olditem != item:
        mailsender(str(item), 'wong@gohjkl.com')
        return item
    else:
        print('no change')
        return olditem

if __name__ == '__main__':
    olditem = []
    while True:
        try:
            olditem = jpfetch(olditem)
        except Exception as e:
            print(e)
            pass
        time.sleep(300)
