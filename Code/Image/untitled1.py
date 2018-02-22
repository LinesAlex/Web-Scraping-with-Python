# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:13:46 2018

@author: 11796
"""

from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
    
    image = Image.point(['tesseract', newFilePath, 'output'])
    image.save(newFilePath)
    
    outputFile = open('output.txt', 'r')
    print(outputFile.read())
    outputFile.close()

cleanFile('text_2.jpg', 'text_2_clean.png')

    