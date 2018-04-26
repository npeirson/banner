"""
############################################################################

## High Altitude Balloon Club

############################################################################
"""
#pylint: disable=no-member

import alt_control		#TODO alt_control.py
import log_control		#TODO log_control.py
import gps_control		#TODO gps_control.py
import led_control		#TODO led_control.py
import thermo_control	#TODO thermo_control.py


#TODO: ----------------------------------------------
read_settings()

init_gps_data() # Ensure we are getting GPS data
init_alt_data() # Ensure we getting Altitude/Pressure/Temperature data
init_led_system() # LED setup (if necessary)
init_coil_burner_system() # Coil-burner setup (if necessary)
init_log_system() # Logging-system setup (if necessary)

HEIGHT_LIMIT = 9999999
TARGET_ALTITUDE = 99999

def should_kill():
	#TODO: in_geofence() in gps_control.py, get_altitude() in alt_control.py
	if in_geofence() == False or get_altitude() > HEIGHT_LIMIT:#TODO more conditions (time limit)
		return True
	else:
		return False

def kill():
	pass #TODO: signal burn appropriate coil(s)
	#TODO: burning coil, takes 6 seconds per coil


while True:
	if get_altitude() >= TARGET_ALTITUDE:
		begin_altitude_control()#TODO:
	if should_kill():
		kill()
	if has_landed():#TODO: define in alt_control.py
		recovery_beacon() #TODO: define in led_control.py
	if is_in_freefall(): #TODO: define in alt_control.py
		release_parachute() #TODO: signal appropriate release system
	thread.sleep(1)
