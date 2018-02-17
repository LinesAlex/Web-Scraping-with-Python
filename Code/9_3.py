# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:47:08 2018

@author: 11796
"""

import requests
files = {'uploadFile': open('../files/Python-logo.png', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php", files=files)
print(r.text)