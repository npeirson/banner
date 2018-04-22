##############################################################################

## Project Banner: LED System
## Created: 11-10-2016 by Madeline McMillan and Nate Peirson
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

##############################################################################

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
