# -*- coding:utf-8 -*-

# Copyright(C), 2020-2020,  Co.,Ltd.
# ProjectName : flaskTemplate
# FileName : semail.py
# Author : lvyandi
# Version : 0.10
# Date : 2020-07-14 10:10:11
# Description :
import smtplib
from email.mime.text import MIMEText


def s_email(sender,sender_pwd,receiver,subject,body,port=465,host='smtp.163.com'):
    msg = MIMEText(body, 'html')
    msg['subject'] = subject
    msg['from'] = sender
    msg['to'] = ",".join(receiver)
    s = smtplib.SMTP_SSL(host, port)
    s.ehlo_or_helo_if_needed()
    s.login(sender, sender_pwd)
    s.sendmail(sender, receiver, msg.as_string())
    s.close()


if __name__ == '__main__':
    # shou quan ma
    s_email('13384028757@163.com','CBVRANJUYSJLYQVT','2274361456@qq.com','xitongyijing','shixitongyujinga')