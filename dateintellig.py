#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : dateintellig.py
'''Purpose :
intelligence funciton for data
feature:
dateintellig timestamp to date
dateintellig date to timestamp
dateintellig last7day timestamp
dateintellig next7day timestamp
'''
# Creation Date : 1429505088
# Last Modified :
# Release By : Doom.zhou


import sys
from datetime import datetime, timedelta


TODAY = datetime.today().strftime('%Y-%m-%d')
TODAYtimestamp = datetime.strptime(TODAY, '%Y-%m-%d').strftime('%s')


def intelligdate():
    dreturn = []
    if len(sys.argv[1:]) > 1:
        dnum = int(sys.argv[2])
        if dnum >= 30:
            print('less than 30 better')
            dnum = 30
        if sys.argv[1] == 'next':
            did = (
                datetime.strptime(TODAY, '%Y-%m-%d') + timedelta(days=dnum)
                ).strftime("%s")
            dreturn.insert(0, dnum)
            dreturn.insert(1, did)
        elif sys.argv[1] == 'pre':
            did = (
                datetime.strptime(TODAY, '%Y-%m-%d') - timedelta(days=dnum)
                ).strftime("%s")
            dreturn.insert(0, dnum)
            dreturn.insert(1, did)
        return dreturn
    else:
        try:
            dtimestamp = int(sys.argv[1])
            returnstr = datetime.fromtimestamp(dtimestamp).\
                strftime('%Y-%m-%d %H:%M:%S')
            dreturn.append(returnstr)
            pass
        except:
            ddatetimestr = sys.argv[1]
            returnstr = datetime.strptime(
                    ddatetimestr, '%Y-%m-%d').strftime('%s')
            dreturn.append(returnstr)
            pass
    return dreturn


if __name__ == '__main__':
    if sys.argv[1:]:
        result = intelligdate()
        print(result)
    else:
        print('Usage: dateintellig.py params')
