# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:14:09 2018

@author: 11796
"""

import requests
params = {'email_addr': 'ryan.e.mitchell@gmail.com'}
r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data=params)
print(r.text)