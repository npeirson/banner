################################################################################################

## Project Banner: Settings
## Created: 10/21/16 by Madeline McMillan and Nate Peirson
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

################################################################################################

# Depending on the application, not all of these will be necessary
# Pin number on the RPi pinout diagram is different from the GPIO port number

def balloonPin():
    value = 11 # pin 11, gpio 17
    return value

def ballastPin():
    value = 12 # pin 12, gpio 18
    return value

def loiterAlt():
    value = 15000 # 15,000 m = 49,212.6 ft
    return value

def killAlt():
    value = 3048 # 3,048 m = 10,000 ft
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
	return value

def cookTime():
	value = 16 # coil on for 3 seconds, recommend overshooting this a little since waiting until fall detected is more ideal
	return value

def timeout(): # kill flight after this many seconds
    value = 1500  # 1500 seconds = 25 minutes
    return value
