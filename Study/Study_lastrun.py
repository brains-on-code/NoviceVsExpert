#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Juni 15, 2021, at 10:52
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

import random, xlrd
import socket
import pandas as pd
import json

global current_image_path

use_eyetracker = False
use_eeg = False

random.seed()

in_file = "conditions.xlsx"
example_file = "example_conditions.xlsx"
syntax_file = "syntax_conditions.xlsx"

syntax_idx = 0
num_items = 32
num_iter = 5
idx_values = [x for x in range(num_items)]

TCP_IP = 'localhost'
TCP_PORT = 50000
Message = 1

from psychopy import monitors

mon = None
for tmp_mon in monitors.getAllMonitors():
    mon = tmp_mon
    
width = monitors.Monitor(mon).getSizePix()[0]
height = monitors.Monitor(mon).getSizePix()[1]
ll = -0.8 * width
lm = -0.4 * width
mm = 0.0 * width
rm = 0.4 * width
rr = 0.8 * width
md = -0.1 * height
mu = 0.2 * height
#from EEGTools.Recorders.LiveAmpRecorder.liveamp_recorder import LiveAmpRecorder as Recorder
#from base_functionalities.logger import Logger


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
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
    originPath='C:\\Users\\jonas\\OneDrive\\Dokumente\\GitHub\\NoviceVsExpert\\Study\\Study_lastrun.py',
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
    monitor='testMonitor', color=[0.5,0.5,0.5], colorSpace='rgb',
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
inbook = pd.read_excel(in_file)
example_df = pd.read_excel(example_file)
syntax_df = pd.read_excel(syntax_file)
    
random.shuffle(idx_values)
current_idx = idx_values.pop(0)

language = "English"
textbase = json.load(open('./Resources/textbase.json', 'rb'))

