# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:56:11 2018

@author: 11796
"""

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()
