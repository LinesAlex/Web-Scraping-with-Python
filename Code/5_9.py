# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:54:36 2018

@author: 11796
"""

import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = "An Email Alert"
    msg['From'] = "ryan@pythonscraping.com"
    msg['To'] = "webmaster@pythonscraping.com"

    s = smtplib.SMTP("localhost")
    s.send_message(msg)
    s.quit()

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
while(bsObj.find('a', {'id':'answer'}).attrs['title'] == 'NO'):
    print('It is not Christmas yet.')
    time.sleep(3600)
    bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
sendMail("It's Christmas!", "According to https://isitchristmas.com, it is Christmas!")