# Initialize components for Routine "Hello"
HelloClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text=textbase["Instructions"][language],
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text=textbase["Instructions2"][language],
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "Hello_World"
Hello_WorldClock = core.Clock()
HelloWorldImage = visual.ImageStim(
    win=win,
    name='HelloWorldImage', units='pix', 
    image=example_df.iloc[0]["ImagePath"], mask=None,
    ori=0.0, pos=(0, 0), size=(example_df.iloc[0]["ImagePathWidth"], example_df.iloc[0]["ImagePathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text=textbase["Hello_World"][language],
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "input"
inputClock = core.Clock()
helloWorldInput = visual.ImageStim(
    win=win,
    name='helloWorldInput', units='pix', 
    image=example_df.iloc[0]["InputPath"], mask=None,
    ori=0.0, pos=(0, 0), size=(example_df.iloc[0]["InputPathWidth"], example_df.iloc[0]["ImagePathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()
text_11 = visual.TextStim(win=win, name='text_11',
    text=textbase["Input"][language],
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "output"
outputClock = core.Clock()
key_resp_5 = keyboard.Keyboard()
helloWorld_1 = visual.ImageStim(
    win=win,
    name='helloWorld_1', units='pix', 
    image=example_df.iloc[0]["RightPath"], mask=None,
    ori=0.0, pos=(ll, 0), size=(example_df.iloc[0]["RightPathWidth"], example_df.iloc[0]["RightPathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
helloWorld_2 = visual.ImageStim(
    win=win,
    name='helloWorld_2', units='pix', 
    image=example_df.iloc[0]["Wrong1Path"], mask=None,
    ori=0.0, pos=(lm, 0), size=(example_df.iloc[0]["Wrong1PathWidth"], example_df.iloc[0]["Wrong1PathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
helloWorld_3 = visual.ImageStim(
    win=win,
    name='helloWorld_3', units='pix', 
    image=example_df.iloc[0]["Wrong2Path"], mask=None,
    ori=0.0, pos=(mm, 0), size=(example_df.iloc[0]["Wrong2PathWidth"], example_df.iloc[0]["Wrong2PathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
helloWorld_4 = visual.ImageStim(
    win=win,
    name='helloWorld_4', units='pix', 
    image=example_df.iloc[0]["DontKnowPath"], mask=None,
    ori=0.0, pos=(rm, 0), size=(example_df.iloc[0]["DontKnowPathWidth"], example_df.iloc[0]["DontKnowPathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Fragezeichen = visual.ImageStim(
    win=win,
    name='Fragezeichen', units='pix', 
    image=example_df.iloc[0]["NextPath"], mask=None,
    ori=0.0, pos=(rr, 0), size=(example_df.iloc[0]["NextPathWidth"], example_df.iloc[0]["NextPathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text=textbase["Output"][language],
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
image_6 = visual.ImageStim(
    win=win,
    name='image_6', units='pix', 
    image='Resources/arrow.png', mask=None,
    ori=0.0, pos=[0,0], size=(86, 54),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# Initialize components for Routine "TrainingSnippet"
TrainingSnippetClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text=textbase["TrainingSnippet"][language],
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_12 = keyboard.Keyboard()
TestSnippet = visual.ImageStim(
    win=win,
    name='TestSnippet', units='pix', 
    image=example_df.iloc[1]["ImagePath"], mask=None,
    ori=0.0, pos=(0, 0), size=(example_df.iloc[1]["ImagePathWidth"], example_df.iloc[1]["ImagePathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "TrainingInput"
TrainingInputClock = core.Clock()
key_resp_13 = keyboard.Keyboard()
TrainingInput_2 = visual.ImageStim(
    win=win,
    name='TrainingInput_2', units='pix', 
    image=example_df.iloc[1]["InputPath"], mask=None,
    ori=0.0, pos=(0, 0), size=(example_df.iloc[1]["InputPathWidth"], example_df.iloc[1]["InputPathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "TrainingOutput_2"
TrainingOutput_2Clock = core.Clock()
key_resp_15 = keyboard.Keyboard()
number1 = visual.ImageStim(
    win=win,
    name='number1', units='pix', 
    image=example_df.iloc[1]["RightPath"], mask=None,
    ori=0.0, pos=(ll, 0), size=(example_df.iloc[1]["RightPathWidth"], example_df.iloc[1]["RightPathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
number2 = visual.ImageStim(
    win=win,
    name='number2', units='pix', 
    image=example_df.iloc[1]["Wrong1Path"], mask=None,
    ori=0.0, pos=(lm, 0), size=(example_df.iloc[1]["Wrong1PathWidth"], example_df.iloc[1]["Wrong1PathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
number3 = visual.ImageStim(
    win=win,
    name='number3', units='pix', 
    image=example_df.iloc[1]["Wrong2Path"], mask=None,
    ori=0.0, pos=(mm, 0), size=(example_df.iloc[1]["Wrong2PathWidth"], example_df.iloc[1]["Wrong2PathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
number4 = visual.ImageStim(
    win=win,
    name='number4', units='pix', 
    image=example_df.iloc[1]["DontKnowPath"], mask=None,
    ori=0.0, pos=(rm, 0), size=(example_df.iloc[1]["DontKnowPathWidth"], example_df.iloc[1]["DontKnowPathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
number5 = visual.ImageStim(
    win=win,
    name='number5', units='pix', 
    image=example_df.iloc[1]["NextPath"], mask=None,
    ori=0.0, pos=(rr, 0), size=(example_df.iloc[1]["NextPathWidth"], example_df.iloc[1]["NextPathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
arrow_2 = visual.ImageStim(
    win=win,
    name='arrow_2', units='pix', 
    image='Resources/arrow.png', mask=None,
    ori=0.0, pos=[0,0], size=(86, 54),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# Initialize components for Routine "CrossExplain"
CrossExplainClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=textbase["Crossexplain"][language],
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_16 = keyboard.Keyboard()

# Initialize components for Routine "Crossfixation"
CrossfixationClock = core.Clock()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='Resources\\\\corss.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.05, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=True,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "Frage"
FrageClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=textbase["Question"][language],
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_14 = keyboard.Keyboard()

# Initialize components for Routine "SyntaxInstruction"
SyntaxInstructionClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=textbase["SyntaxInstruction"][language],
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "SampleSyntax"
SampleSyntaxClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=textbase["SampleSyntax"][language],
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sampleSyntax = visual.ImageStim(
    win=win,
    name='sampleSyntax', units='pix', 
    image=syntax_df.iloc[syntax_idx]["ImagePath"], mask=None,
    ori=0.0, pos=(0, mu), size=(syntax_df.iloc[syntax_idx]["ImagePathWidth"],syntax_df.iloc[syntax_idx]["ImagePathHeight"]),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Pfeiltaste = keyboard.Keyboard()
weiter = keyboard.Keyboard()

# Initialize components for Routine "Crossfixation"
CrossfixationClock = core.Clock()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='Resources\\\\corss.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.05, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=True,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "Overview"
OverviewClock = core.Clock()
overview = visual.TextStim(win=win, name='overview',
    text=textbase["Overview"][language],
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
warningStartStudy = visual.ImageStim(
    win=win,
    name='warningStartStudy', 
    image='Resources\\\\Intro\\\\stopp.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "eeg_setup"
eeg_setupClock = core.Clock()

# Initialize components for Routine "Warning"
WarningClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text=textbase["DoNotMove"][language],
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_19 = keyboard.Keyboard()

# Initialize components for Routine "SetVariables"
SetVariablesClock = core.Clock()
import random





# Initialize components for Routine "ShowImage"
ShowImageClock = core.Clock()
Image = visual.ImageStim(
    win=win,
    name='Image', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
response = keyboard.Keyboard()

# Initialize components for Routine "ShowInput"
ShowInputClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "ShowOptions"
ShowOptionsClock = core.Clock()
image_1 = visual.ImageStim(
    win=win,
    name='image_1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
arrow = visual.ImageStim(
    win=win,
    name='arrow', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(86, 54),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "updateIndex"
updateIndexClock = core.Clock()

# Initialize components for Routine "Crossfixation"
CrossfixationClock = core.Clock()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='Resources\\\\corss.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.05, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=True,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "SyntaxWarning"
SyntaxWarningClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text=textbase["BeforeSearchTask"][language],
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_17 = keyboard.Keyboard()

# Initialize components for Routine "SyntaxTask"
SyntaxTaskClock = core.Clock()
image_8 = visual.ImageStim(
    win=win,
    name='image_8', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_18 = keyboard.Keyboard()

# Initialize components for Routine "Crossfixation"
CrossfixationClock = core.Clock()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='Resources\\\\corss.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.05, 0.05),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=True,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "AskToContinue"
AskToContinueClock = core.Clock()
continuQuestion = visual.TextStim(win=win, name='continuQuestion',
    text=textbase["Continue"][language],
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
stop = keyboard.Keyboard()
from psychopy.hardware import keyboard
from psychopy import core
import time


kb = keyboard.Keyboard()

# Initialize components for Routine "EndEEG"
EndEEGClock = core.Clock()

# Initialize components for Routine "Danke"
DankeClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Danke fürs Teilnehmen.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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

# ------Prepare to start Routine "Hello"-------
continueRoutine = True
# update component parameters for each repeat
text_13.setText(textbase["Hello"][language])
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
HelloComponents = [text_13, key_resp_11]
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
# the Routine "Hello" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
InstructionsComponents = [text_5, key_resp_6]
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
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
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

# ------Prepare to start Routine "Hello_World"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Hello_WorldComponents = [HelloWorldImage, key_resp, text_2]
for thisComponent in Hello_WorldComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Hello_WorldClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Hello_World"-------
while continueRoutine:
    # get current time
    t = Hello_WorldClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Hello_WorldClock)
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
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Hello_WorldComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Hello_World"-------
for thisComponent in Hello_WorldComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('HelloWorldImage.started', HelloWorldImage.tStartRefresh)
thisExp.addData('HelloWorldImage.stopped', HelloWorldImage.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "Hello_World" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "input"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
inputComponents = [helloWorldInput, key_resp_4, text_11]
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
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# the Routine "input" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "output"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
from psychopy.hardware import keyboard
from psychopy import core

kb = keyboard.Keyboard()

arrow_pos_array = [ll, lm, mm, rm, rr]
arrow_idx_test = 0
# keep track of which components have finished
outputComponents = [key_resp_5, helloWorld_1, helloWorld_2, helloWorld_3, helloWorld_4, Fragezeichen, text_4, image_6]
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
            key_resp_5.keys = [key.name for key in _key_resp_5_allKeys]  # storing all keys
            key_resp_5.rt = [key.rt for key in _key_resp_5_allKeys]
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
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    if image_6.status == STARTED:  # only update if drawing
        image_6.setPos((arrow_pos_array[arrow_idx_test], md))
    
    keys = kb.getKeys(['right', 'left'], waitRelease=True)
    if 'left' in keys:
        arrow_idx_test = arrow_idx_test - 1
    
    if 'right' in keys:
        arrow_idx_test = arrow_idx_test + 1
        
    arrow_idx_test = max(0, arrow_idx_test)
    arrow_idx_test = min(4, arrow_idx_test)
    
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
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
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
thisExp.addData('image_6.started', image_6.tStartRefresh)
thisExp.addData('image_6.stopped', image_6.tStopRefresh)
# the Routine "output" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TrainingSnippet"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
TrainingSnippetComponents = [text_14, key_resp_12, TestSnippet]
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
    
    # *TestSnippet* updates
    if TestSnippet.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TestSnippet.frameNStart = frameN  # exact frame index
        TestSnippet.tStart = t  # local t and not account for scr refresh
        TestSnippet.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TestSnippet, 'tStartRefresh')  # time at next scr refresh
        TestSnippet.setAutoDraw(True)
    
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
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('TestSnippet.started', TestSnippet.tStartRefresh)
thisExp.addData('TestSnippet.stopped', TestSnippet.tStopRefresh)
# the Routine "TrainingSnippet" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TrainingInput"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
TrainingInputComponents = [key_resp_13, TrainingInput_2]
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
    
    # *TrainingInput_2* updates
    if TrainingInput_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TrainingInput_2.frameNStart = frameN  # exact frame index
        TrainingInput_2.tStart = t  # local t and not account for scr refresh
        TrainingInput_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TrainingInput_2, 'tStartRefresh')  # time at next scr refresh
        TrainingInput_2.setAutoDraw(True)
    
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
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('TrainingInput_2.started', TrainingInput_2.tStartRefresh)
thisExp.addData('TrainingInput_2.stopped', TrainingInput_2.tStopRefresh)
# the Routine "TrainingInput" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TrainingOutput_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
from psychopy.hardware import keyboard
from psychopy import core

kb = keyboard.Keyboard()

arrow_pos_array = [ll, lm, mm, rm, rr]
arrow_idx_test = 0
# keep track of which components have finished
TrainingOutput_2Components = [key_resp_15, number1, number2, number3, number4, number5, arrow_2]
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
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = [key.name for key in _key_resp_15_allKeys]  # storing all keys
            key_resp_15.rt = [key.rt for key in _key_resp_15_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # *number1* updates
    if number1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        number1.frameNStart = frameN  # exact frame index
        number1.tStart = t  # local t and not account for scr refresh
        number1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(number1, 'tStartRefresh')  # time at next scr refresh
        number1.setAutoDraw(True)
    
    # *number2* updates
    if number2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        number2.frameNStart = frameN  # exact frame index
        number2.tStart = t  # local t and not account for scr refresh
        number2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(number2, 'tStartRefresh')  # time at next scr refresh
        number2.setAutoDraw(True)
    
    # *number3* updates
    if number3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        number3.frameNStart = frameN  # exact frame index
        number3.tStart = t  # local t and not account for scr refresh
        number3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(number3, 'tStartRefresh')  # time at next scr refresh
        number3.setAutoDraw(True)
    
    # *number4* updates
    if number4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        number4.frameNStart = frameN  # exact frame index
        number4.tStart = t  # local t and not account for scr refresh
        number4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(number4, 'tStartRefresh')  # time at next scr refresh
        number4.setAutoDraw(True)
    
    # *number5* updates
    if number5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        number5.frameNStart = frameN  # exact frame index
        number5.tStart = t  # local t and not account for scr refresh
        number5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(number5, 'tStartRefresh')  # time at next scr refresh
        number5.setAutoDraw(True)
    
    # *arrow_2* updates
    if arrow_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arrow_2.frameNStart = frameN  # exact frame index
        arrow_2.tStart = t  # local t and not account for scr refresh
        arrow_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arrow_2, 'tStartRefresh')  # time at next scr refresh
        arrow_2.setAutoDraw(True)
    if arrow_2.status == STARTED:  # only update if drawing
        arrow_2.setPos((arrow_pos_array[arrow_idx_test], md))
    
    keys = kb.getKeys(['right', 'left'], waitRelease=True)
    if 'left' in keys:
        arrow_idx_test = arrow_idx_test - 1
    
    if 'right' in keys:
        arrow_idx_test = arrow_idx_test + 1
        
    arrow_idx_test = max(0, arrow_idx_test)
    arrow_idx_test = min(4, arrow_idx_test)
    
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
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys = None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.addData('key_resp_15.started', key_resp_15.tStartRefresh)
thisExp.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('number1.started', number1.tStartRefresh)
thisExp.addData('number1.stopped', number1.tStopRefresh)
thisExp.addData('number2.started', number2.tStartRefresh)
thisExp.addData('number2.stopped', number2.tStopRefresh)
thisExp.addData('number3.started', number3.tStartRefresh)
thisExp.addData('number3.stopped', number3.tStopRefresh)
thisExp.addData('number4.started', number4.tStartRefresh)
thisExp.addData('number4.stopped', number4.tStopRefresh)
thisExp.addData('number5.started', number5.tStartRefresh)
thisExp.addData('number5.stopped', number5.tStopRefresh)
thisExp.addData('arrow_2.started', arrow_2.tStartRefresh)
thisExp.addData('arrow_2.stopped', arrow_2.tStopRefresh)
# the Routine "TrainingOutput_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "CrossExplain"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_16.keys = []
key_resp_16.rt = []
_key_resp_16_allKeys = []
# keep track of which components have finished
CrossExplainComponents = [text_3, key_resp_16]
for thisComponent in CrossExplainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CrossExplainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "CrossExplain"-------
while continueRoutine:
    # get current time
    t = CrossExplainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CrossExplainClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_16* updates
    waitOnFlip = False
    if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_16.frameNStart = frameN  # exact frame index
        key_resp_16.tStart = t  # local t and not account for scr refresh
        key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_16.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_16.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_16_allKeys.extend(theseKeys)
        if len(_key_resp_16_allKeys):
            key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
            key_resp_16.rt = _key_resp_16_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CrossExplainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "CrossExplain"-------
for thisComponent in CrossExplainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_16.keys in ['', [], None]:  # No response was made
    key_resp_16.keys = None
thisExp.addData('key_resp_16.keys',key_resp_16.keys)
if key_resp_16.keys != None:  # we had a response
    thisExp.addData('key_resp_16.rt', key_resp_16.rt)
thisExp.addData('key_resp_16.started', key_resp_16.tStartRefresh)
thisExp.addData('key_resp_16.stopped', key_resp_16.tStopRefresh)
thisExp.nextEntry()
# the Routine "CrossExplain" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Crossfixation"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
CrossfixationComponents = [image_7]
for thisComponent in CrossfixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CrossfixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Crossfixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = CrossfixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CrossfixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    if image_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_7.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_7.tStop = t  # not accounting for scr refresh
            image_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_7, 'tStopRefresh')  # time at next scr refresh
            image_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CrossfixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Crossfixation"-------
for thisComponent in CrossfixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_7.started', image_7.tStartRefresh)
thisExp.addData('image_7.stopped', image_7.tStopRefresh)

# ------Prepare to start Routine "Frage"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
FrageComponents = [text, key_resp_14]
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
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
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
        theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
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
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.addData('key_resp_14.started', key_resp_14.tStartRefresh)
thisExp.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
thisExp.nextEntry()
# the Routine "Frage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SyntaxInstruction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
SyntaxInstructionComponents = [text_6, key_resp_7]
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
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
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
syntax_idx += 1
# the Routine "SampleSyntax" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Crossfixation"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
CrossfixationComponents = [image_7]
for thisComponent in CrossfixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CrossfixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Crossfixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = CrossfixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CrossfixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    if image_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_7.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_7.tStop = t  # not accounting for scr refresh
            image_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_7, 'tStopRefresh')  # time at next scr refresh
            image_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CrossfixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Crossfixation"-------
for thisComponent in CrossfixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_7.started', image_7.tStartRefresh)
thisExp.addData('image_7.stopped', image_7.tStopRefresh)

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
Warning_StartSessionComponents = [key_resp_9, warningStartStudy]
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
thisExp.addData('warningStartStudy.started', warningStartStudy.tStartRefresh)
thisExp.addData('warningStartStudy.stopped', warningStartStudy.tStopRefresh)
# the Routine "Warning_StartSession" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "eeg_setup"-------
continueRoutine = True
# update component parameters for each repeat
eeg_rec = None
logger = None
if use_eeg==True:
    eeg_rec = Recorder()
    eeg_rec.connect()
    eeg_rec.connect_plot()
    eeg_rec.start_recording()

if use_eyetracker==True:
    logger = Logger("exepriment_data.csv")
    logger.add_key_to_log('left_gaze_point_in_user_coordinate_system')
    logger.add_key_to_log('left_gaze_point_validity')
    logger.add_key_to_log('right_gaze_point_validity')
    logger.add_key_to_log('right_gaze_point_in_user_coordinate_system')
    logger.add_key_to_log('left_gaze_origin_in_user_coordinate_system')
    logger.add_key_to_log('right_gaze_origin_in_user_coordinate_system')
    logger.add_key_to_log('left_gaze_point_on_display_area')
    logger.add_key_to_log('right_gaze_point_on_display_area')
    logger.add_key_to_log('system_time_stamp')
    logger.add_key_to_log('left_pupil_diameter')
    logger.add_key_to_log('right_pupil_diameter')
    logger.start_recording()

# keep track of which components have finished
eeg_setupComponents = []
for thisComponent in eeg_setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
eeg_setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "eeg_setup"-------
while continueRoutine:
    # get current time
    t = eeg_setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=eeg_setupClock)
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
    for thisComponent in eeg_setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "eeg_setup"-------
for thisComponent in eeg_setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "eeg_setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Warning"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_19.keys = []
key_resp_19.rt = []
_key_resp_19_allKeys = []
# keep track of which components have finished
WarningComponents = [text_12, key_resp_19]
for thisComponent in WarningComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WarningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Warning"-------
while continueRoutine:
    # get current time
    t = WarningClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WarningClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *key_resp_19* updates
    waitOnFlip = False
    if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_19.frameNStart = frameN  # exact frame index
        key_resp_19.tStart = t  # local t and not account for scr refresh
        key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_19.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_19.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_19_allKeys.extend(theseKeys)
        if len(_key_resp_19_allKeys):
            key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
            key_resp_19.rt = _key_resp_19_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WarningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Warning"-------
for thisComponent in WarningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# check responses
if key_resp_19.keys in ['', [], None]:  # No response was made
    key_resp_19.keys = None
thisExp.addData('key_resp_19.keys',key_resp_19.keys)
if key_resp_19.keys != None:  # we had a response
    thisExp.addData('key_resp_19.rt', key_resp_19.rt)
thisExp.addData('key_resp_19.started', key_resp_19.tStartRefresh)
thisExp.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
thisExp.nextEntry()
# the Routine "Warning" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=8, method='random', 
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
    Loop = data.TrialHandler(nReps=4, method='random', 
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
        
        # ------Prepare to start Routine "SetVariables"-------
        continueRoutine = True
        # update component parameters for each repeat
        if use_eeg==True: 
            eeg_rec.refresh()
            eeg_rec.set_event(current_idx%1000000007)
        
        current_image_path = inbook.iloc[current_idx]["ImagePath"]
        width = inbook.iloc[current_idx]["ImagePathWidth"]
        height = inbook.iloc[current_idx]["ImagePathHeight"]
        
        current_input_path = inbook.iloc[current_idx]["InputPath"]
        input_width = inbook.iloc[current_idx]["InputPathWidth"]
        input_height = inbook.iloc[current_idx]["InputPathHeight"]
        
        right_path = inbook.iloc[current_idx]["RightPath"]
        right_width = inbook.iloc[current_idx]["RightPathWidth"]
        right_height = inbook.iloc[current_idx]["RightPathHeight"]
        
        wrong1_input_path = inbook.iloc[current_idx]["Wrong1Path"]
        wrong1_width = inbook.iloc[current_idx]["Wrong1PathWidth"]
        wrong1_height = inbook.iloc[current_idx]["Wrong1PathHeight"]
        
        wrong2_input_path = inbook.iloc[current_idx]["Wrong2Path"]
        wrong2_width = inbook.iloc[current_idx]["Wrong2PathWidth"]
        wrong2_height = inbook.iloc[current_idx]["Wrong2PathHeight"]
        
        dk_input_path = inbook.iloc[current_idx]["DontKnowPath"]
        dk_width = inbook.iloc[current_idx]["DontKnowPathWidth"]
        dk_height = inbook.iloc[current_idx]["DontKnowPathHeight"]
        
        next_input_path = inbook.iloc[current_idx]["NextPath"]
        next_width = inbook.iloc[current_idx]["NextPathWidth"]
        next_height = inbook.iloc[current_idx]["NextPathHeight"]
        
        answer_array = [right_path, wrong1_input_path, wrong2_input_path]
        width_array = [right_width, wrong1_width, wrong2_width]
        height_array = [right_height, wrong1_height, wrong2_height]
        
        answer_idx = [0,1,2]
        random.shuffle(answer_idx)
        # keep track of which components have finished
        SetVariablesComponents = []
        for thisComponent in SetVariablesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        SetVariablesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "SetVariables"-------
        while continueRoutine:
            # get current time
            t = SetVariablesClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=SetVariablesClock)
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
            for thisComponent in SetVariablesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "SetVariables"-------
        for thisComponent in SetVariablesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "SetVariables" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ShowImage"-------
        continueRoutine = True
        routineTimer.add(180.000000)
        # update component parameters for each repeat
        Image.setSize([width, height])
        Image.setImage(current_image_path)
        response.keys = []
        response.rt = []
        _response_allKeys = []
        if use_eeg==True: 
            eeg_rec.refresh()
            eeg_rec.set_event(hash("DisplayImage" + str(current_idx))%1000000007)
        thisExp.addData("ImagePath", inbook.iloc[current_idx]["ImagePath"])
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
        while continueRoutine and routineTimer.getTime() > 0:
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
            if Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Image.tStartRefresh + 180-frameTolerance:
                    # keep track of stop time/frame for later
                    Image.tStop = t  # not accounting for scr refresh
                    Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Image, 'tStopRefresh')  # time at next scr refresh
                    Image.setAutoDraw(False)
            
            # *response* updates
            if response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                response.clock.reset()  # now t=0
                response.clearEvents(eventType='keyboard')
            if response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response.tStartRefresh + 180-frameTolerance:
                    # keep track of stop time/frame for later
                    response.tStop = t  # not accounting for scr refresh
                    response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response, 'tStopRefresh')  # time at next scr refresh
                    response.status = FINISHED
            if response.status == STARTED:
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
        
        
        
        
        # ------Prepare to start Routine "ShowInput"-------
        continueRoutine = True
        routineTimer.add(30.000000)
        # update component parameters for each repeat
        image.setSize([input_width, input_height])
        image.setImage(current_input_path)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        if use_eeg==True: 
            eeg_rec.refresh()
            eeg_rec.set_event(hash("ShowInput" + str(current_idx))%1000000007)
        thisExp.addData("InputPath", inbook.iloc[current_idx]["InputPath"])
        # keep track of which components have finished
        ShowInputComponents = [image, key_resp_2]
        for thisComponent in ShowInputComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ShowInputClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ShowInput"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ShowInputClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ShowInputClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 30.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
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
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 30.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ShowInputComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ShowInput"-------
        for thisComponent in ShowInputComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Loop.addData('image.started', image.tStartRefresh)
        Loop.addData('image.stopped', image.tStopRefresh)
        
        # ------Prepare to start Routine "ShowOptions"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_1.setPos((ll, 0))
        image_1.setSize([width_array[answer_idx[0]], height_array[answer_idx[0]]])
        image_1.setImage(answer_array[answer_idx[0]])
        image_2.setPos((lm, 0))
        image_2.setSize([width_array[answer_idx[1]], height_array[answer_idx[1]]])
        image_2.setImage(answer_array[answer_idx[1]])
        image_3.setPos((mm, 0))
        image_3.setSize([width_array[answer_idx[2]], height_array[answer_idx[2]]])
        image_3.setImage(answer_array[answer_idx[2]])
        image_4.setPos((rm, 0))
        image_4.setSize([dk_width, dk_height])
        image_4.setImage(dk_input_path)
        image_5.setPos((rr, 0))
        image_5.setSize([next_width, next_height])
        image_5.setImage(next_input_path)
        arrow.setImage('Resources/arrow.png')
        from psychopy.hardware import keyboard
        from psychopy import core
        
        if use_eeg==True: 
            eeg_rec.refresh()
            eeg_rec.set_event(hash("GetInput" + str(current_idx))%1000000007)
        thisExp.addData("ImagePathInputs", inbook.iloc[current_idx]["ImagePath"])
        
        kb = keyboard.Keyboard()
        
        answers = []
        current = 0
        position_array = [ll, lm, mm, rm, rr]
        arrow_position = position_array[current]
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        ShowOptionsComponents = [image_1, image_2, image_3, image_4, image_5, arrow, key_resp_3]
        for thisComponent in ShowOptionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ShowOptionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ShowOptions"-------
        while continueRoutine:
            # get current time
            t = ShowOptionsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ShowOptionsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_1* updates
            if image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_1.frameNStart = frameN  # exact frame index
                image_1.tStart = t  # local t and not account for scr refresh
                image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
                image_1.setAutoDraw(True)
            if image_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_1.tStartRefresh + 30.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_1.tStop = t  # not accounting for scr refresh
                    image_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_1, 'tStopRefresh')  # time at next scr refresh
                    image_1.setAutoDraw(False)
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            if image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_2.tStartRefresh + 30.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                    image_2.setAutoDraw(False)
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            if image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_3.tStartRefresh + 30.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_3.tStop = t  # not accounting for scr refresh
                    image_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                    image_3.setAutoDraw(False)
            
            # *image_4* updates
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                image_4.setAutoDraw(True)
            if image_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_4.tStartRefresh + 30.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_4.tStop = t  # not accounting for scr refresh
                    image_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
                    image_4.setAutoDraw(False)
            
            # *image_5* updates
            if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                image_5.setAutoDraw(True)
            if image_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_5.tStartRefresh + 30.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_5.tStop = t  # not accounting for scr refresh
                    image_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
                    image_5.setAutoDraw(False)
            
            # *arrow* updates
            if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow.frameNStart = frameN  # exact frame index
                arrow.tStart = t  # local t and not account for scr refresh
                arrow.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
                arrow.setAutoDraw(True)
            if arrow.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > arrow.tStartRefresh + 30.0-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow.tStop = t  # not accounting for scr refresh
                    arrow.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(arrow, 'tStopRefresh')  # time at next scr refresh
                    arrow.setAutoDraw(False)
            if arrow.status == STARTED:  # only update if drawing
                arrow.setPos((arrow_position, md))
            
            keys = kb.getKeys(['right', 'left'], waitRelease=True)
            if 'left' in keys:
                current = current - 1
            
            if 'right' in keys:
                current = current + 1
                
            current = max(0, current)
            current = min(4, current)
            
            arrow_position = position_array[current]
            
            
            
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
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ShowOptionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ShowOptions"-------
        for thisComponent in ShowOptionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Loop.addData('image_1.started', image_1.tStartRefresh)
        Loop.addData('image_1.stopped', image_1.tStopRefresh)
        Loop.addData('image_2.started', image_2.tStartRefresh)
        Loop.addData('image_2.stopped', image_2.tStopRefresh)
        Loop.addData('image_3.started', image_3.tStartRefresh)
        Loop.addData('image_3.stopped', image_3.tStopRefresh)
        Loop.addData('image_4.started', image_4.tStartRefresh)
        Loop.addData('image_4.stopped', image_4.tStopRefresh)
        Loop.addData('image_5.started', image_5.tStartRefresh)
        Loop.addData('image_5.stopped', image_5.tStopRefresh)
        Loop.addData('arrow.started', arrow.tStartRefresh)
        Loop.addData('arrow.stopped', arrow.tStopRefresh)
        answer = ""
        if current == 0:
            answer = answer_array[answer_idx[0]]
        elif current == 1:
            answer = answer_array[answer_idx[1]]
        elif current == 2:
            answer = answer_array[answer_idx[2]]
        elif current == 3:
            answer = "None"
        else:
            answer = "Skipped"
        
        
        thisExp.addData("ChoosenAnwer", answer)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        Loop.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            Loop.addData('key_resp_3.rt', key_resp_3.rt)
        Loop.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        Loop.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        # the Routine "ShowOptions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "updateIndex"-------
        continueRoutine = True
        # update component parameters for each repeat
        try:
            current_idx = idx_values.pop(0)
        except:
            pass
        # keep track of which components have finished
        updateIndexComponents = []
        for thisComponent in updateIndexComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        updateIndexClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "updateIndex"-------
        while continueRoutine:
            # get current time
            t = updateIndexClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=updateIndexClock)
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
            for thisComponent in updateIndexComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "updateIndex"-------
        for thisComponent in updateIndexComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "updateIndex" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Crossfixation"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        CrossfixationComponents = [image_7]
        for thisComponent in CrossfixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        CrossfixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Crossfixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = CrossfixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=CrossfixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_7* updates
            if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                image_7.setAutoDraw(True)
            if image_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_7.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_7.tStop = t  # not accounting for scr refresh
                    image_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_7, 'tStopRefresh')  # time at next scr refresh
                    image_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CrossfixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Crossfixation"-------
        for thisComponent in CrossfixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Loop.addData('image_7.started', image_7.tStartRefresh)
        Loop.addData('image_7.stopped', image_7.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 4 repeats of 'Loop'
    
    
    # ------Prepare to start Routine "SyntaxWarning"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_17.keys = []
    key_resp_17.rt = []
    _key_resp_17_allKeys = []
    # keep track of which components have finished
    SyntaxWarningComponents = [text_8, key_resp_17]
    for thisComponent in SyntaxWarningComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SyntaxWarningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SyntaxWarning"-------
    while continueRoutine:
        # get current time
        t = SyntaxWarningClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SyntaxWarningClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # *key_resp_17* updates
        waitOnFlip = False
        if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.tStart = t  # local t and not account for scr refresh
            key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_17.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_17.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_17_allKeys.extend(theseKeys)
            if len(_key_resp_17_allKeys):
                key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SyntaxWarningComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SyntaxWarning"-------
    for thisComponent in SyntaxWarningComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_8.started', text_8.tStartRefresh)
    trials.addData('text_8.stopped', text_8.tStopRefresh)
    # check responses
    if key_resp_17.keys in ['', [], None]:  # No response was made
        key_resp_17.keys = None
    trials.addData('key_resp_17.keys',key_resp_17.keys)
    if key_resp_17.keys != None:  # we had a response
        trials.addData('key_resp_17.rt', key_resp_17.rt)
    trials.addData('key_resp_17.started', key_resp_17.tStartRefresh)
    trials.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
    # the Routine "SyntaxWarning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "SyntaxTask"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_8.setSize((syntax_df.iloc[syntax_idx]["ImagePathWidth"], syntax_df.iloc[syntax_idx]["ImagePathHeight"]))
    image_8.setImage(syntax_df.iloc[syntax_idx]["ImagePath"])
    key_resp_18.keys = []
    key_resp_18.rt = []
    _key_resp_18_allKeys = []
    # keep track of which components have finished
    SyntaxTaskComponents = [image_8, key_resp_18]
    for thisComponent in SyntaxTaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SyntaxTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SyntaxTask"-------
    while continueRoutine:
        # get current time
        t = SyntaxTaskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SyntaxTaskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_8* updates
        if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_8.frameNStart = frameN  # exact frame index
            image_8.tStart = t  # local t and not account for scr refresh
            image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
            image_8.setAutoDraw(True)
        if image_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_8.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                image_8.tStop = t  # not accounting for scr refresh
                image_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_8, 'tStopRefresh')  # time at next scr refresh
                image_8.setAutoDraw(False)
        
        # *key_resp_18* updates
        waitOnFlip = False
        if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_18.frameNStart = frameN  # exact frame index
            key_resp_18.tStart = t  # local t and not account for scr refresh
            key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
            key_resp_18.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_18.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_18.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_18_allKeys.extend(theseKeys)
            if len(_key_resp_18_allKeys):
                key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
                key_resp_18.rt = _key_resp_18_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SyntaxTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SyntaxTask"-------
    for thisComponent in SyntaxTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image_8.started', image_8.tStartRefresh)
    trials.addData('image_8.stopped', image_8.tStopRefresh)
    # check responses
    if key_resp_18.keys in ['', [], None]:  # No response was made
        key_resp_18.keys = None
    trials.addData('key_resp_18.keys',key_resp_18.keys)
    if key_resp_18.keys != None:  # we had a response
        trials.addData('key_resp_18.rt', key_resp_18.rt)
    trials.addData('key_resp_18.started', key_resp_18.tStartRefresh)
    trials.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
    if use_eeg==True: 
        eeg_rec.refresh()
        eeg_rec.set_event(hash("SyntaxTask" + str(syntax_idx))%1000000007)
    syntax_idx += 1
    # the Routine "SyntaxTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Crossfixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CrossfixationComponents = [image_7]
    for thisComponent in CrossfixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CrossfixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Crossfixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CrossfixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CrossfixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_7* updates
        if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_7.frameNStart = frameN  # exact frame index
            image_7.tStart = t  # local t and not account for scr refresh
            image_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
            image_7.setAutoDraw(True)
        if image_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_7.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_7.tStop = t  # not accounting for scr refresh
                image_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_7, 'tStopRefresh')  # time at next scr refresh
                image_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CrossfixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Crossfixation"-------
    for thisComponent in CrossfixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image_7.started', image_7.tStartRefresh)
    trials.addData('image_7.stopped', image_7.tStopRefresh)
    
    # ------Prepare to start Routine "AskToContinue"-------
    continueRoutine = True
    # update component parameters for each repeat
    stop.keys = []
    stop.rt = []
    _stop_allKeys = []
    stop_experiment = False
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
        
        keys = kb.getKeys(['s'], waitRelease=True)
        
        if stop_experiment == True:
            time.sleep(10.0)
            core.quit()
        
        if 's' in keys:
            continuQuestion.setText("Danke für die Teilnahme")
            if use_eeg:
                eeg_rec.refresh()
                eeg_rec.disconnect()
                eeg_rec.save("CollectedData")
            if use_eyetracker:
                logger.stop_recording()
            stop_experiment = True
            
        
        
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
    
# completed 8 repeats of 'trials'


# ------Prepare to start Routine "EndEEG"-------
continueRoutine = True
# update component parameters for each repeat
if use_eeg:
    eeg_rec.refresh()
    eeg_rec.disconnect()
    eeg_rec.save("CollectedData")
if use_eyetracker:
    logger.stop_recording()
# keep track of which components have finished
EndEEGComponents = []
for thisComponent in EndEEGComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndEEGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndEEG"-------
while continueRoutine:
    # get current time
    t = EndEEGClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndEEGClock)
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
    for thisComponent in EndEEGComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndEEG"-------
for thisComponent in EndEEGComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EndEEG" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Danke"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
DankeComponents = [text_15]
for thisComponent in DankeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DankeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Danke"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = DankeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DankeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    if text_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_15.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text_15.tStop = t  # not accounting for scr refresh
            text_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_15, 'tStopRefresh')  # time at next scr refresh
            text_15.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DankeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Danke"-------
for thisComponent in DankeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)

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
