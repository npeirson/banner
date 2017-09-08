################################################################################################

## Project Banner: System Initialization
## Created: 07-11-2016 by Madeline McMillan and Nate Peirson
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

## This is the main file to run to initialize ALL other processes.
## Altitude control and sensor logging run on separate threads to maximize efficiency.

################################################################################################

#! /bin/sh -e
import os
import subprocess
import gps
import time
time.sleep(4)

# Initializes GPS
# No functions begin until GPS locks acquired
def startGPS():
    latitude = None
    subprocess.call(['sudo gpsd /dev/ttyUSB0 -n -F /var/run/gpsd.sock'], shell=True)
    print('\nGPS initialized, searching for satellites...\nThis might take a while...')
    time.sleep(4)
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)   
    while isinstance(latitude, float) == False:
        time.sleep(1)
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lat'):
                latitude = report.lat
        print('Searching for signal...')
    if isinstance(latitude, float) == True:
            print('Signal acquired!')
            subprocess.call(['sudo gpsd /dev/ttyUSB0 -n -F /var/run/gpsd.sock'], shell=True)
            subprocess.call(['python', '/home/pi/Desktop/Bruce/altitudeControl.py'])
            subprocess.call(['python', '/home/pi/Desktop/Bruce/mainLogging.py'])         
                
startGPS()                

