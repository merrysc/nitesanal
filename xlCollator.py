# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 09:37:22 2021

@author: dmerr
"""

import glob
import numpy as np
import pandas as pd
import os 

directoryName = 'supine/pvm'

os.chdir(directoryName )

fileList = []
dataNew = []
for file in glob.glob("*.xlsx"):
    fileList.append(file)
    
    
    indexI = len(fileList)
    
i =0
while i < indexI:
    baseName = fileList[i]
    dataEx = pd.read_excel(baseName)   
    
    dataEx = dataEx[0:len(dataEx)-5]
    #-5 to account for the metadata
    
    dataNew.append(dataEx)
    
    i = i+1


dataG = pd.concat(dataNew)

    
# c = directoryName  + 'allFilesCol.csv' 

c = 'PVMallFilesCol.csv' 
dataG.to_csv(c)