# -*- coding:utf-8 -*-
import smtplib
from email.mine.text import MIMEText
from email.header import Header

sender = '113067169@qq.com'
receiver = '1053372550@qq.com'
subject = 'python email test'
smtpserver = 'smtp.qq.com'
username = '113067169@qq.com'
password = 'mqfcu315'

msg = MIMEText('你好！', 'test', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
'''
msg = MIMEText('<html><h1>你好！</h1><html>', 'html', 'utf-8')
msg['Subject'] = subject
'''

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

