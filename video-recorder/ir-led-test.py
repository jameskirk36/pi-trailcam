from signal import pause
import RPi.GPIO as GPIO

try: 
  IR_LED_GPIO=24
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(IR_LED_GPIO, GPIO.OUT)
  GPIO.output(IR_LED_GPIO, GPIO.HIGH)
  pause()
finally: 
  GPIO.cleanup()

