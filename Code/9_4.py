# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:57:16 2018

@author: 11796
"""

import requests

params = {'username': 'Ryan', 'password': 'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("--------")
print("Going to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies = r.cookies)
print(r.text)
