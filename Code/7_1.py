# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 11:03:59 2018

@author: 11796
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
def ngrams(Input, n):
    Input = re.sub('\n+', " ", Input)
    Input = bytes(Input, "utf-8")
    Input = input.decode("ascii", "ignore")
    print(Input)
    Input = Input.split(' ')
    output = []
    for i in range(len(Input)-n+1):
        output.append(Input[i:i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, 'html.parser')
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print("2-grams count is : " + str(len(ngrams)))