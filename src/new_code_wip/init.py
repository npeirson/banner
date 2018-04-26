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
import loiter_settings  #TODO loiter_settings.py. Madeline (need to change GPIO pin #)


#TODO: ----------------------------------------------
read_settings()

init_gps_data() # Ensure we are getting GPS data
init_alt_data() # Ensure we getting Altitude/Pressure/Temperature data
init_led_system() # LED setup (if necessary)
init_coil_burner_system() # Coil-burner setup (if necessary)
init_log_system() # Logging-system setup (if necessary)

<<<<<<< HEAD
# Start launch clock:
launch_start = time.time()

def should_kill():
	#TODO: in_geofence() in gps_control.py, get_altitude() in alt_control.py
	if in_geofence() == False or get_altitude() > height_limit() or (time.time()-launch_start) > max_flight_time():#TODO more conditions
=======
HEIGHT_LIMIT = 9999999
TARGET_ALTITUDE = 99999

def should_kill():
	#TODO: in_geofence() in gps_control.py, get_altitude() in alt_control.py
	if in_geofence() == False or get_altitude() > HEIGHT_LIMIT:#TODO more conditions (time limit)
>>>>>>> caffb98264417612f222b7b124645a1b66917598
		return True
	else:
		return False

<<<<<<< HEAD
def kill(): # Changed by Madeline
    # If both balloons attached... (Something like IF BALLOON_1 == NOT RELEASED)
    # Release lifting balloon:
    GPIO.output(loiter_settings.coil_burner_1(), GPIO.HIGH) # turns coil burner 1 on
    time.sleep(loiter_settings.burn_time()) # leaves burner 1 on for specified amount of time
    GPIO.output(loiter_settings.coil_burner_1(), GPIO.LOW) # turns coil burner 1 off
    # Release neutral balloon:
    GPIO.output(loiter_settings.coil_burner_2(), GPIO.HIGH) # turns coil burner 2 on
    time.sleep(loiter_settings.burn_time()) # leaves burner 2 on for specified amount of time
    GPIO.output(loiter_settings.coil_burner_2(), GPIO.LOW) # turns coil burner 2 off
    # If only neutral balloon still attached... (Something like IF BALLOON_2 == NOT RELEASED)
    GPIO.output(loiter_settings.coil_burner_2(), GPIO.HIGH) # turns coil burner 2 on
    time.sleep(loiter_settings.burn_time()) # leaves burner 2 on for specified amount of time
    GPIO.output(loiter_settings.coil_burner_2(), GPIO.LOW) # turns coil burner 2 off
=======
def kill():
	pass #TODO: signal burn appropriate coil(s)
	#TODO: burning coil, takes 6 seconds per coil

>>>>>>> caffb98264417612f222b7b124645a1b66917598

while True:
	if get_altitude() >= TARGET_ALTITUDE:
		begin_altitude_control()#TODO:
	if should_kill():
		kill()
<<<<<<< HEAD
    if reached_target():
        
	if has_landed():#TODO: define in altitudeControl.py
=======
	if has_landed():#TODO: define in alt_control.py
>>>>>>> caffb98264417612f222b7b124645a1b66917598
		recovery_beacon() #TODO: define in led_control.py
	if is_in_freefall(): #TODO: define in alt_control.py
		release_parachute() #TODO: signal appropriate release system
	thread.sleep(1)
