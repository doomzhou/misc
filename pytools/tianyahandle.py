#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : tianyahandle.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1430109197
# Last Modified :
# Release By : Doom.zhou
###############################################################################


import os
from glob import glob
from mylog import logging
import sqlite3


def main():
    os.chdir('/home/doom/Downloads')
    dlist = glob('tianya*')
    for i in range(len(dlist)):
        with open(dlist[i], 'r', encoding='gbk', errors='ignore') as f:
            dflist = f.read().splitlines()
        conn = sqlite3.connect('/home/doom/github/misc/data.sqlite3')
        cur = conn.cursor()
        for j in range(len(dflist)):
            logging.warning('%f*%f' % ((i+1)/len(dlist), j/len(dflist)))
            try:
                [a, b, c] = dflist[j].split()
                cur.execute(
                    'INSERT INTO items VALUES (?, ?, ?, ?)', (None, a, b, c))
            except Exception as e:
                logging.warning(e)
        conn.commit()
    conn.close()

if __name__ == '__main__':
    conn = sqlite3.connect('data.sqlite3')
    cur = conn.cursor()
    try:
        cur.execute(
            'create table items (id integer primary key autoincrement,\
username string, password string, email string)')
    except Exception as e:
        logging.warning(e)
    finally:
        cur.close()
    main()
