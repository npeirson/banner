"""
############################################################################

## Project Banner: System Initialization
## Created: 07-11-2016 by Madeline McMillan and Nate Peirson
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

## This is the main file to run to initialize ALL other processes.
## Altitude control & sensor logging run on separate threads for efficiency.

############################################################################
"""

#! /bin/sh -e
#pylint: disable=no-member

import subprocess
import time
import gps

def get_gps_lock():
	latitude = None
	subprocess.call(['sudo gpsd /dev/ttyUSB0 -n -F /var/run/gpsd.sock'], shell=True)
	print 'GPS initialized, searching for satellites...'
	print 'This might take a while...'
	time.sleep(2)
	session = gps.gps("localhost", "2947")
	session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
	while isinstance(latitude, float) is False:
		time.sleep(1)
		report = session.next()
		if report['class'] == 'TPV':
			if hasattr(report, 'lat'):
				latitude = report.lat
		print 'Searching for signal...'
	print 'Signal acquired!'


#get_gps_lock() # Make sure we are getting GPS data


#subprocess.call(['sudo gpsd /dev/ttyUSB0 -n -F /var/run/gpsd.sock'], shell=True)
subprocess.call(['python', './altitudeControl.py'])
subprocess.call(['python', './mainLogging.py'])
