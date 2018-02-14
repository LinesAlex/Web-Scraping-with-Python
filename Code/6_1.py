# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:30:31 2018

@author: 11796
"""

from urllib.request import urlopen
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")#/chapter1
print(textPage.read())