#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : pyproysocket.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1457144359
# Last Modified :
# Release By : Doom.zhou
###############################################################################


import socket
import urllib.parse
import logging
import sys

logging.basicConfig(level=logging.INFO)


def to_bytes(s):    ##取自shadowsocks
    if bytes != str:
        if type(s) == str:
            return s.encode('latin-1')
    return s


def to_str(s):       ##取自shadowsocks
    if bytes != str:
        if type(s) == bytes:
            return s.decode('latin-1')
    return s

def server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(500)
    logging.info('Server start at %s:%d' % (host, port))
    while 1:
        try:
            conn, addr = s.accept()
            do_connection(conn)
        except KeyboardInterrupt:
            logging.info('Quit')
            break

def parse_header(raw_headers):
    logging.info('raw_headers: %s' % raw_headers)
    request_lines = raw_headers.split('\r\n')
    first_line = request_lines[0].split(' ')
    method = first_line[0]
    full_path = first_line[1]
    version = first_line[2]
    print("%s %s" % (method, full_path))
    (scm, netloc, path, params, query, fragment) \
        = urllib.parse.urlparse(full_path, 'http')

    i = netloc.find(':')
    if i >= 0:
        address = netloc[:i], int(netloc[i + 1:])
    else:
        address = netloc, 80
    return method, version, scm, address, path, params, query, fragment


def GET(conn, req_headers, address, path, params, query, method, version):
    path = urllib.parse.urlunparse(("", "", path, params, query, ""))
    req_headers = " ".join([method, path, version]) + "\r\n" +\
        "\r\n".join(req_headers.split('\r\n')[1:])
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        soc.connect(address)
    except Exception as e:
        conn.sendall(to_bytes("HTTP/1.1 Fail\r\n\r\n"))
        conn.close()
        soc.close()
    else:
        if req_headers.find('Connection') >= 0:
            req_headers = req_headers.replace('keep-alive', 'close')
        else:
            req_headers += req_headers + 'Connection: close\r\n'
        req_headers += '\r\n'
        soc.sendall(to_bytes(req_headers))
        data = ''
        logging.info('##################################################start')
        while 1:
            try:
                buf = to_str(soc.recv(8129))
                data += buf
            except:
                buf = None
            finally:
                if not buf:
                    soc.close()
                    break
        logging.info('data: %s' % data)
        conn.sendall(to_bytes(data))
        conn.close()


def CONNECT(conn, req_headers, address):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        soc.connect(address)
    except Exception as e:
        conn.sendall(to_bytes("HTTP/1.1 Fail\r\n\r\n"))
        conn.close()
        soc.close()
    else:
        conn.sendall(to_bytes('HTTP/1.1 200 Connection established\r\n\r\n'))
        try:
            while True:
                data = conn.recv(99999)
                soc.sendall(data)
                data = soc.recv(999999)
                conn.sendall(data)
        except:
            conn.close()
            soc.close()

def do_connection(conn):
    req_headers = to_str(conn.recv(8080))
    if req_headers is None:
        return
    method, version, scm, address, path, params, query, fragment = \
        parse_header(req_headers)
    if method == 'GET':
        GET(conn, req_headers, address, path, params, 
                query, method, version)
    elif method == 'CONNECT':
        address = (path.split(':')[0], int(path.split(':')[1]))
        CONNECT(conn, req_headers, address)

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8000         
    server(HOST, PORT)
