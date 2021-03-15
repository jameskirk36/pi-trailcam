
import time
import os
import RPi.GPIO as GPIO
from signal import pause

STATUS_LED_GPIO=27
PIR_GPIO=14

try: 
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(STATUS_LED_GPIO, GPIO.OUT)
  GPIO.setup(PIR_GPIO, GPIO.IN)

  def callback(channel):
    GPIO.output(STATUS_LED_GPIO, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(STATUS_LED_GPIO, GPIO.LOW)

  GPIO.add_event_detect(PIR_GPIO,GPIO.RISING,callback=callback, bouncetime=10) 
  pause()
finally:
  GPIO.cleanup()
