# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:10:38 2018

@author: 11796
"""

from PIL import Image, ImageFilter

kitten = Image.open("kitten.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("kitten_blurred.jpg")
blurryKitten.show()
