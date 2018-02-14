# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:51:13 2018

@author: 11796
"""

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Alert"
msg['From'] = "ryan@pythonscraping.com"
msg['To'] = "webmaster@pythonscraping.com"

s = smtplib.SMTP("localhost")
s.send_message(msg)
s.quit()
