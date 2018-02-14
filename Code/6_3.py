# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:48:13 2018

@author: 11796
"""

from urllib.request import urlopen
from io import StringIO
import csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode("ascii","ignore")
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

for row in csvReader:
    print(row)
