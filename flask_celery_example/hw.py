#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : hw.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1428545651
# Last Modified :
# Release By : Doom.zhou


from __future__ import absolute_import
from celery import Celery
from flask import Flask
from datetime import datetime
import time


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)


@celery.task(name="hw.fileh")
def fileh():
    time.sleep(2)
    f = open('1.t', 'a')
    f.write("%s\n" % str(datetime.now()))
    f.close()


@app.route('/')
def index():
    fileh.delay()
    try:
        with open('1.t', 'r') as lines:
            newlines = lines.read().splitlines()
    except Exception as e:
        print(e)
        newlines = 'nil '
        pass
    return str(newlines)


if __name__ == '__main__':
    app.run(debug=True)
