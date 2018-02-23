# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:59:02 2018

@author: 11796
"""

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps

def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = Image.point(lambda x:0 if x<143 else 255)
    borderImage = ImageOps.expand(image, border=20, fill='white')
    borderImage.save(imagePath)

html = urlopen('http://www.pythonscraping.com/humans-only')
bsObj = BeautifulSoup(html, 'html.parser')
imageLocation = bsObj.find('img', {'title': 'Image CAPTCHA'})['src']
formBuildId = bsObj.find("input", {'name': 'form_build_Id'})['value']
captchaSid = bsObj.find('input', {'name': 'captcha_sid'})['value']
captchaToken = bsObj.find('input', {'name': 'captcha_token'})['value']

captchaUrl = 'http://pythonscraping.com' + imageLocation
urlretrieve(captchaUrl, 'captcha.jpg')
cleanImage('captcha.jpg')
p = subprocess.Popen(['tesseract', 'captcha.jpg', 'captcha'], stdout=subprocess.PIPE.stderr=subprocess.PIPE)
p.wait()
f = open('captcha.txt', 'r')

captchaResponse = f.read().replace(' ', '').replace('\n', '')
print('Captcha solution attempt: ' + captchaResponse)

if len(captchaResponse) == 5:
    params = {'captcha_token'：captchaToken
              , 'captcha_sid': captchaSid
              , 'form_id': 'comment_node_page_form'
              , 'form_build_id': formBuildId
              , 'captcha_response': captchaResponse
              , 'name': 'Ryan Mitchell'
              , 'comment_body[und][0][value]': '...and I am definitely not a bot'}
    r = requests.post('http://www.pythonscraping.com/commit/reply/10', data=params)
    responseObj = BeautifulSoup(r.text)
    if responseObj.find('div', {'class': 'messages'}) is not None:
        print(responseObj.find('div', {'class'：'messages'}).get_text())
else:
    print("There was a problem reading the CAPTCHA correctly!")

