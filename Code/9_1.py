# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:10:59 2018

@author: 11796
"""

import requests

params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)
