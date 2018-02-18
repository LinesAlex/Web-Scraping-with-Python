# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:10:09 2018

@author: 11796
"""

import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mas OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml, application/xml; q=0.9, image/webp, */*, q=0.8'}
url = 'http://www.whaismybrowser.com/developers/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)

bsObj = BeautifulSoup(req.text)
print(bsObj.find('table', {'class': 'table-striped'}).get_text)
