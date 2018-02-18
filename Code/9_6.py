# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:57:10 2018

@author: 11796
"""

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('ryan', 'password')
r = requests.post(url='http://pythonscraping.com/pages/auth/login.php', auth = auth)
print(r.text)

