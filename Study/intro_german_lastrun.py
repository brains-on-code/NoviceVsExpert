#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Mai 31, 2021, at 11:35
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'intro_german'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\Annabelle\\Documents\\GitHub\\NoviceVsExpert\\Study\\intro_german_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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

# Initialize components for Routine "Hello"
HelloClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Vielen Dank, dass Sie an dieser Studie teilnehmen.\n\nIn dieser Studie werden wir Ihnen kurze Java Programme zeigen\n(maximale Dauer je 3 Minuten).\nIhre Aufgabe ist es, die Programme zu verstehen. \nDanach werden wir Ihnen eine Frage zu der Funktionalität des Programms stellen.\n\nEs folgt ein Beispiel\n<Weiter mit Leertaste>',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "HelloWorld"
HelloWorldClock = core.Clock()
HelloWorldImage = visual.ImageStim(
    win=win,
    name='HelloWorldImage', 
    image='Resources\\\\Intro\\\\helloWorld.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.763, 0.279),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='<Weiter mit Leertaste>',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='Program Comprehension',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "input"
inputClock = core.Clock()
helloWorldInput = visual.ImageStim(
    win=win,
    name='helloWorldInput', 
    image='Resources\\\\Intro\\\\helloWorldInput.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.834, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Hier wird die Methode von eben aufgerufen.\nWie lautet die Ausgabe?\n',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='Antwortmöglichkeiten folgen:\n<Weiter mit Leertaste>',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "output"
outputClock = core.Clock()
key_resp_3 = keyboard.Keyboard()
helloWorld_1 = visual.ImageStim(
    win=win,
    name='helloWorld_1', 
    image='Resources\\\\Intro\\\\wrong1.PNG', mask=None,
    ori=0.0, pos=(-0.6, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
helloWorld_2 = visual.ImageStim(
    win=win,
    name='helloWorld_2', 
    image='Resources\\\\Intro\\\\wrong2.PNG', mask=None,
    ori=0.0, pos=(-0.3, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
helloWorld_3 = visual.ImageStim(
    win=win,
    name='helloWorld_3', 
    image='Resources\\\\Intro\\\\correct.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
helloWorld_4 = visual.ImageStim(
    win=win,
    name='helloWorld_4', 
    image='Resources\\\\Intro\\\\wrong3.PNG', mask=None,
    ori=0.0, pos=(0.3, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Fragezeichen = visual.ImageStim(
    win=win,
    name='Fragezeichen', 
    image='Resources\\\\Intro\\\\fragezeichen.PNG', mask=None,
    ori=0.0, pos=(0.6, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='Wählen Sie mit den Pfeiltasten die passende Ausgabe.\n\nWenn keine der Antwortmöglichkeiten passt, wählen Sie bitte "?".\n',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='Resources\\\\Intro\\\\pfeil.png', mask=None,
    ori=0.0, pos=(0, -0.25), size=(0.1, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Der Code ist immer syntaktisch korrekt,\nalso ausführbar.\n\nFunktionsnamen, Codestruktur, Variablen etc. können ungewöhnlich sein. Lassen Sie sich davon nicht irritieren und lösen Sie die Aufgabe so gut wie möglich.\n\nDie zur Verfügung stehende Zeit ist sehr knapp! Das Experiment ist bewusst anspruchsvoll ausgelegt, sodass nicht alle Aufgaben gelöst werden können. \n\nFür "Weiter" und "einloggen" immer die Leertaste drücken. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Bitte Antworten Sie nur, wenn Sie das Ergebnis auch kennen. \n\nGenau wie in diesem Beispiel wird Ihnen immer ein Funktionsaufruf präsentiert werden, und Sie sollen die korrekte Ausgabe auswählen. \n\nBitte raten Sie nicht, sondern wählen Sie "?". "?" ist besser, als eine Antwort zu raten. Am Wichtigsten ist jedoch, dass Sie sich nicht frustrieren lassen. \n\nHaben Sie noch Fragen?\nNun folgt ein Trainingsbeispiel:',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "TrainingSnippet"
TrainingSnippetClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='Program Comprehension',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Resources\\\\Intro\\\\helloWorld.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "TrainingInput"
TrainingInputClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='Resources\\\\Intro\\\\helloWorldInput.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "TrainingOutput_2"
TrainingOutput_2Clock = core.Clock()
key_resp_14 = keyboard.Keyboard()
helloWorld = visual.ImageStim(
    win=win,
    name='helloWorld', 
    image='Resources\\\\Intro\\\\wrong1.PNG', mask=None,
    ori=0.0, pos=(-0.6, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
helloWorld_5 = visual.ImageStim(
    win=win,
    name='helloWorld_5', 
    image='Resources\\\\Intro\\\\wrong2.PNG', mask=None,
    ori=0.0, pos=(-0.3, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
helloWorld_6 = visual.ImageStim(
    win=win,
    name='helloWorld_6', 
    image='Resources\\\\Intro\\\\correct.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
helloWorld_7 = visual.ImageStim(
    win=win,
    name='helloWorld_7', 
    image='Resources\\\\Intro\\\\wrong3.PNG', mask=None,
    ori=0.0, pos=(0.3, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Fragezeichen_2 = visual.ImageStim(
    win=win,
    name='Fragezeichen_2', 
    image='Resources\\\\Intro\\\\fragezeichen.PNG', mask=None,
    ori=0.0, pos=(0.6, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='Resources\\\\Intro\\\\pfeil.png', mask=None,
    ori=0.0, pos=(0, -0.25), size=(0.1, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# Initialize components for Routine "Rest"
RestClock = core.Clock()
key_resp_7 = keyboard.Keyboard()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Sehr gut!\n\nNach jeder Aufgabe erscheint für 30 Sekunden ein kleines Kreuz auf dem Bildschirm. Nutzen Sie diese Zeit, um sich auszuruhen.\n\nUm früher fortzufahren: <Leertaste>',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Rest_crossfixation"
Rest_crossfixationClock = core.Clock()
restImage_2 = visual.ImageStim(
    win=win,
    name='restImage_2', 
    image='Resources\\\\Intro\\\\rest.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "Frage"
FrageClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='Haben Sie noch Fragen?\n\n<Weiter mit Leertaste>',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "SyntaxInstruction"
SyntaxInstructionClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Nun kennen Sie einen der beiden Aufgabentypen. Der andere Aufgabentyp heißt “search ”. Wir zeigen Ihnen ein Java Programm, dabei ist Ihre Aufgabe so schnell wie möglich für jede Klammer ( oder { einmal die Pfeiltaste nach unten zu drücken. Wenn Sie fertig sind, drücken Sie die Leertaste.\nAchtung! Wir suchen nur die offenen Klammern ( und {,\nandere Klammern, wie beispielsweise },), [, ] sollen ignoriert werden.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "SampleSyntax"
SampleSyntaxClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Klammer gefunden: <Pfeiltatste nach unten>\nz.B. 5 Klammern = 5 mal Pfeiltaste nach unten drücken\n\n<Weiter mit Leertaste>',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sampleSyntax = visual.ImageStim(
    win=win,
    name='sampleSyntax', 
    image='Resources\\\\Intro\\\\helloWorld.png', mask=None,
    ori=0.0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Pfeiltaste = keyboard.Keyboard()
weiter = keyboard.Keyboard()

# Initialize components for Routine "Rest_crossfixation"
Rest_crossfixationClock = core.Clock()
restImage_2 = visual.ImageStim(
    win=win,
    name='restImage_2', 
    image='Resources\\\\Intro\\\\rest.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "Overview"
OverviewClock = core.Clock()
overview = visual.TextStim(win=win, name='overview',
    text='Insgesamt machen wir 3 Durchläufe à 20 Minuten. \n\nZwischen den Durchläufen machen wir eine 5 Minuten Pause.\nDazu werden wir Ihnen während der 30s Pause Bescheid sagen.\nIn dieser Zeit können Sie sich strecken, wir lüften und kontrollieren den korrekten Sitz der EEG Kappe.\n\n<Weiter mit Leertaste>',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
overviewImage = visual.ImageStim(
    win=win,
    name='overviewImage', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "Warning_StartSession"
Warning_StartSessionClock = core.Clock()
key_resp_9 = keyboard.Keyboard()
text_9 = visual.TextStim(win=win, name='text_9',
    text='<Start der Studie mit "s">',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
warningStartStudy = visual.ImageStim(
    win=win,
    name='warningStartStudy', 
    image='Resources\\\\Intro\\\\stopp.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Hello"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
HelloComponents = [text, key_resp]
for thisComponent in HelloComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
HelloClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Hello"-------
while continueRoutine:
    # get current time
    t = HelloClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=HelloClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in HelloComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Hello"-------
for thisComponent in HelloComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Hello" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "HelloWorld"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
HelloWorldComponents = [HelloWorldImage, key_resp_2, text_2, text_12]
for thisComponent in HelloWorldComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
HelloWorldClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "HelloWorld"-------
while continueRoutine:
    # get current time
    t = HelloWorldClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=HelloWorldClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *HelloWorldImage* updates
    if HelloWorldImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HelloWorldImage.frameNStart = frameN  # exact frame index
        HelloWorldImage.tStart = t  # local t and not account for scr refresh
        HelloWorldImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HelloWorldImage, 'tStartRefresh')  # time at next scr refresh
        HelloWorldImage.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in HelloWorldComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "HelloWorld"-------
for thisComponent in HelloWorldComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('HelloWorldImage.started', HelloWorldImage.tStartRefresh)
thisExp.addData('HelloWorldImage.stopped', HelloWorldImage.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# the Routine "HelloWorld" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "input"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
inputComponents = [helloWorldInput, key_resp_4, text_3, text_11]
for thisComponent in inputComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inputClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "input"-------
while continueRoutine:
    # get current time
    t = inputClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inputClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *helloWorldInput* updates
    if helloWorldInput.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloWorldInput.frameNStart = frameN  # exact frame index
        helloWorldInput.tStart = t  # local t and not account for scr refresh
        helloWorldInput.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloWorldInput, 'tStartRefresh')  # time at next scr refresh
        helloWorldInput.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inputComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "input"-------
for thisComponent in inputComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('helloWorldInput.started', helloWorldInput.tStartRefresh)
thisExp.addData('helloWorldInput.stopped', helloWorldInput.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# the Routine "input" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "output"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
outputComponents = [key_resp_3, helloWorld_1, helloWorld_2, helloWorld_3, helloWorld_4, Fragezeichen, text_4, image_3]
for thisComponent in outputComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
outputClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "output"-------
while continueRoutine:
    # get current time
    t = outputClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=outputClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
            key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # *helloWorld_1* updates
    if helloWorld_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloWorld_1.frameNStart = frameN  # exact frame index
        helloWorld_1.tStart = t  # local t and not account for scr refresh
        helloWorld_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloWorld_1, 'tStartRefresh')  # time at next scr refresh
        helloWorld_1.setAutoDraw(True)
    
    # *helloWorld_2* updates
    if helloWorld_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloWorld_2.frameNStart = frameN  # exact frame index
        helloWorld_2.tStart = t  # local t and not account for scr refresh
        helloWorld_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloWorld_2, 'tStartRefresh')  # time at next scr refresh
        helloWorld_2.setAutoDraw(True)
    
    # *helloWorld_3* updates
    if helloWorld_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloWorld_3.frameNStart = frameN  # exact frame index
        helloWorld_3.tStart = t  # local t and not account for scr refresh
        helloWorld_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloWorld_3, 'tStartRefresh')  # time at next scr refresh
        helloWorld_3.setAutoDraw(True)
    
    # *helloWorld_4* updates
    if helloWorld_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloWorld_4.frameNStart = frameN  # exact frame index
        helloWorld_4.tStart = t  # local t and not account for scr refresh
        helloWorld_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloWorld_4, 'tStartRefresh')  # time at next scr refresh
        helloWorld_4.setAutoDraw(True)
    
    # *Fragezeichen* updates
    if Fragezeichen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fragezeichen.frameNStart = frameN  # exact frame index
        Fragezeichen.tStart = t  # local t and not account for scr refresh
        Fragezeichen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fragezeichen, 'tStartRefresh')  # time at next scr refresh
        Fragezeichen.setAutoDraw(True)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in outputComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "output"-------
for thisComponent in outputComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('helloWorld_1.started', helloWorld_1.tStartRefresh)
thisExp.addData('helloWorld_1.stopped', helloWorld_1.tStopRefresh)
thisExp.addData('helloWorld_2.started', helloWorld_2.tStartRefresh)
thisExp.addData('helloWorld_2.stopped', helloWorld_2.tStopRefresh)
thisExp.addData('helloWorld_3.started', helloWorld_3.tStartRefresh)
thisExp.addData('helloWorld_3.stopped', helloWorld_3.tStopRefresh)
thisExp.addData('helloWorld_4.started', helloWorld_4.tStartRefresh)
thisExp.addData('helloWorld_4.stopped', helloWorld_4.tStopRefresh)
thisExp.addData('Fragezeichen.started', Fragezeichen.tStartRefresh)
thisExp.addData('Fragezeichen.stopped', Fragezeichen.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)
# the Routine "output" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
InstructionsComponents = [text_5, key_resp_5]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
Instructions2Components = [text_10, key_resp_10]
for thisComponent in Instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions2"-------
while continueRoutine:
    # get current time
    t = Instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TrainingSnippet"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
TrainingSnippetComponents = [text_14, image, key_resp_12]
for thisComponent in TrainingSnippetComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TrainingSnippetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TrainingSnippet"-------
while continueRoutine:
    # get current time
    t = TrainingSnippetClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TrainingSnippetClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TrainingSnippetComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TrainingSnippet"-------
for thisComponent in TrainingSnippetComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
# the Routine "TrainingSnippet" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TrainingInput"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
TrainingInputComponents = [image_2, key_resp_13]
for thisComponent in TrainingInputComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TrainingInputClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TrainingInput"-------
while continueRoutine:
    # get current time
    t = TrainingInputClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TrainingInputClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TrainingInputComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TrainingInput"-------
for thisComponent in TrainingInputComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
# the Routine "TrainingInput" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TrainingOutput_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
TrainingOutput_2Components = [key_resp_14, helloWorld, helloWorld_5, helloWorld_6, helloWorld_7, Fragezeichen_2, image_4]
for thisComponent in TrainingOutput_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TrainingOutput_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TrainingOutput_2"-------
while continueRoutine:
    # get current time
    t = TrainingOutput_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TrainingOutput_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = [key.name for key in _key_resp_14_allKeys]  # storing all keys
            key_resp_14.rt = [key.rt for key in _key_resp_14_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # *helloWorld* updates
    if helloWorld.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloWorld.frameNStart = frameN  # exact frame index
        helloWorld.tStart = t  # local t and not account for scr refresh
        helloWorld.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloWorld, 'tStartRefresh')  # time at next scr refresh
        helloWorld.setAutoDraw(True)
    
    # *helloWorld_5* updates
    if helloWorld_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloWorld_5.frameNStart = frameN  # exact frame index
        helloWorld_5.tStart = t  # local t and not account for scr refresh
        helloWorld_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloWorld_5, 'tStartRefresh')  # time at next scr refresh
        helloWorld_5.setAutoDraw(True)
    
    # *helloWorld_6* updates
    if helloWorld_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloWorld_6.frameNStart = frameN  # exact frame index
        helloWorld_6.tStart = t  # local t and not account for scr refresh
        helloWorld_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloWorld_6, 'tStartRefresh')  # time at next scr refresh
        helloWorld_6.setAutoDraw(True)
    
    # *helloWorld_7* updates
    if helloWorld_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        helloWorld_7.frameNStart = frameN  # exact frame index
        helloWorld_7.tStart = t  # local t and not account for scr refresh
        helloWorld_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(helloWorld_7, 'tStartRefresh')  # time at next scr refresh
        helloWorld_7.setAutoDraw(True)
    
    # *Fragezeichen_2* updates
    if Fragezeichen_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fragezeichen_2.frameNStart = frameN  # exact frame index
        Fragezeichen_2.tStart = t  # local t and not account for scr refresh
        Fragezeichen_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fragezeichen_2, 'tStartRefresh')  # time at next scr refresh
        Fragezeichen_2.setAutoDraw(True)
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TrainingOutput_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TrainingOutput_2"-------
for thisComponent in TrainingOutput_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.addData('key_resp_14.started', key_resp_14.tStartRefresh)
thisExp.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('helloWorld.started', helloWorld.tStartRefresh)
thisExp.addData('helloWorld.stopped', helloWorld.tStopRefresh)
thisExp.addData('helloWorld_5.started', helloWorld_5.tStartRefresh)
thisExp.addData('helloWorld_5.stopped', helloWorld_5.tStopRefresh)
thisExp.addData('helloWorld_6.started', helloWorld_6.tStartRefresh)
thisExp.addData('helloWorld_6.stopped', helloWorld_6.tStopRefresh)
thisExp.addData('helloWorld_7.started', helloWorld_7.tStartRefresh)
thisExp.addData('helloWorld_7.stopped', helloWorld_7.tStopRefresh)
thisExp.addData('Fragezeichen_2.started', Fragezeichen_2.tStartRefresh)
thisExp.addData('Fragezeichen_2.stopped', Fragezeichen_2.tStopRefresh)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)
# the Routine "TrainingOutput_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Rest"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
RestComponents = [key_resp_7, text_8]
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
while continueRoutine:
    # get current time
    t = RestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
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
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# the Routine "Rest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Rest_crossfixation"-------
continueRoutine = True
routineTimer.add(30.000000)
# update component parameters for each repeat
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
# keep track of which components have finished
Rest_crossfixationComponents = [restImage_2, key_resp_15]
for thisComponent in Rest_crossfixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Rest_crossfixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Rest_crossfixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Rest_crossfixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Rest_crossfixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *restImage_2* updates
    if restImage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        restImage_2.frameNStart = frameN  # exact frame index
        restImage_2.tStart = t  # local t and not account for scr refresh
        restImage_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(restImage_2, 'tStartRefresh')  # time at next scr refresh
        restImage_2.setAutoDraw(True)
    if restImage_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > restImage_2.tStartRefresh + 30.0-frameTolerance:
            # keep track of stop time/frame for later
            restImage_2.tStop = t  # not accounting for scr refresh
            restImage_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(restImage_2, 'tStopRefresh')  # time at next scr refresh
            restImage_2.setAutoDraw(False)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_15.tStartRefresh + 30.0-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_15.tStop = t  # not accounting for scr refresh
            key_resp_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_15, 'tStopRefresh')  # time at next scr refresh
            key_resp_15.status = FINISHED
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
            key_resp_15.rt = _key_resp_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Rest_crossfixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Rest_crossfixation"-------
for thisComponent in Rest_crossfixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('restImage_2.started', restImage_2.tStartRefresh)
thisExp.addData('restImage_2.stopped', restImage_2.tStopRefresh)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys = None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.addData('key_resp_15.started', key_resp_15.tStartRefresh)
thisExp.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "Frage"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
FrageComponents = [text_13, key_resp_11]
for thisComponent in FrageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FrageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Frage"-------
while continueRoutine:
    # get current time
    t = FrageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FrageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FrageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Frage"-------
for thisComponent in FrageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
# the Routine "Frage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SyntaxInstruction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
SyntaxInstructionComponents = [text_6, key_resp_6]
for thisComponent in SyntaxInstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SyntaxInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SyntaxInstruction"-------
while continueRoutine:
    # get current time
    t = SyntaxInstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SyntaxInstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SyntaxInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SyntaxInstruction"-------
for thisComponent in SyntaxInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "SyntaxInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SampleSyntax"-------
continueRoutine = True
# update component parameters for each repeat
Pfeiltaste.keys = []
Pfeiltaste.rt = []
_Pfeiltaste_allKeys = []
weiter.keys = []
weiter.rt = []
_weiter_allKeys = []
# keep track of which components have finished
SampleSyntaxComponents = [text_7, sampleSyntax, Pfeiltaste, weiter]
for thisComponent in SampleSyntaxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SampleSyntaxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SampleSyntax"-------
while continueRoutine:
    # get current time
    t = SampleSyntaxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SampleSyntaxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *sampleSyntax* updates
    if sampleSyntax.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sampleSyntax.frameNStart = frameN  # exact frame index
        sampleSyntax.tStart = t  # local t and not account for scr refresh
        sampleSyntax.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sampleSyntax, 'tStartRefresh')  # time at next scr refresh
        sampleSyntax.setAutoDraw(True)
    
    # *Pfeiltaste* updates
    waitOnFlip = False
    if Pfeiltaste.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pfeiltaste.frameNStart = frameN  # exact frame index
        Pfeiltaste.tStart = t  # local t and not account for scr refresh
        Pfeiltaste.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pfeiltaste, 'tStartRefresh')  # time at next scr refresh
        Pfeiltaste.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Pfeiltaste.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Pfeiltaste.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Pfeiltaste.status == STARTED and not waitOnFlip:
        theseKeys = Pfeiltaste.getKeys(keyList=['down'], waitRelease=False)
        _Pfeiltaste_allKeys.extend(theseKeys)
        if len(_Pfeiltaste_allKeys):
            Pfeiltaste.keys = [key.name for key in _Pfeiltaste_allKeys]  # storing all keys
            Pfeiltaste.rt = [key.rt for key in _Pfeiltaste_allKeys]
    
    # *weiter* updates
    waitOnFlip = False
    if weiter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        weiter.frameNStart = frameN  # exact frame index
        weiter.tStart = t  # local t and not account for scr refresh
        weiter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(weiter, 'tStartRefresh')  # time at next scr refresh
        weiter.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(weiter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(weiter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if weiter.status == STARTED and not waitOnFlip:
        theseKeys = weiter.getKeys(keyList=['space'], waitRelease=False)
        _weiter_allKeys.extend(theseKeys)
        if len(_weiter_allKeys):
            weiter.keys = _weiter_allKeys[-1].name  # just the last key pressed
            weiter.rt = _weiter_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SampleSyntaxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SampleSyntax"-------
for thisComponent in SampleSyntaxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
thisExp.addData('sampleSyntax.started', sampleSyntax.tStartRefresh)
thisExp.addData('sampleSyntax.stopped', sampleSyntax.tStopRefresh)
# check responses
if Pfeiltaste.keys in ['', [], None]:  # No response was made
    Pfeiltaste.keys = None
thisExp.addData('Pfeiltaste.keys',Pfeiltaste.keys)
if Pfeiltaste.keys != None:  # we had a response
    thisExp.addData('Pfeiltaste.rt', Pfeiltaste.rt)
thisExp.addData('Pfeiltaste.started', Pfeiltaste.tStartRefresh)
thisExp.addData('Pfeiltaste.stopped', Pfeiltaste.tStopRefresh)
thisExp.nextEntry()
# check responses
if weiter.keys in ['', [], None]:  # No response was made
    weiter.keys = None
thisExp.addData('weiter.keys',weiter.keys)
if weiter.keys != None:  # we had a response
    thisExp.addData('weiter.rt', weiter.rt)
thisExp.addData('weiter.started', weiter.tStartRefresh)
thisExp.addData('weiter.stopped', weiter.tStopRefresh)
thisExp.nextEntry()
# the Routine "SampleSyntax" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Rest_crossfixation"-------
continueRoutine = True
routineTimer.add(30.000000)
# update component parameters for each repeat
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
# keep track of which components have finished
Rest_crossfixationComponents = [restImage_2, key_resp_15]
for thisComponent in Rest_crossfixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Rest_crossfixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Rest_crossfixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Rest_crossfixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Rest_crossfixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *restImage_2* updates
    if restImage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        restImage_2.frameNStart = frameN  # exact frame index
        restImage_2.tStart = t  # local t and not account for scr refresh
        restImage_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(restImage_2, 'tStartRefresh')  # time at next scr refresh
        restImage_2.setAutoDraw(True)
    if restImage_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > restImage_2.tStartRefresh + 30.0-frameTolerance:
            # keep track of stop time/frame for later
            restImage_2.tStop = t  # not accounting for scr refresh
            restImage_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(restImage_2, 'tStopRefresh')  # time at next scr refresh
            restImage_2.setAutoDraw(False)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_15.tStartRefresh + 30.0-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_15.tStop = t  # not accounting for scr refresh
            key_resp_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_15, 'tStopRefresh')  # time at next scr refresh
            key_resp_15.status = FINISHED
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
            key_resp_15.rt = _key_resp_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Rest_crossfixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Rest_crossfixation"-------
for thisComponent in Rest_crossfixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('restImage_2.started', restImage_2.tStartRefresh)
thisExp.addData('restImage_2.stopped', restImage_2.tStopRefresh)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys = None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.addData('key_resp_15.started', key_resp_15.tStartRefresh)
thisExp.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "Overview"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
OverviewComponents = [overview, overviewImage, key_resp_8]
for thisComponent in OverviewComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
OverviewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Overview"-------
while continueRoutine:
    # get current time
    t = OverviewClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=OverviewClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *overview* updates
    if overview.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        overview.frameNStart = frameN  # exact frame index
        overview.tStart = t  # local t and not account for scr refresh
        overview.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(overview, 'tStartRefresh')  # time at next scr refresh
        overview.setAutoDraw(True)
    
    # *overviewImage* updates
    if overviewImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        overviewImage.frameNStart = frameN  # exact frame index
        overviewImage.tStart = t  # local t and not account for scr refresh
        overviewImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(overviewImage, 'tStartRefresh')  # time at next scr refresh
        overviewImage.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in OverviewComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Overview"-------
for thisComponent in OverviewComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('overview.started', overview.tStartRefresh)
thisExp.addData('overview.stopped', overview.tStopRefresh)
thisExp.addData('overviewImage.started', overviewImage.tStartRefresh)
thisExp.addData('overviewImage.stopped', overviewImage.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "Overview" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Warning_StartSession"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
Warning_StartSessionComponents = [key_resp_9, text_9, warningStartStudy]
for thisComponent in Warning_StartSessionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Warning_StartSessionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Warning_StartSession"-------
while continueRoutine:
    # get current time
    t = Warning_StartSessionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Warning_StartSessionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *warningStartStudy* updates
    if warningStartStudy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        warningStartStudy.frameNStart = frameN  # exact frame index
        warningStartStudy.tStart = t  # local t and not account for scr refresh
        warningStartStudy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(warningStartStudy, 'tStartRefresh')  # time at next scr refresh
        warningStartStudy.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Warning_StartSessionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Warning_StartSession"-------
for thisComponent in Warning_StartSessionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
thisExp.addData('warningStartStudy.started', warningStartStudy.tStartRefresh)
thisExp.addData('warningStartStudy.stopped', warningStartStudy.tStopRefresh)
# the Routine "Warning_StartSession" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
