#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import smtplib
import sys
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart('alternative')

data = sys.stdin.readlines()
k = 0
for i in data:
    if re.search(r'User-Agent: M', i):
        break
    k += 1

bdata, adata = data[:k], data[k+1:]
print bdata

content = '\n'.join(adata)
for i in bdata:
    if re.match(r'Date:(.*)', i):
        msg['Date'] = re.match(r'Date:(.*)', i).group(1)
    if re.match(r'Subject:(.*)', i):
        msg['Subject'] = re.match(r'Subject:(.*)', i).group(1)
    if re.match(r'To:(.*)', i):
        msg['To'] = re.match(r'To:(.*)', i).group(1)
    if re.match(r'Cc:(.*)', i):
        msg['Cc'] = re.match(r'Cc:(.*)', i).group(1)
msg['From'] = 'xx@goo6le.com'
toaddr = msg['To'].split(',') + msg['Cc'].split(',')



msg.attach(MIMEText(content, 'plain'))

s = smtplib.SMTP_SSL('smtp.exmail.qq.com', port=465)
s.login(msg['From'], 'xxxx')
s.sendmail(msg['From'], toaddr,  msg.as_string())
s.quit()
