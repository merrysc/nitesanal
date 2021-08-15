#from psychopy import sound
from __future__ import absolute_import, division, print_function
from psychopy import visual, core, data, event, logging, gui, sound
from builtins import range
#from psychopy import *
import time
from numpy import arange, random, transpose, meshgrid, roll, concatenate, reshape, pi, sin
from datetime import datetime
#import random
#import itertools
import pandas as pd
import sounddevice as sd
import soundfile as sf
import argparse
import matplotlib.pyplot as plt

frameTimesAll = pd.DataFrame()

simpleK, audSamp = sf.read('oneKHz33ms.wav')


# GUI parameters

params = {'Observer': 'pvm'}

paramsDlg = gui.DlgFromDict(dictionary=params, title='VernierBisection', fixed=[])

# Values for gamma correction
gamma = [2.052043344, 2.100525447, 2.445199413]
##Check these against mine from DW's scripts

#cheatT = pd.DataFrame()

if paramsDlg.OK:

    print(params)

else: 
    core.quit();print('User Cancelled')

# class sound.backend_sounddevice:
#     def 
    
#     SoundDeviceSound(self):
#         setSound(value=10000, secs=0.5, octave=4, hamming=None, log=True)



DEBUG=False

if DEBUG:
    
    ### change me to your resolution
    xFov = 2560
    winSize=(xFov,1440)
    win = visual.Window(size=winSize, monitor='testMonitor',units='pix',bitsMode=None,allowGUI=False, winType='pyglet')	

else:
    xFov = 5760
    winSize=(xFov,1200)
    win = visual.Window(size=winSize,units='pix',bitsMode=None,allowGUI=False, winType='pyglet',fullscr=True)	
#debug set to my home comp if false set to their screen check this






# Additional parameters

params['Env_SD'] = 10

params['dateStr'] = time.strftime("%b_%d_%H%M", time.localtime())#add the current time



# window for drawing stimuli




##Have altered code to use oneDegree, means that this will need rounding however
oneDegree = xFov/180






## sets up the mouse currently at 0.0


###this is a lazy way of adding to the stimArray.  For two reps make it [1, 2] etc etf
repNo = list(range(1,6))
#fstFrame = list(range(5,117))


FrameStim=[43,51,59, 67,75]

#fstFrame = 29

stimLength =[2]

### left or right of the screen for the stimulus
mod = [1, -1]


#if not left or right use this one
#mouseSeq = [-20*oneDegreeR, -10*oneDegreeR, 10*oneDegreeR, 20*oneDegreeR]


#if left to right use this one (note sq so double reps)


## mouseSeq no longer used in experiment, however to play nice with analysis have left it in
#mouseSeq = [round(-5*oneDegree), round(5*oneDegree)]

##can range this for fine detail too
#angleSeq = [0, 10, 20,30,40,50,60,70, 80]

angleSeq = [10,20,40, 80]#2 of each done on the 7th one of these was suspect

abStimSize = params['Env_SD']*15

##currently extremely unsubtle relative sizes

fI=1
sizeSeq1 = [1]

#sizeSeq2 = [1]


def cartprod(*arrays):
    N = len(arrays)
    return transpose(meshgrid(*arrays, indexing='ij'), 
                    roll(arange(N + 1), -1)).reshape(-1, N)

#bs = len(sizeSeq1)

#biggerStim = numpy.zeros(bs)

###cartprod gives the cart product i.e all permentations of all varations
sA1 = cartprod(repNo, mod, angleSeq, sizeSeq1, FrameStim, stimLength)

sALen = len(sA1)

trialList1 = arange(1, sALen+1, 1)
tL = trialList1.reshape(-1,1)
# sA = sA1
sA = random.permutation(sA1)
#print(cartprod)

stimArray = concatenate((tL, sA), axis=1)
#stimeArray2 =cartprod(stimArray)


#for l in sizeSeq1:

 #   if sizeSeq1 < sizeSeq2:
 #       biggerStim == 1
 #   else:
 #       biggerStim ==-1
    







