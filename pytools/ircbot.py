#!/usr/bin/python2
import socket
import sys
import os, time
from datetime import datetime

server = "irc.google.com"
channel = "#google"
username = "google"
pipe_name = "msgpipe"

def child():
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
    while True:
        time.sleep(1)
        os.write(pipeout, b'Number %03d\n' % counter)
        counter = (counter+1) % 5

def parent(channel):
    time.sleep(0.2)
    pipein = open(pipe_name, 'r')
    STARTMIN = datetime.now().minute
    while True:
        NOWMIN = datetime.now().minute
        if NOWMIN != STARTMIN:
            STARTMIN = NOWMIN
            print('%s Send PONG' % datetime.now())
            ircsock.send("PONG :irc.google.com")
        line = pipein.readline()[:-1]
        if not line.startswith("Number"):
            print('Parent got will send alarm: "%s"' % line)
            ircsock.send("PRIVMSG doomzh :hh\r\n")
            sendmsg(channel, line)

def ping(ircsock):
    data = ircsock.recv(512)
    print(data)
    if data.find('PING') != -1:
        ircsock.send('PONG %s' % data[5:])

def sendmsg(chan , msg):
    ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\r\n")

def joinchan(chan):
    ircsock.send("JOIN "+ chan +"\r\n")

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 8818))
ircsock.send('NICK %s\r\n' % (username,))
ping(ircsock)
ircsock.send('USER %s 8 * :%s\r\n' % (username, username))
ping(ircsock)
joinchan(channel)
sendmsg(channel, "Google welcome")

if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
pid = os.fork()
if pid != 0:
    parent(channel)
else:
    child()

ircsock.close()
