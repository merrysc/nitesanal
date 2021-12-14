
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


# General a toy dataset:s it's just a straight line with some Gaussian noise:
xFmin, xFmax = 0, 120*60
# n_samples = 100
# np.random.seed(0)
# X = np.random.normal(size=n_samples)
# y = (X > 0).astype(float)
# X[X > 0] *= 4
# X += .3 * np.random.normal(size=n_samples)

# X = X[:, np.newaxis]

xFmin, xFmax = 0, 120*60
# n_samples = 100
# np.random.seed(0)
# X = np.random.normal(size=n_samples)
# y = (X > 0).astype(float)
# X[X > 0] *= 4
# X += .3 * np.random.normal(size=n_samples)

# X = X[:, np.newaxis]



baseName= 'PVMallFilesCol'
#fstFrame = 29

stimLength =[2]

### left or right of the screen for the stimulus
mod = [1, -1]
labelM = ['right', 'left']
angleSeq = [0,10,20,30,40,50]

sizeSeq1a=[0.55, 0.70, 0.85, 1, 1.15, 1.30, 1.45]
#sizeSeq1b =[0.40, 0.55, 0.70, 0.85, 1, 1.15, 1.30, 1.45, 1.60]

b = baseName + '.csv'

        #angleSeq = [60,70,80]
#dataExM = pd.read_excel(b)      

dataExM = pd.read_csv(b)  





fI =1

for modN in mod:
    
    
    

    dataEx = dataExM.loc[dataExM['mod'] == modN]
    
    if modN == 1:
        truePos1= dataEx[((dataEx['stimChose_mean'] == 1)  & (dataEx['biggerStim_mean'] ==  1) & (dataEx['sizeSeq1'] !=  1))]
        falsePos1 = dataEx[((dataEx['stimChose_mean'] == 1)  & (dataEx['biggerStim_mean'] == -1)& (dataEx['sizeSeq1'] !=  1))] 
        tpOfp1 = len(truePos1)/len(falsePos1)
    else:
        truePos2= dataEx[((dataEx['stimChose_mean'] == 1)  & (dataEx['biggerStim_mean'] ==  1)& (dataEx['sizeSeq1'] !=  1))]
        falsePos2 = dataEx[((dataEx['stimChose_mean'] == 1)  & (dataEx['biggerStim_mean'] == -1)& (dataEx['sizeSeq1'] !=  1))]
        tpOfp2 = len(truePos2)/len(falsePos2)
    for angleSeqN in angleSeq:
        
        
        justAng = dataEx.loc[dataEx['angleSeq'] == angleSeqN]
        if angleSeqN < 60:
            sizeSeq1 = sizeSeq1a
        else:
            sizeSeq1 = sizeSeq1b    
        
        for sizeN in sizeSeq1:
            sizeAng = justAng.loc[justAng['sizeSeq1'] == sizeN]
            #timebefore_mean = justAng.loc[justAng['timebefore_mean'] == fstFrameN]
            #frameStim_mean = justAng.loc[justAng['frameStim_mean'] == fstFrameN]
            #Resp_mean = justAng.loc[justAng['Resp_mean'] == fstFrameN]
            
            totalC = sizeAng.loc[sizeAng['stimChose_raw'] == 1]
            countCa = len(totalC)
                        
            
            if countCa == 0:
                percentS = 0
                 
            else:
                percentS = countCa/len(sizeAng)
            
            
            d = {'mod':modN, 'angleSeq': angleSeqN, 'sizeN': sizeN,'percentS': percentS, 'Observer': b} #"timebefore_mean": timebefore_mean, 'Resp_mean': Resp_mean, 'frameStim_mean':frameStim_mean
            
            if fI ==1:
                results = pd.DataFrame(d, index = [0])
                fI =2
            
            else:
                results = results.append(d, ignore_index = True)
            
        
    
c = baseName + '_results.csv' 
results.to_csv(c)

sampleRate = 15000
X_test = np.linspace(0.3, 1.7, sampleRate)
plt.title(baseName)
plt.figure(figsize=(12,12))

cmap=plt.cm.Dark2
c2 = cmap(np.linspace(0,1,14)) 
newI=1

fI=1

plt.xticks(sizeSeq1)
plt.yticks([0, 0.5, 1])
plt.ylim(-.25, 1.25)
        #plt.xlim(0, 120*60)
  
plotCo = 1