#bob = array([1, 3, 4, 5])
# Initialise stimuli

 ### Gauss2 = visual.GratingStim(win, tex='sin',mask = 'gauss', units = 'pix', pos=(0,0), size=params['Env_SD']*6,sf=0)
 #Env_SD single value code I don't understand why initialised here though.

#Gauss2 = visual.GratingStim(win, tex='sin',mask = 'gauss', units = 'pix', pos=(0,0), size=abstimSize,sf=0)
Gauss1 = visual.GratingStim(win, tex='sin',mask = 'gauss', units = 'pix', pos=(1400,0), size=abStimSize,sf=0)

## below initialised once cursor in centre of screen


#trialActivationWindow = visual.ShapeStim(win, units='', lineWidth=1.5, lineColor='white', lineColorSpace='rgb', fillColor=None, fillColorSpace='rgb', vertices=((-300, 0), (0, 300), (300, 0), (0, -300)), 
#    windingRule=None, closeShape=True, pos=(0, 0), size=1, ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True, name=None, autoLog=None, autoDraw=True)


## code here



#Gauss3 = visual.GratingStim(win, tex='sin',mask = 'gauss', units = 'pix', pos=(-1400,-0), size=params['Env_SD']*6,sf=0)



# Fixation cross

fixation1 = visual.GratingStim(win,rgb=1,sf=0, pos=(0,-500), size=(2,250))
fixation2 = visual.GratingStim(win,rgb=1,sf=0,pos=(0,500),size=(2,250))


#fixation1 = visual.Line(win, start=(xFov/2,0), end=(xFov/2, 300))


# Mean luminance frame

blank = visual.GratingStim(win,rgb=0,sf=0)






myHeaders = ['trialID', 'repNo', 'mod', 'angleSeq', 'sizeSeq1', 'FrameStim', 'stimLength']




        





haveYourDumbDataFrameThen = pd.DataFrame(stimArray, columns=myHeaders)

haveYourDumbDataFrameThen.to_csv(path_or_buf='Users.csv', index=False)




#xT2.append({'trialNumber':trialNumber,'repNo':repNo, 'mod':mod, 'mouseSeq1':mouseSeq1, 'mouseSeq2':mouseSeq2, 'angleSeq':angleSeq, 'sizeSeq':sizeSeq, 'sizeSeq2':sizeSeq2, 'sizeSeq3':sizeSeq3, 'sizeSeq4':sizeSeq4})




trials = data.TrialHandler(data.importConditions('Users.csv', returnFieldNames=False), 1, dataTypes=['acc'], method='sequential', extraInfo=params)

#cheatT = data.TrialHandler(data.importConditions('Users.csv', returnFieldNames=False), 1, dataTypes=['acc'], method='sequential', extraInfo=params)

##Trial.handler is good for how I've done it. i.e the "repititions" are actually just duplicates that are randomised into the main set if they want true reps need to use experiment handler


def checkCorrect(keys):

    for key in keys:		

        if key=='escape':

            win.close()
            #sys.exit()
            core.quit()

        elif key in ['1','num_1','3','num_3']:

            if (key in ['3','num_3']):

                return 1

            else: 

                return -1

        else: 

            return None





win.recordFrameIntervals = True

win.refreshThreshold = 1/60 + 0.95

win.nDroppedFrames =-1

#sd.s


