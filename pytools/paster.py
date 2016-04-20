#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : paster.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1460640480
# Last Modified :
# Release By : Doom.zhou
###############################################################################

from flask import Flask, request, redirect, url_for, jsonify, Response
from werkzeug import secure_filename
import os
import redis
import time
from random import random
from io import StringIO


UPLOAD_FOLDER = '/home/doom/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        conn = redis.StrictRedis(host='127.0.0.1')  
        file = request.files['data']
        stream = file.stream.read()
        if file and allowed_file(file.filename):
            filename = "%d-%s" % (int(time.time() * 1000), secure_filename(file.filename))
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            conn.hset('img',filename, stream)
            #return redirect(url_for('upload_file',
            #                        filename=filename))
            return '%s?filename=%s' % (request.url, filename)
    filename = request.args.get('filename')
    if filename:
        conn = redis.StrictRedis(host='127.0.0.1')  
        if conn.hexists('img', filename):
            #return jsonify({"status": 0, "msg": "Success", "url": "%s" % request.url})
            return Response(conn.hget('img', filename),mimetype='image/png')
        else:
            return jsonify({"status": 1, "msg": "Error"})
    return '''
<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form action="" method=post enctype=multipart/form-data>
<p><input type=file name=data>
    <input type=submit value=Upload>
</form>
    '''

@app.route('/paster', methods=['GET', 'POST'])
def paster():
    if request.method == 'POST':
        conn = redis.StrictRedis(host='127.0.0.1')  
        text = request.form['text']
        if text:
            pastername  = "%d-%d" % (int(time.time() * 1000), int(random() * 1000))
            conn.hset('pas', pastername, text)
            return '%s?pastername=%s' % (request.url, pastername)
    pastername = request.args.get('pastername')
    if pastername:
        conn = redis.StrictRedis(host='127.0.0.1')  
        if conn.hexists('pas', pastername):
            #return jsonify({"status": 0, "msg": "Success", "url": "%s" % request.url})
            return Response(conn.hget('pas', pastername), mimetype='text/plain')
        else:
            return jsonify({"status": 1, "msg": "Error"})
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <form action="" method=post enctype=multipart/form-data>
            <textarea value="" name="text" placeholder="请输入" rows="4" cols="50"></textarea> 
            <br>
            <input type=submit value=Submit>
        </form>
    </body>
    </html>
'''
    pass

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