for angleSeqN in angleSeq:
    for modN in mod:
        if angleSeqN < 60:
            sizeSeq1 = sizeSeq1a
        else:
            sizeSeq1 = sizeSeq1b    
        
        colorZ = c2[newI]
        newI = newI+1
        
        #sizePlot = results.loc[results['angleSeq'] == angleSeqN] and results.loc[results['angleSeq'] == angleSeqN]
        
        sizePlot = results[((results['mod'] == modN)  & (results['angleSeq'] ==  angleSeqN))]
       # sizePlot[(df>=0)&(df<=20)].dropna()
        
        justAng = dataExM.loc[(dataExM['angleSeq'] == angleSeqN) & (dataExM['mod'] == modN)]
        # xFloatffs = range(0,2*10)
        # xFloatffs = xFloatffs/10
        
       
        
        X= pd.DataFrame.to_numpy(justAng.sizeSeq1)
        y =  pd.DataFrame.to_numpy(justAng.stimChose_raw)
        #trueX = pd.DataFrame.to_numpy(justAng.timebefore_mean)
        X = X.reshape(-1,1)
    #y = y.reshape(-1,1)
        #trueX = trueX.reshape(-1,1)
    
        X =X
    
        
    
    
    # Fit the classifier
    ####NOTE BECAUSE IT DOES MOD FIRST THIS DOES WORK! SHIFT Pleaase thanks
        if modN ==1:
            clf = linear_model.LogisticRegression(penalty='none')
            #clf = linear_model.LogisticRegression()
            clf.fit(X, y)
        
            tClf =  linear_model.LogisticRegression(penalty='none')
            #tClf.fit(trueX, y)
        
        # and plot the result
            #plt.figure(1, figsize=(4, 3))
            #plt.clf()
        
            
        
            loss = expit(X_test * clf.coef_ + clf.intercept_).ravel()
        else:
            clf1 = linear_model.LogisticRegression(penalty='none')
            #clf = linear_model.LogisticRegression()
            clf1.fit(X, y)
        
            tClf1 =  linear_model.LogisticRegression(penalty='none')
            #tClf.fit(trueX, y)
        
        # and plot the result
            #plt.figure(1, figsize=(4, 3))
            #plt.clf()
        
            
        
            loss1 = expit(X_test * clf1.coef_ + clf1.intercept_).ravel()
            
            #lossMean = mean()
    
        #lossT = expit(X_test * tClf.coef_ + tClf.intercept_).ravel()
        plt.subplot(2, 3, plotCo)
        
        if modN ==1:
            plt.scatter(sizePlot.sizeN, sizePlot.percentS, label='right') #, color = colorZ
            
            pseHack = loss  
        else:
            pseHack=loss1
        frameLabel = 'Angle ' + str(angleSeqN)
        plt.ylabel('Stim Selected')
        plt.xlabel('Stim Size Ratio')
       
        
        plt.title(baseName + str(angleSeqN))      
        if modN == -1:
            plt.scatter(sizePlot.sizeN, sizePlot.percentS, label='left') #, color = colorZ
            #
          #plt.plot(X_test, loss, linewidth=1, label=frameLabel, color = colorZ)
            plt.fill_between(X_test,loss,loss1,   where=loss1 >= loss, facecolor='red', alpha=0.4)
            plt.fill_between(X_test,loss,loss1,   where=loss1 < loss, facecolor='blue', alpha=0.4)
           #plt.ax.fill_betweenx(y, x1, x2, where=x2 >= x1, facecolor='green')
           #plt.ax.fill_betweenx(y, x1, x2, where=x2 <= x1, facecolor='red')
            plotCo = plotCo+1
            plt.plot(X_test, loss1,'--', linewidth=1, color = 'red')
            plt.plot(X_test, loss,'--', linewidth=1, color = 'blue')
            plt.legend()
        
      
    
        #pseTotals = [i for i in loss if i >= 0.5]
        #pseNew=  next(i for i in loss if i > 0.5)
      
        pseI =np.where(pseHack>0.5)
        
        pse=X_test[pseI[0][0]]
        x1i = pseI[0][0]+200
        
        x1 = pseI[0][0]-200
        x2 = pseI[0][0]+200
        y1 = pseHack[x1]
        y2 = pseHack[x2]
        
        slopeHack = (y2-y1)/(x2-x1)*sampleRate/2
       
        
        e= {'mod':modN, 'pse':  pse, 'angle': angleSeqN, 'slopeHack':slopeHack} 
            
        if fI ==1:
            PSEResults = pd.DataFrame(e, index = [0])
            fI =2
            
        else:
            PSEResults = PSEResults.append(e, ignore_index = True)
        
    
    #plt.tight_layout()

plt.savefig(baseName+ 'angleSeq')
f = baseName + '_PSEresults.csv'     
PSEResults.to_csv(f)        


plt.figure(figsize=(12,12))
plt.title(baseName + ' PSE ')

PSEResultsR = PSEResults[(PSEResults['mod'] == 1)]
PSEResultsL = PSEResults[(PSEResults['mod'] == -1)]

adapt = PSEResultsR.pse[:]-PSEResultsL.pse[:]


plt.plot(PSEResultsR.angle, PSEResultsR.pse, linewidth=1, label=frameLabel, color = 'blue')
plt.plot(PSEResultsL.angle, PSEResultsL.pse, linewidth=1, label=frameLabel, color = 'red')
plt.yticks(sizeSeq1)
plt.ylabel('PSE')
plt.xlabel('Angle')
plt.savefig(baseName+ 'PSE')


plt.figure(figsize=(12,12))
plt.plot(PSEResultsR.angle, PSEResultsR.slopeHack, linewidth=1, label=frameLabel, color = 'blue')  
plt.plot(PSEResultsL.angle, PSEResultsL.slopeHack, linewidth=1, label=frameLabel, color = 'red')            
plt.title(baseName + ' Slope Around the PSE ')     
plt.ylabel('(y2-y1)/(x2-x1)')
plt.xlabel('Angle')   
plt.savefig(baseName+ 'PSE Slope')      
    #plt.show()
    


        

