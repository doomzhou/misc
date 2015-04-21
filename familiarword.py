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


def main(dlist, dwordsum, dlike=0):
    dword1 = dlist[0].upper()
    dword2 = dlist[1].upper()
    print(dword1)
    print(dword2)
    for i in range(len(dword1)):
        try:
            if dword1[i] == dword2[i]:
                dlike += 1
        except IndexError:
            pass
    return dlike / dwordsum


def sumord(word, sum=0):
    word = word.upper()
    for i in word:
        sum += ord(i)
    return sum

if __name__ == '__main__':
    if len(sys.argv[1:]) == 2:
        dwordsum = len(sys.argv[1] + sys.argv[2]) / 2
        ddiffnum = sumord(sys.argv[1]) - sumord(sys.argv[2])
        dresultlist = []
        for i in range(len(sys.argv[1])):
            for j in range(len(sys.argv[2])):
                if sys.argv[1][i] == sys.argv[2][j]:
                    dresultlist = [i, j]
                    break
            if dresultlist:
                break
        try:
            dper = main(
                [sys.argv[1][dresultlist[0]:], sys.argv[2][dresultlist[1]:]],
                dwordsum
                )
        except IndexError:
            dper = 0
            print('no same')
        if math.fabs(ddiffnum) <= 90 and dper >= 0.6:
            print('likely')
