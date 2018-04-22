#!/bin/bash
# I don't think this works currently

if [ "$(id -u)" != "0" ]; then
	echo "This probaby will not work without sudo"
	exit
fi

apt-get install python-gps
apt-get install gpsd gpsd-clients
pip install RPi.GPIO
apt-get install python-smbus
apt-get install i2c-tools
#Adafruit_ADS1x15 (https://github.com/adafruit/Adafruit_ADS1X15)
#it-hook='import sys; sys.path.append("/path/to/root")'
