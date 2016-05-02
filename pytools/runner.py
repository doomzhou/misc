#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : runner.py
'''Purpose : 模拟kde runner ALT+F2 
requirement:
    tkinter
    tk
'''
# Creation Date : 1462173892
# Last Modified :
# Release By : Doom.zhou
###############################################################################


import os
from tkinter import  Text, Button, Tk, INSERT

root = Tk()

def call():
    tv = text.get("1.0", 'end-1c')
    os.system("%s &" % tv)
    root.quit()

text = Text(root , height = 2, width = 30)
text.focus_force()


button = Button(root, height=2,command=call, width=20,text="Submit")
text.bind('<Return>', lambda e: call())
root.bind('<Escape>', lambda e: root.quit())

text.pack()
button.pack()

root.mainloop()


if __name__ == '__main__':
    pass