loadingTrial =1
redo = 1
fdI = 0
for thisTrial in trials:
    
    redo = 1
    
    while redo == 1:
    
        redo=0
        angle = thisTrial['angleSeq']
        g1Size = thisTrial['sizeSeq1']
     
        absMod = thisTrial['mod']
        
        fstFrame = thisTrial['FrameStim']
        stimLength = thisTrial['stimLength']
        repNo= thisTrial['repNo']
        trialID = thisTrial['trialID']
       
        
         ## Note code treats equals to as being wrong at the moment. Loathe to zero it but might later.
        if fstFrame  <  60:
            soundTLoc = -1
                          
        else:
            soundTLoc =1
        
        
        
    
        # Set position of central element using constant stimuli
        #trialActivationWindow
       
        #this doesn't work after first trial and I don't understand why not considering the guass1 works fine however after consideration this might be a good thing as removes another frame of reference
        
    
        Gauss1.setPos([round(oneDegree*angle*absMod),0])  
        Gauss1.setSize([g1Size*abStimSize, g1Size*abStimSize])
     
        #sound.backend_sounddevice.SoundDeviceSound.setSound(value=10000, secs=0.5, octave=4, hamming=None, log=True)
        #sound.backend_sounddevice.SoundDeviceSound(value=10000, secs=0.5, hamming=None)  
    
         # Clear events and Resp variable   
    
    
        Resp=None
    
        event.clearEvents()
        # Draw stimuli
        
        for nFrames in range(1):
            
            ###splash screen
            fixation1.draw()
            fixation2.draw()
            win.flip()
            sleepTime = 0.5+(1/(repNo*3))
            time.sleep(sleepTime)
            
            
        for nFrames in range(1):
            
            fixation1.draw()
            fixation2.draw()
            #pysine(10000)
            ##playsound.playsound('out.mp3')
           # sd.OutputStream(device=args.device, channels=1, callback=callback, samplerate=samplerate)
            #sound.backend_sounddevice.SoundDeviceSound.play(simpleK,loops=None, when=None)
           # sd.play(simpleK, samplerate=audSamp)
            win.callOnFlip(sd.play, simpleK, audSamp)
            win.recordFrameIntervals = True
            win.refreshThreshold = 6/60
            win.nDroppedFrames =0
            win.flip()
       
        for nFrames in range(fstFrame):
            #sd.stop()
            
            fixation1.draw()
    
            fixation2.draw()
        
            #blank.draw()
           
    
           # Gauss3.draw()
    
            win.flip()
            
        for nFrames in range(stimLength):
             fixation1.draw()
    
             fixation2.draw()
             Gauss1.draw()
             win.flip()
             
        for nFrames in range(122-fstFrame-stimLength):
            fixation1.draw()
    
            fixation2.draw()
          
    
            win.flip()
        
        for nFrames in range(1):
            fixation1.draw()
    
            fixation2.draw()
            #sd.play(simpleK, samplerate=audSamp)
            
            win.callOnFlip(sd.play, simpleK, audSamp)
            
            win.flip() 
        
        win.recordFrameIntervals = False
        Resp=None
        event.clearEvents(eventType='keys')
        for nFrames in range(1):
            #sd.stop()
            #blank.draw()
            visual.TextStim(win, 'Select closest sound').draw()
            
            win.flip()
        
      
        
        
        if win.nDroppedFrames > 1:
           
            trials.data.add('trialDropID', win.nDroppedFrames) ##get rid of nDrop
            win.nDroppedFrames = 0
            frameTimesAll = frameTimesAll.append({'abort': win.frameIntervals}, trialID)
            redo=1
            for nFrames in range(50):
                visual.TextStim(win, 'Select closest sound.').draw()
                win.flip()
                
                
                
                
                
        else:
            frameTimesAll = frameTimesAll.append({'successful': win.frameIntervals}, trialID)
            redo =0
            win.nDroppedFrames = 0
       
        
        # if fI ==1:
        #     #cheatT = pd.DataFrame({'frameInters': win.frameIntervals}, index = [0])
        #     fI =2
        
        # else:
        #     #cheatT = cheatT.append({'frameInters': win.frameIntervals}, ignore_index=True)  
        #     fI ==1
    
        timeBefore = sum(win.frameIntervals[1:fstFrame])
        
        end = len(win.frameIntervals)-1
        timeAfter = sum(win.frameIntervals[fstFrame+1+stimLength:end-1])
        totalGapTime = timeBefore+timeAfter
        win.frameIntervals = []
        
        if timeBefore < timeAfter:
            soundALoc = -1
        else:
            soundALoc = 1
            
        #Get response from keyboard
       
        keys=event.getKeys()
    
        if len(keys)>0: 
    
            Resp = checkCorrect(keys)
    
    
    
        #if no response wait for one
    
        while Resp is None:
    
            Resp = checkCorrect(event.waitKeys())
            
            
        
    
        #record response
        
        expCorrectAnswer = soundTLoc*Resp
        actCorrectAnswer = soundALoc*Resp
        
        trials.data.add('Resp',Resp)
        trials.data.add('timebefore', timeBefore)
        trials.data.add('timeafter', timeAfter)
        trials.data.add('totalGapTime', totalGapTime)
        trials.data.add('ExpectedcorrectAnswer', expCorrectAnswer)
        trials.data.add('soundTLoc', soundTLoc)
        trials.data.add('FrameStim', fstFrame)
        trials.data.add('actualcorrectAnswer', actCorrectAnswer)
        
        
        trials.data.add('angleS', angle)
        trials.data.add('sizeSeq`', g1Size)
        trials.data.add('absMod', absMod)
        trials.data.add('stimLength', stimLength)
        
        trials.data.add('repNo', repNo)
        trials.data.add('trialID', trialID)
        
       
      
    
    #trialActivationWindow.opacity=1.0

   #record response

    #trials.data.add('acc',Resp)
    #trialActivationWindow.opacity=1.0


    
    
