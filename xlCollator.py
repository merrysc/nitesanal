# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 09:37:22 2021

@author: dmerr
"""

import glob

fileList = []
for file in glob.glob("*.xlsx"):
    fileList.append(file)
    
    
    indexI = len(fileList)
    
    for i in indexI:
        