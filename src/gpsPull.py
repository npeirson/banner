################################################################################################

## Project Banner: Pulls data from GPS
## Created: 07-14-2016 by Madeline McMillan and Nate Peirson
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

## This holds the functions for pulling data from the GPS

##############################################################################

# ---- Functions ----
#      Time:   timeGet()
#  Latitude:   latGet()
# Longitude:   lonGet()
#  Altitude:   altGet()
# Climb/ROA:   climbGet()


import gps
from smbus import SMBus
import time

# GPS setup
session = gps.gps("localhost", "2947")
##gps.sendCommand(PMTK_SET_NMEA_OUTPUT_OFF)
##gps.sendCommand(PGCMD_NOANTENNA)
##gps.sendCommand(PMTK_SET_NMEA_UPDATE_5HZ)
##gps.sendCommand(PMTK_SET_NMEA_FIZ_5HZ)
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


def timeGet():
	while True:
		try:
			report = session.next()
			if report['class'] == 'TPV':
				if hasattr(report, 'time'):
					time = report.time
					return time
				break
		except:
			pass

def latGet():
	while True:
		try:
			report = session.next()
			if report['class'] == 'TPV':
				if hasattr(report, 'lat'):
					latitude = report.lat
					return latitude
				break
		except:
			pass

def lonGet():
	while True:
		try:
			report = session.next()
			if report['class'] == 'TPV':
				if hasattr(report, 'lon'):
					longitude = report.lon
					return longitude
				break
		except:
			pass

def altGet():
	while True:
		try:
			report = session.next()
			if report['class'] == 'TPV':
				if hasattr(report, 'alt'):
					GPSaltitude = report.alt
					return GPSaltitude
				break

		except:
			pass

def climbGet():
	while True:
		try:
			report = session.next()
			if report['class'] == 'TPV':
				if hasattr(report, 'climb'):
					global climb
					climb = report.climb
					return climb
				break
		except:
			pass
