# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 21:32:00 2018

@author: 11796
"""

from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_paht='')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()