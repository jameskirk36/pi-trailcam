
import time
import os
import RPi.GPIO as GPIO

STATUS_LED_GPIO=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(STATUS_LED_GPIO, GPIO.OUT)
for x in range(15):
  GPIO.output(STATUS_LED_GPIO, GPIO.LOW)
  time.sleep(1)
  GPIO.output(STATUS_LED_GPIO, GPIO.HIGH)
  time.sleep(1)
 
GPIO.output(STATUS_LED_GPIO, GPIO.LOW)
GPIO.cleanup()
