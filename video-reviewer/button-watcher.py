import RPi.GPIO as GPIO
import time
import subprocess

BUTTON_GPIO=24

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turn_wifi_on():
   subprocess.Popen(["./start_video_reviewer.sh"])
  
def turn_wifi_off():
   subprocess.Popen(["./stop_video_reviewer.sh"])

def button_callback(channel):
   if not GPIO.input(BUTTON_GPIO):
      print("Button pressed!")
      turn_wifi_on()
   else:
      print("Button released!")
      turn_wifi_off()

GPIO.add_event_detect(BUTTON_GPIO,GPIO.BOTH,callback=button_callback, bouncetime=50) 

while True:
  True
