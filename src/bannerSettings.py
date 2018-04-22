##############################################################################

## Project Banner: Settings
## Created: 10/21/16 by Madeline McMillan and Nate Peirson
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

##############################################################################

# Pin number on the RPi pinout diagram is different from the GPIO port number

def balloonPin():
	value = 18 # pin 18, gpio 24
	return value

def ballastPin():
	value = 12 # pin 12, gpio 18
	return value

def loiterAlt():
	value = 12192 # 12,192 m = 40,000 ft
	return value

def loiterTime():
	value = 600 # Loiter time before flight termination (seconds)
	return value

def deltaA():
	value = 6 # threshold of change in acceleration indicating balloon severance
	return value

def gpsLedPin():
	value = 22 # GPIO pin for LED to indicate GPS status
	return value

def tempSensorLedPin():
	value = 23 # GPIO pin for LED to indicate thermocouple value in range
	return value

def logFreq():
	value = 5 # time between taking data points (seconds)
