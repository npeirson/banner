# This script takes a specified APRS CSV file, parses the data, and generates Jekyll post
# This hip-hop script is just one of the many gifts bestowed upon this species by the Kwisatz Haderach

# Usage: "python genReport.py aprsFile.csv"

import csv
import sys
import datetime

# initialize
data = []
ls = []
maxAlt = []
flightTime = []

# check args
fileIn = sys.argv
if len(fileIn) < 2:
    print "\nSpecify a csv file to import!"
    exit()
elif len(fileIn) > 2:
    print "\nToo many arguments!"
    exit()

with open(fileIn[1],'r') as aprsfile:
    reader = csv.reader(aprsfile)
    # sets format data[row][column]
    for row in reader:
        data.append(row)

    # liberate all the info that wants to be free
    for i in range (1,len(data)): # starting from 1 excludes column headers
        maxAlt.append(float(data[i][6])) # max altitude
        if data[i][4] != "0":
            ls.append(float(data[i][4])) # landspeed
            flightTime.append(str(data[i][0]))

    # landspeed and altitude
    avgSpeedKph = round(sum(ls)/float(len(ls)),2) # in km/h for 95% of the planet
    avgSpeedMph = round((avgSpeedKph * 0.621371),2) # in mph for the other plebs
    maxSpeedKph = round(max(ls),2)
    maxSpeedMph = round((maxSpeedKph * 0.621371),2)
    maxAltKm = max(maxAlt) # in km because science
    maxAltFt = round((maxAltKm * 3.28084),2) # in ft because engineers QQ

    liftOff = (flightTime[0])
    # figures out timeframe
    touchDown = (flightTime[len(flightTime)-1])
    airTime = (str((int(touchDown[-8:13]))-(int(liftOff[-8:13])))+':'+str((int(touchDown[-5:16]))-(int(liftOff[-5:16])))+':'+str((int(touchDown[-2:]))-(int(liftOff[-2:]))))
    recoveryTime = str(data[i][0]) # when APRS went down, assuming manually switched on recovery... standard practice

# interrogation
print('\nPlease answer the following questions:')
client = raw_input('\nLaunch Client: ')
category = raw_input('\nLaunch Category: ')
status = raw_input('\nLaunch status (success/failure): ')
lremarks = raw_input('\nLaunch remarks: ')
rremarks = raw_input('\nRecovery remarks: ')
atc = raw_input('\nWho notified ATC: ')
sims = raw_input('\nWho ran the simulations: ')
medic = raw_input('\nWho was the Safety Officer: ')
crew = raw_input('\nEnter the names of launch crew. Separate names with a comma: ')
crew = crew.split()
lcrew = raw_input('\nCrew size for launch: ')
rcrew = raw_input('\nCrew size for recovery: ')
gasType = raw_input('\nEnter gas type (e.g. Helium, G4): ')
# numbers interrogation
print('\nPlease answer the following questions with NUMBERS ONLY:')
payloadMassKg = input('\nEnter payload mass (in kg): ')
payloadMassLb = round((payloadMassKg * 2.20462),2) # plebs
balloonMassKg = input('\nEnter balloon mass (in kg): ')
balloonMassLb = round((balloonMassKg * 2.20462),2)
gasVolume = input('\nEnter gas volume (in L): ')
balloonLiftN = input('\nEnter system lift (in N or kg*m/s^2): ')
balloonLiftS = round(balloonLiftN * (0.224809),2) # slug? seriously? (ft/s^2)

# write log file
now = datetime.datetime.now()
prefix = now.strftime("%Y-%m-%d")
fileOut = ('scribble/'+str(prefix)+'-flight-log.md')
commit_message = 'latest flight log'

with open(fileOut, 'w') as text_file:
    text_file.write('---\nlayout: post\ntitle: Flight Summary\n---\n\n') # Jekyll header
    # this is where the magic happens
    text_file.write('## Overview  \n- Client: '+client+'  \n- Category: '+category+'  \n- Status: '+status+'  \n\n- Launch date/time: '+liftOff+'  \n- Recovery date/time: '+recoveryTime+'  \n\n<div class="message">Launch Remarks: '+lremarks+'</div>  \n<div class="message">Recovery Remarks: '+rremarks+'</div>\n\n')
    text_file.write('## Payload Details:  \n- Payload Mass: '+payloadMassKg+' kg ('+payloadMassLb+' lb)')
