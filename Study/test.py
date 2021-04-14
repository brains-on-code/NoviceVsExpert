#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Februar 10, 2021, at 16:23
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import random, xlrd

random.seed()

in_file = "conditions.xlsx"

num_items = 14
num_iter = 5

path_stim = []
current_idx = 0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '001', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jonas\\OneDrive\\Desktop\\eeg-Study\\experiments\\test\\test.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=-1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "codeStartup"
codeStartupClock = core.Clock()
#open execl
inbook = xlrd.open_workbook(in_file)
insheet = inbook.sheet_by_index(0)

#loop through rows
for rowx in range(1, num_items+1):
    
    row = insheet.row_values(rowx)
    
    path_stim.append(row[0])
    
random.shuffle(path_stim)

    
    

# Initialize components for Routine "ShowImage"
ShowImageClock = core.Clock()
Image = visual.ImageStim(
    win=win,
    name='Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
response = keyboard.Keyboard()

# Initialize components for Routine "Rest"
RestClock = core.Clock()
rest = visual.TextStim(win=win, name='rest',
    text='Rest',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AskToContinue"
AskToContinueClock = core.Clock()
continuQuestion = visual.TextStim(win=win, name='continuQuestion',
    text='Möchtest du weitermachen?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
stop = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "codeStartup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
codeStartupComponents = []
for thisComponent in codeStartupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
codeStartupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "codeStartup"-------
while continueRoutine:
    # get current time
    t = codeStartupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=codeStartupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in codeStartupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "codeStartup"-------
for thisComponent in codeStartupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "codeStartup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Loop = data.TrialHandler(nReps=3, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Loop')
    thisExp.addLoop(Loop)  # add the loop to the experiment
    thisLoop = Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
    if thisLoop != None:
        for paramName in thisLoop:
            exec('{} = thisLoop[paramName]'.format(paramName))
    
    for thisLoop in Loop:
        currentLoop = Loop
        # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
        if thisLoop != None:
            for paramName in thisLoop:
                exec('{} = thisLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ShowImage"-------
        continueRoutine = True
        # update component parameters for each repeat
        Image.setImage(path_stim[current_idx])
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        ShowImageComponents = [Image, response]
        for thisComponent in ShowImageComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ShowImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ShowImage"-------
        while continueRoutine:
            # get current time
            t = ShowImageClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ShowImageClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Image* updates
            if Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Image.frameNStart = frameN  # exact frame index
                Image.tStart = t  # local t and not account for scr refresh
                Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Image, 'tStartRefresh')  # time at next scr refresh
                Image.setAutoDraw(True)
            
            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['space'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ShowImageComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ShowImage"-------
        for thisComponent in ShowImageComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Loop.addData('Image.started', Image.tStartRefresh)
        Loop.addData('Image.stopped', Image.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
        Loop.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            Loop.addData('response.rt', response.rt)
        Loop.addData('response.started', response.tStartRefresh)
        Loop.addData('response.stopped', response.tStopRefresh)
        thisExp.addData("path", path_stim[current_idx])
        
        current_idx = current_idx + 1
        
        if current_idx >= 14:
            exit(0)
        # the Routine "ShowImage" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Rest"-------
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        # keep track of which components have finished
        RestComponents = [rest]
        for thisComponent in RestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        RestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Rest"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RestClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=RestClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rest* updates
            if rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rest.frameNStart = frameN  # exact frame index
                rest.tStart = t  # local t and not account for scr refresh
                rest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
                rest.setAutoDraw(True)
            if rest.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rest.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    rest.tStop = t  # not accounting for scr refresh
                    rest.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rest, 'tStopRefresh')  # time at next scr refresh
                    rest.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Rest"-------
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Loop.addData('rest.started', rest.tStartRefresh)
        Loop.addData('rest.stopped', rest.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 3 repeats of 'Loop'
    
    
    # ------Prepare to start Routine "AskToContinue"-------
    continueRoutine = True
    # update component parameters for each repeat
    stop.keys = []
    stop.rt = []
    _stop_allKeys = []
    # keep track of which components have finished
    AskToContinueComponents = [continuQuestion, stop]
    for thisComponent in AskToContinueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AskToContinueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AskToContinue"-------
    while continueRoutine:
        # get current time
        t = AskToContinueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AskToContinueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *continuQuestion* updates
        if continuQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            continuQuestion.frameNStart = frameN  # exact frame index
            continuQuestion.tStart = t  # local t and not account for scr refresh
            continuQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continuQuestion, 'tStartRefresh')  # time at next scr refresh
            continuQuestion.setAutoDraw(True)
        
        # *stop* updates
        waitOnFlip = False
        if stop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stop.frameNStart = frameN  # exact frame index
            stop.tStart = t  # local t and not account for scr refresh
            stop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop, 'tStartRefresh')  # time at next scr refresh
            stop.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stop.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stop.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stop.status == STARTED and not waitOnFlip:
            theseKeys = stop.getKeys(keyList=['space'], waitRelease=False)
            _stop_allKeys.extend(theseKeys)
            if len(_stop_allKeys):
                stop.keys = _stop_allKeys[-1].name  # just the last key pressed
                stop.rt = _stop_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AskToContinueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AskToContinue"-------
    for thisComponent in AskToContinueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('continuQuestion.started', continuQuestion.tStartRefresh)
    trials.addData('continuQuestion.stopped', continuQuestion.tStopRefresh)
    # check responses
    if stop.keys in ['', [], None]:  # No response was made
        stop.keys = None
    trials.addData('stop.keys',stop.keys)
    if stop.keys != None:  # we had a response
        trials.addData('stop.rt', stop.rt)
    trials.addData('stop.started', stop.tStartRefresh)
    trials.addData('stop.stopped', stop.tStopRefresh)
    # the Routine "AskToContinue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
