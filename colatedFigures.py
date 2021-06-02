# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:04:19 2021

@author: dmerr
"""


#from psychopy import sound
from __future__ import absolute_import, division, print_function
#from psychopy import visual, core, data, event, logging, gui, sound
from builtins import range
#from psychopy import *
import time
import numpy as np
from datetime import datetime
#import random
#import itertools
import pandas as pd

import matplotlib.pyplot as plt

import tkinter as tk

from sklearn import linear_model
from scipy.special import expit
from cycler import cycler
import math

frameLabel = ['right', 'left']


PSEResults = pd.concat(pd.read_excel('PSEAll2.xlsx', sheet_name=None), ignore_index=True)

observers  = PSEResults['baseName'].value_counts()
sizeSeq1 = [0.40, 0.55, 0.70, 0.85, 1, 1.15, 1.30, 1.45, 1.60]

PSERH = pd.DataFrame()

for obsI in observers.index:

    plt.figure(figsize=(12,12))
    plt.title(' PSE ')
    
    PSEResultsR = PSEResults[((PSEResults['mod'] == 1)& (PSEResults['baseName'] ==  obsI))]
    PSEResultsL = PSEResults[((PSEResults['mod'] == -1)& (PSEResults['baseName'] ==  obsI))]
    
    adapt = PSEResultsR.pse[:]-PSEResultsL.pse[:]
    
    PSERH[obsI]= PSEResultsR['pse'].values-PSEResultsL['pse'].values
    
    
    
    plt.plot(PSEResultsR.angle, PSEResultsR.pse, linewidth=1, label=frameLabel, color = 'blue')
    plt.plot(PSEResultsL.angle, PSEResultsL.pse, linewidth=1, label=frameLabel, color = 'red')
    plt.yticks(sizeSeq1)
    plt.ylabel('PSE')
    plt.xlabel('Angle')
    plt.savefig('PSE All')
    
    
    plt.figure(figsize=(12,12))
    plt.plot(PSEResultsR.angle, PSEResultsR.slopeHack, linewidth=1, label=frameLabel, color = 'blue')  
    plt.plot(PSEResultsL.angle, PSEResultsL.slopeHack, linewidth=1, label=frameLabel, color = 'red')            
    plt.title(' Slope Around the PSE ')     
    plt.ylabel('(y2-y1)/(x2-x1)')
    plt.xlabel('Angle')   
    plt.savefig('PSE Slope All')      
        #plt.show()
    

