##############################################################################

## Project Banner: Sensor Data Logging
## Created: 07-11-2016 by Madeline McMillan and Nate Peirson
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

## Sensor data points are taken by this script

##############################################################################

import gps
from smbus import SMBus
from thermocouple import readThermo
import time
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import gpsPull
from ptAltitude import ptAlt
import bannerSettings

print('- Main logging has begun') # terminal feedback
file_name = ('./logs/log-' + gpsPull.timeGet() +'.txt') # name your log file

with open(file_name, 'w') as text_file:
	# this is your log file header, tab deliniated, column by column
	text_file.write('HABC: Project Banner\nFlight Data Log\n\nTimestamp\tAir Pressure (Pa)\tOutside Temp (C)\tInside Temp (C)\tAltitude (GPS)\tAltitude (STP)\tClimb (m/Min)\tLatitude\tLongitude\n')

while True:
	adc = Adafruit_ADS1x15.ADS1015() # reference the analog to digital converter used for thermocouple
	pressure, celsius, altitude = ptAlt() # references the PTA unit
	with open(file_name, 'a') as text_file:
		print('Writing main log') # terminal feedback
		# customize the data you log, tab deliniated ('\t'), etc. E.g. text_file.write(str(columnOneDataFunction) + '\t' + str(columnTwoDataVariable) ... )
		text_file.write(str(gpsPull.timeGet()) + '\t' + str(pressure) + '\t' + str(readThermo()) + '\t' + str(celsius) + '\t' + str(gpsPull.altGet()) + '\t' + str(altitude) + '\t' + str(gpsPull.climbGet()) + '\t' + str(gpsPull.latGet()) + '\t' + str(gpsPull.lonGet()) + '\n')
		time.sleep(bannerSettings.logFreq)


