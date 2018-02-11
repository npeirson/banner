# Project Banner
## Buoyancy Control and Data Acquisition System
Created 2016 by Madeline McMillan and Nate Peirson at Texas A&M University, Department Aerospace Engineering.
Questions? Contact Nate: npeirson@tamu.edu

### Overview
This software was designed to control the components of an experimental payload loitering system, and to simultaneously collect atmospheric data from a variety of sensors. The entire system is initiated by running init.py. Not included in this package are the gamma radiation and lightning strike detection hardware, which run independently on additional threads. Coding by Madeline McMillan and Nate Peirson, with additional contributions from Ramsey Bissex and Michael Bayern. We literally learned Python while writing this system, so it's far from perfect.

### Hardware
Designed to run on a Raspberry Pi 3 running Raspbian Jessie.
Additional custom PCB designed and produced by Michael Bayern (see attached Eagle files).
Sensors:
- GPS: Adafruit Ultimate GPS Breakout (http://adafru.it/746)
    - Setup tutorial: https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/introduction
		- Uses GPSD daemon (see tutorial)
		- Gives date/time, lat/long, rate of ascent, etc
- Thermocouple: Analog Output K-Type Thermocouple Amplifier (http://adafru.it/1778)
		- K-Type Thermocouple (-200 to 1200 Celsius)
		- Converted to digital by TI ADS1015 4 channel ADC (http://adafru.it/1083) (ADS1115 also acceptable, math might need tweaking depending on which you use [in thermocouple.py]).
			- Uses Adafruit_ADS1X15 Library (https://github.com/adafruit/Adafruit_ADS1X15)
			- BE SURE TO GROUND UNUSED CHANNELS ON ADC. NOISE WILL DESTROY YOUR READINGS.
- Pressure/Temperature/Altitude
		- Uses MPL3115A2 (specifically we used SparkFun item SEN-11084)
		- Actually only detects pressure and temperature, but you can extrapolate altitude reasonably well based on a standard atmospheric model. Our code to do this is in ptAltitude.py.

### Libraries
gps (sudo apt-get install python-gps)
gpsd (sudo apt-get install gpsd gpsd-clients)
RPi.GPIO (pip install RPi.GPIO)
SMBus (sudo apt-get install python-smbus)
I2C-Tools (sudo apt-get install i2c-tools)
Adafruit_ADS1x15 (https://github.com/adafruit/Adafruit_ADS1X15)
If I'm forgetting any, you'll surely see what they are when you try to run init.py or any subsystems.

### Radio Transmission
The system is intended to operate in conjunction with a radio data transmission system. This uses a TNC-Pi board and a BaoFeng radio to communicate with a ground-station. You'll need a licensed HAM operator.

### Files and Their Functions
altitudeControl.py	----	The loitering system, including action logging
bannerSettings.py	----	General settings file
gpsPull.py			----	Functions for getting specific data from GPS
init.py				----	Main initalization. Run this to begin everything. Can be made to run on startup via /etc/rc.local or whatever
ledSystem.py		----	Super shitty LED signalling functions. Please improve these with loops... please...
mainLogging.py		----	Logs all sensor data
ptAltitude.py		----	Collects pressure and temperature data from MPL3115A2, then extrapolates altitude based on standard atmospheric model
readme.txt			----	This document
thermocouple.py		----	Collects data from thermocouple via TI ADS1X15 ADC
folder "logs"		----	Includes example log files from both buoyancy control (loiterLog*.txt) and sensors (log*.txt)  
