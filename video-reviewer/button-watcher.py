import RPi.GPIO as GPIO
import time
import subprocess
from signal import pause

BUTTON_GPIO=15
LED_GPIO=27

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_GPIO, GPIO.OUT)
GPIO.output(LED_GPIO, GPIO.LOW)

def turn_reviewer_on():
   subprocess.Popen(["./start_video_reviewer.sh"])
  
def turn_reviewer_off():
   subprocess.Popen(["./stop_video_reviewer.sh"])

reviewer_running=False

def button_callback(channel):
   global reviewer_running
   print("Button pressed!")

   if reviewer_running is False:
      print("Turning reviewer on")
      turn_reviewer_on()
      reviewer_running=True
      GPIO.output(LED_GPIO, GPIO.HIGH)
   else:
      print("Turning reviewer off")
      turn_reviewer_off()
      reviewer_running=False
      GPIO.output(LED_GPIO, GPIO.LOW)

GPIO.add_event_detect(BUTTON_GPIO,GPIO.RISING,callback=button_callback, bouncetime=1000) 

pause()
