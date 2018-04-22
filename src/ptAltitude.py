##############################################################################

## Project Banner: Sensor Data Logging
## Created: 07-09-2016 by Madeline McMillan
## Texas A&M University, Department of Aerospace Engineering
## High Altitude Balloon Club

## Collects P & T data from MPL3115A2 sensor and extrapolates altitude
## based on standard atmospheric model.

##############################################################################

from smbus import SMBus
import time

def ptAlt():
	# Special Chars
	deg = u'\N{DEGREE SIGN}'

	# I2C Constants
	ADDR = 0x60
	CTRL_REG1 = 0x26
	PT_DATA_CFG = 0x13
	bus = SMBus(1)

	who_am_i = bus.read_byte_data(ADDR, 0x0C)
	#print hex(who_am_i)
	if who_am_i != 0xc4:
		print "PTA device not active!" # terminal feedback
		exit(1)

	# Set oversample rate to 128
	setting = bus.read_byte_data(ADDR, CTRL_REG1)
	newSetting = setting | 0x38
	bus.write_byte_data(ADDR, CTRL_REG1, newSetting)

	# Enable event flags
	bus.write_byte_data(ADDR, PT_DATA_CFG, 0x07)

	# Toggle One Shot
	setting = bus.read_byte_data(ADDR, CTRL_REG1)
	if (setting & 0x02) == 0:
		bus.write_byte_data(ADDR, CTRL_REG1, (setting | 0x02))

	# Read sensor data
	#print "Waiting for data..."
	status = bus.read_byte_data(ADDR,0x00)
	while (status & 0x08) == 0:
		#print bin(status)
		status = bus.read_byte_data(ADDR,0x00)
		time.sleep(0.5)

	#print "Reading PTA data..."
	p_data = bus.read_i2c_block_data(ADDR,0x01,3)
	t_data = bus.read_i2c_block_data(ADDR,0x04,2)
	status = bus.read_byte_data(ADDR,0x00)
	#print "status: "+bin(status)

	p_msb = p_data[0]
	p_csb = p_data[1]
	p_lsb = p_data[2]
	t_msb = t_data[0]
	t_lsb = t_data[1]

	pressure = (p_msb << 10) | (p_csb << 2) | (p_lsb >> 6)
	p_decimal = ((p_lsb & 0x30) >> 4)/4.0

	# unit convrsion
	celsius = t_msb + (t_lsb >> 4)/16.0
	fahrenheit = (celsius * 9)/5 + 32
	altitude = '[Out of range]'

	# altitude extrapolation
	if celsius < 15 and celsius >= -55.5:
		if pressure > 12000:
			altitude = (15.04 - celsius) / .00649
		elif pressure < 12000:
			altitude = (celsius + 131.21)/(.00299)
		elif celsius < -55.5:
			altitude = (1.73 - math.log(pressure/22.65))/.000157

	#print "Pressure and Temperature at "+time.strftime('%m/%d/%Y %H:%M:%S%z')
##    print str(pressure+p_decimal)+" Pa"
##    print str(celsius)+deg+"C"
##    print str(fahrenheit)+deg+"F"
##    print str(altitude)+" meters"
	return (pressure, celsius, altitude)
