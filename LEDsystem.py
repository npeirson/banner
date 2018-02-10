# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:09:17 2018

@author: Nick
"""

################################################################################################

## Project Banner: LED System
## Created: 2/9/2018 by Nate Peirson, Madeline McMillan and Nick Turner
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

###############################################################################

# super shitty method for LED signalling... don't judge me

import time
import RPi.GPIO as GPIO
import bannerSettings

def signalSearch():
    GPIO.output(bannerSettings.gpsLedPin(), GPIO.HIGH)
    time.sleep(1)
    GPIO.output(bannerSettings.gpsLedPin(), GPIO.LOW)
    
def signalAcquired():
    end_time = time.time()+30
    while time.time() < end_time:
        GPIO.output(bannerSettings.gpsLedPin(), GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(bannerSettings.gpsLedPin(), GPIO.LOW)
        time.sleep(0.1)
    

def tcGood():
    GPIO.output(bannerSettings.tempSensorLedPin(), GPIO.HIGH)
    time.sleep(5)
    GPIO.output(bannerSettings.tempSensorLedPin(), GPIO.LOW)