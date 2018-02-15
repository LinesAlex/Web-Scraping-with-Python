# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 11:10:26 2018

@author: 11796
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

def cleanInput(Input):
    Input = re.sub('\n+', ' ', Input)
    Input = re.sub('\[[0-9]*\]', ' ', Input)
    Input = re.sub(' +', ' ', Input)
    Input = bytes(Input, 'utf-8')
    Input = Input.decode('ascii', 'ignore')
    cleanInput = []
    Input = Input.split(' ')
    for item in Input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput
def ngrams(Input, n):
    Input = cleanInput(Input)
    output = []
    for i in range(len(Input) - n + 1):
        output.append(Input[i:i+n])
    return output

if __name__ == "__main__":
    html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
    bsObj = BeautifulSoup(html, 'html.parser')
    content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
    ngrams = ngrams(content, 2)
    print(ngrams)
    print("2-grams count is : " + str(len(ngrams)))