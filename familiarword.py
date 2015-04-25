#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : familiarword.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1429576218
# Last Modified :
# Release By : Doom.zhou
###############################################################################


import sys
import math
from mylog import logging


def main(dlist, dwordsum, dlike=0):
    dword1 = dlist[0].upper()
    dword2 = dlist[1].upper()
    for i in range(len(dword1)):
        try:
            if dword1[i] == dword2[i]:
                dlike += 1
        except IndexError:
            pass
    return [dlike / dwordsum, dwordsum]


def sumord(word, sum=0):
    word = word.upper()
    for i in word:
        sum += ord(i)
    return sum


def judge(dlist):
    if len(dlist) == 2:
        dwordsum = len(dlist[0] + dlist[1]) / 2
        ddiffnum = sumord(dlist[0]) - sumord(dlist[1])
        dresultlist = []
        for i in range(len(dlist[0])):
            for j in range(len(dlist[1])):
                if dlist[0][i] == dlist[1][j]:
                    dresultlist = [i, j]
                    break
            if dresultlist:
                break
        try:
            dper = main(
                [dlist[0][dresultlist[0]:], dlist[1][dresultlist[1]:]],
                dwordsum
                )
        except IndexError:
            dper = [0, 0]
        if math.fabs(ddiffnum) <= 90 and\
                (
                (dper[1] <= 3 and dper[0] > 0.67) or
                (dper[1] >= 4 and dper[0] >= 0.75) or
                dper[0] >= 8) and dper[0] != 1:
            return True
        return False

if __name__ == '__main__':
    if len(sys.argv[1:]) == 2:
        if judge(sys.argv[1:]):
            print('likely')
    else:
        with open('1.t', 'r') as newsf:
            dflist = newsf.read().splitlines()
        for i in range(len(dflist)):
            for j in range(len(dflist)):
                if judge([dflist[i], dflist[j]]):
                    print("%s---%s" % (dflist[i], dflist[j]))
                    logging.warning("%s---%s" % (dflist[i], dflist[j]))
                pass
