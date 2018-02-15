# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:30:22 2018

@author: 11796
"""

from urllib.request import urlopen
#from bs4 import BeautifulSoup
import re
import string
import operator

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
    output = {}
    for i in range(len(Input) - n + 1):
        ngramTemp = " ".join(Input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse = True)
print(sortedNGrams)