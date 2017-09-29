################################################################################################

## Project Banner: Main Module v2.3
## Created: 07-11-2016 by Madeline McMillan and Nate Peirson
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

## Cord severance software

################################################################################################

import gps
from smbus import SMBus
import time
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import gpsPull
import bannerSettings

print('Initiating altitude listener...') # terminal feedback

# variable initialization
file_name = ('/home/pi/Desktop/banner/logs/operationsLog-' + gpsPull.timeGet() +'.txt') # name your log file here
balloonStatus = 1 # is balloon attached?
coilStatus = 0 # is coil on? 0 = off before use, 1 = on/in use, 2 = off after use
state = 'Climbing...' # for operation tracking in log
reason = 'N/A' # used later to explain what triggered severence
initialTime = time.time() # record time of launch
print('- Stopwatch has begun') # terminal feedback

# RPi IO port initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(bannerSettings.balloonPin(), GPIO.OUT)
print('- Altitude listener running\n\n--==[ READY FOR LAUNCH ]==--\n') # terminal feedback

# logging function for control system actions
# tab deliniated by '\t'
# write your data from function or variable by text_file.write(str(columnOneData) + '\t' + str(columnTwoData) + 't' + ... )
def takeLog():
    global balloonStatus
    global state
    global reason
    with open(file_name, 'a') as text_file:
        text_file.write(str(gpsPull.timeGet()) + '\t' + str(ballonStatus) + '\t' + str(gpsPull.altGet()) + '\t' + str(gpsPull.climbGet()) + '\t' + str(state) + '\t' + str(reason) + '\n')

# Turns release coil ON
def releaseBalloon():
    global balloonStatus
    global coilStatus
    global state
    GPIO.output(bannerSettings.balloonPin(), GPIO.HIGH) # turn coil on
    coilStartTime = time.time() # records time when coil turns on
    coilStatus = 1
    state = 'Coil on'
    takeLog()
    while coilStatus == 1: # while the coil is cookin'...
        if gpsPull.climbGet() <= -1 or time.time() - coilStartTime >= bannerSettings.cookTime(): # if payload is falling or maximum coil time has passed
            GPIO.output(bannerSettings.balloonPin(), GPIO.LOW) # turn coil off
            coilStatus = 2
            state = 'Coil off'
            balloonStatus = 0
            takeLog()

# action log file header, tab deliniated
with open(file_name, 'w') as text_file:
    text_file.write('HABC: Project Banner\n')
    text_file.write('Loiter Log\n')
    text_file.write('\n\n')
    text_file.write('Timestamp\tBalloon Status\tAltitude (GPS)\tRate of Ascent (GPS)\tState\tReason\n' + str(gpsPull.timeGet()) + '\t' + str(balloonStatus) + '\t' + str(gpsPull.altGet()) + '\t' + str(gpsPull.climbGet()) + '\t' + str(state) + '\t' + str(reason) + '\n')

# altitude listener and stopwatch to initiate cable severance
# set kill altitude (killAlt) and timeout in bannerSetting.py
while balloonStatus == 1:
    time.sleep(0.5) # checks altitude and flight time this often (seconds)
    if gpsPull.altGet() >= bannerSettings.killAlt() and coilStatus == 0:
        reason = 'Target Altitude Achieved'
        releaseBalloon()
    elif time.time() - initialTime >= bannerSettings.timeout() and coilStatus == 0:
        reason = 'Killed by Timeout'
        releaseBalloon()    