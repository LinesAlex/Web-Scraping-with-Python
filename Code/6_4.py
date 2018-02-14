# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:54:23 2018

@author: 11796
"""

from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode("ascii","ignore")
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)

print(dictReader.fieldnames)

for row in dictReader:
    print(row)
