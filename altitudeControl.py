################################################################################################

## Project Banner: Main Module v2.3
## Created: 07-11-2016 by Madeline McMillan and Nate Peirson
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

## The altitude control system

################################################################################################

## All valve related lines currently commented out.
## Functions have been moved to own file ballast.py

import gps
from smbus import SMBus
from thermocouple import readThermo
import time
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import gpsPull
import bannerSettings

# variable initialization
file_name = ('/home/pi/Desktop/Bruce/logs/loiterLog-' + gpsPull.timeGet() +'.txt') # name your log file here
balloonStatus = 1
valveStatus = 0
coilStatus = 0
sample = False
acceleration = 0
state = 'Waiting...'
near = 0

# RPi IO port initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(bannerSettings.balloonPin(), GPIO.OUT)
GPIO.setup(bannerSettings.ballastPin(), GPIO.OUT)
GPIO.setup(bannerSettings.gpsLedPin(), GPIO.OUT)
GPIO.setup(bannerSettings.tempSensorLedPin(), GPIO.OUT)

# terminal feedback
print('- Altitude Control Engaged')

# logging function for control system actions
# tab deliniated by '\t'
# write your data from function or variable by text_file.write(str(columnOneData) + '\t' + str(columnTwoData) + 't' + ... )
def takeLog():
    global valveStatus
    global balloonStatus
    global coilStatus
    with open(file_name, 'a') as text_file:
        text_file.write(str(gpsPull.timeGet()) + '\t' + str(ballonStatus) + '\t' + str(coilStatus) + '\t' + str(valveStatus) + '\t' + str(gpsPull.altGet()) + '\t' + str(gpsPull.climbGet()) + '\t' + str(state) + '\n')
        

# this function pulls samples of the rate of ascent to establish an average for later use. Climb data comes from GPS.
# math could probably be improved.
def sampleClimb():
    global sample
    global acceleration
    currentClimb = gpsPull.climbGet()
    time.sleep(0.07)
    acceleration = (gpsPull.climbGet() - currentClimb)/0.07

# Turns release coil ON, then listens for sudden acceleration change indicating balloon release. Includes timeout.
def releaseBalloon():
    global balloonStatus
    global coilStatus
    global state
    global acceleration
    sampleClimb()
    initialAcceleration = acceleration
    initialTime = time.time()
    GPIO.output(bannerSettings.balloonPin(), GPIO.HIGH)
    coilStatus = 1
    state = 'Coil on'
    takeLog()
    while coilStatus == 1:
        sampleClimb()
        if abs(acceleration - initialAcceleration) >= bannerSettings.deltaA(): # acceleration change listener. Customize threshold in bannerSettings.py
            GPIO.output(bannerSettings.balloonPin(), GPIO.LOW)
            coilStatus = 2
            state = 'Coil off (dA)'
            balloonStatus = 0
            takeLog()
        elif time.time() - initialTime >= 2: # set your timeout here for safety
            GPIO.output(bannerSettings.balloonPin(), GPIO.LOW)
            coilStatus = 2
            state = 'Coil off (timeout)'
            balloonStatus = 0
            takeLog()

# This function attempts to correct any major error in buoyancy after the lift balloon is released.
# In other words, if payload is falling rapidly after balloon release, this is where it'd dump tiny bits of ballast to compensate.
# Some of the math is in while loop below
def releaseBallast(timeOpen):
    global valveStatus
    global state
    GPIO.output(bannerSettings.ballastPin(), GPIO.HIGH)
    valveStatus = 1
    state = 'Valve open'
    takeLog()
    time.sleep(timeOpen)
    valveStatus = 0
    GPIO.output(bannerSettings.ballastPin(), GPIO.LOW)
    state = 'Valve closed'
    takeLog()

# terminate loitering
# kills flight by dumping all remeainin ballast
# could replace this with main balloon severance instead
def termLoiter():
    global state
    global valveStatus
    GPIO.output(bannerSettings.ballastPin(), GPIO.HIGH)
    valveStatus = 1
    state = 'Termianting Flight'
    takeLog()
    time.sleep(120)
    GPIO.output(bannerSettings.ballastPin(), GPIO.LOW)
    valveStatus = 0
    state = 'Flight Terminated'
    takeLog()

# action log file header, tab deliniated
with open(file_name, 'w') as text_file:
    text_file.write('HABC: Project Banner\n')
    text_file.write('Loiter Log\n')
    text_file.write('\n\n')
    text_file.write('Timestamp\tBalloon Status\tCoil Status\tValve Status\tAltitude (GPS)\tRate of Ascent (GPS)\tState\n' + str(gpsPull.timeGet()) + '\t' + str(balloonStatus) + '\t' + str(coilStatus) + '\t' + str(valveStatus) + '\t' + str(gpsPull.altGet()) + '\t' + str(gpsPull.climbGet()) + '\t' + str(state))

# altitude listener to initiate entire buoyancy control operations.
# if you want to make a timeout (to prevent another Mississippi), do it here
# set initiation altitude in bannerSetting.py
while balloonStatus == 1:
    time.sleep(0.01)
    if gpsPull.altGet() >= bannerSettings.loiterAlt() and coilStatus == 0:
        loiterStartTime = time.time()
        sample = True
        releaseBalloon()

# experimental system to compensate for errors in buoyancy after lift balloon is jettisoned
# math could probably be improved
while sample == True:
    time.sleep(0.01)
    if coilStatus == 2:
        if acceleration < 0 and gpsPull.climbGet() > 0:
            timeOpen = (acceleration/5)**2
            releaseBallast(timeOpen)
            time.sleep(timeOpen + 0.07)

        if acceleration < 1 and acceleration > -1 and gpsPull.climbGet() > -1 and near == 0:
            state = 'Velocity nearing zero...'
            near = 1
            takeLog()

        if acceleration < 1 and acceleration > -1 and gpsPull.climbGet() > -1 and gpsPull.climbGet() < 1:
            sample = False
            state = 'Loitering Achieved'
            takeLog()
            
        #assuming the balloon is now loitering.

        if balloonStatus == 0 and time.time() - loiterStartTime >= bannerSettings.loiterTime():
            termLoiter()        