#trials finished 

p1 = params['Observer']
    #p2 = datetime.now()
    # baseNameT = p1 + '_temp' #+ p2.strftime()
baseName = p1
    #trials.saveAsText(fileName=baseName,stimOut =['separations'],dataOut =['acc_mean'],matrixOnly=True)


    #trials.saveAsPickle(fileName=baseNameT)
    #trials.saveAsPickle(fileName=baseName)

    # cheatName = p1 + 'cheat.csv'


#trials finished 

trials.frameTimes = frameTimesAll
trials.saveAsPickle(fileName=baseName,  fileCollisionMethod='rename')




visual.TextStim(win, 'Experiment Finished').draw()
win.flip()
event.waitKeys(keyList=['return'], maxWait=5)
win.close()




trials.saveAsExcel(fileName=baseName,  fileCollisionMethod='rename')
# cheatT.to_csv(cheatName)

b = baseName + '.xlsx'
if DEBUG:
        #angleSeq = [60,70,80]
        angleSeq = [30,40,50,60,70,80]
        sizeSeq1 = [0.55, 0.70, 0.85, 1, 1.15, 1.30, 1.35]
        baseName = 'test'
        b = 'pvmR1T.xlsx'

else:
    b = baseName + '.xlsx'
        
dataEx = pd.read_excel(b)

##dataframe.sum could have handled the heavy work but hey ho 

fI =1
for angleSeqN in angleSeq:
    justAng = dataEx.loc[dataEx['angleSeq'] == angleSeqN]
    
    
    for fstFrameN in FrameStim:
        sizeAng = justAng.loc[justAng['FrameStim'] == fstFrameN]
        
       
        totalC = sizeAng.loc[sizeAng['Resp_mean'] == 1]
        countCa = len(totalC)
        if countCa == 0:
            percentS = 0
        else:
            percentS = countCa/len(sizeAng)
        
        
        d = {'angleSeq': angleSeqN, 'fstFrameN': fstFrameN,'percentS': percentS, 'Observer': b}
        
        if fI ==1:
            results = pd.DataFrame(d, index = [0])
            fI =2
        
        else:
            results = results.append(d, ignore_index = True)
        
    
    
c = baseName + '_results.csv' 
results.to_csv(c)

for angleSeqN in angleSeq:
    
    sizePlot = results.loc[results['angleSeq'] == angleSeqN]
    plt.title(baseName)
    plt.ylim(0, 1)
    plt.plot(sizePlot.fstFrameN, sizePlot.percentS, label=angleSeqN)
    plt.ylabel('Stim Selected')
    plt.xlabel('Fram Loc')
    plt.legend()
    

    
plt.show()





########################################

##save data need to copy code from nites 2

########################################


###Need to work this one out

# baseName = 'data//%s_%s' %(params['Observer'],params['dateStr'])''

# trials.saveAsText(fileName=baseName,stimOut =['separations'],dataOut =['acc_mean'],matrixOnly=True)

# trials.saveAsPickle(fileName=baseName)
