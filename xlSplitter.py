# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 12:17:37 2021

@author: dmerr
"""


from __future__ import absolute_import, division, print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn import linear_model
from scipy.special import expit
import os

xFmin, xFmax = 0, 120*60





FrameStim=[43,51, 59,67,75]
stimLength =[2]
### left or right of the screen for the stimulus
mod = [1, -1]
angleSeq = [0,10,20,30,40,50,60,80]
#angleSeq= [10,20,40,80]

directoryName = 'ljob2'

os.chdir(directoryName )


##loads up the spreadsheet
baseName ='ljob2allFilesCol'
b = baseName + '.csv'
dataEx = pd.read_csv(b)      
#dataEx = pd.read_excel(b)

advName = '2nd30'



#get column names from dataEx
1st30 = pd.DataFrame([])
2nd30 = pd.DataFrame

fI =1

for angleSeqN in angleSeq:
    justAng = dataEx.loc[dataEx['angleSeq'] == angleSeqN]
    
    
    for fstFrameN in FrameStim:
        sizeAng = justAng.loc[justAng['FrameStim'] == fstFrameN]
       
        xlsplit1 = sizeAng[0:30]
        xlsplit2 = sizeAng[30:60]

