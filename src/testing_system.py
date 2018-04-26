import time
import RPi.GPIO as GPIO

GPIO.setup(bannerSettings.balloonLiftPin(), GPIO.OUT)
GPIO.setup(bannerSettings.balloonEqPin(), GPIO.OUT)
GPIO.setup(bannerSettings.ballastPin(), GPIO.OUT)


print 'System running'

print 'cutting 1st balloon'
time.sleep(15)
GPIO.output(11, GPIO.HIGH) # Cut Lift Balloon
time.sleep(8)
GPIO.output(11, GPIO.LOW)
time.sleep(8)

print 'ballast time'
GPIO.output(7, GPIO.HIGH) # Ballast system
time.sleep(3)
GPIO.output(7, GPIO.LOW)
time.sleep(10)

print 'cutting 2nd balloon'
GPIO.output(15, GPIO.HIGH) # 2nd Balloon system
time.sleep(8)
GPIO.output(15, GPIO.LOW)
time.sleep(10)

print 'Done!'
