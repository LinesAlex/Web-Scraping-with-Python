# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:38:54 2018

@author: 11796
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")#/chapter1
#print(str(textPage.read(), 'utf-8'))

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, 'html.parser')
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
#print(content)
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
#print(content)