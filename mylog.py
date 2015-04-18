#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : test.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1424949882
# Last Modified :
# Release By : Doom.zhou

import logging

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] \
        [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.WARNING)

fileHandler = logging.FileHandler("{0}/{1}.log".format('./', 'log'))
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
