#!/usr/bin/env python
import sys
import subprocess
import ASUS.GPIO as GPIO                           #Import GPIO library
import time                                       #Import time library
GPIO.setmode(GPIO.BOARD)                          #Set GPIO pin numbering
pir = 40                                          #Associate pin 26 to pir
GPIO.setup(pir, GPIO.IN)                          #Set pin as GPIO in 
SHUTOFF_DELAY = 60
turned_off = 1
print "Waiting for sensor to settle"
time.sleep(2)                                     #Waiting 2 seconds for the sensor to initiate
print "Detecting motion"
try:
    while True:
        if GPIO.input(pir):                            #Check whether pir is HIGH
            print "Motion Detected!"
            last_motion_time = time.time()
            time.sleep(2)                               #D1- Delay to avoid multiple detection
            if turned_off:
                subprocess.call("sh /root/pir/monitor_on.sh", shell=True)
                subprocess.call("sh /root/pir/pic_on.sh", shell=True)
                print "turned ON"
                turned_off = 0
            time.sleep(0.1)                                 #While loop delay should be less than detection(hardware) delay
        else:
            if not turned_off and time.time() > (last_motion_time + SHUTOFF_DELAY): 
                subprocess.call("sh /root/pir/monitor_off.sh", shell=True)
                subprocess.call("sh /root/pir/pic_off.sh", shell=True)
                turned_off = 1
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup(40)

