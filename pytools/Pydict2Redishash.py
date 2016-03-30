#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : Pydict2Redishash.py
'''Purpose : Python dict 2 Redis hash'''
# Creation Date : 1459380199
# Last Modified :
# Release By : Doom.zhou
###############################################################################



def d2h(conn, dictname, storedict):
    return conn.hmset(dictname, storedict)
