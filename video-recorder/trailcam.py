# Full credit goes to Chris at Peak nature blog for this code https://peaknature.co.uk/blog/how-to-build-a-raspberry-pi-zero-trail-camera--part-1-what-you-need

from gpiozero import MotionSensor
import logging
from datetime import datetime
from subprocess import call
import picamera
import time
import os
import RPi.GPIO as GPIO

IR_LED_GPIO=24
PIR_GPIO=14

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_LED_GPIO, GPIO.OUT)
GPIO.output(IR_LED_GPIO, GPIO.LOW)

if not os.path.exists('trailcam_log/'):
    os.makedirs('trailcam_log/')

if not os.path.exists('videos/'):
    os.makedirs('videos/')

if not os.path.exists('/mnt/usb/videos'):
    os.makedirs('/mnt/usb/videos')

logfile = "trailcam_log/trailcam_log-"+str(datetime.now().strftime("%Y%m%d-%H%M"))+".csv"
logging.basicConfig(filename=logfile, level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d, %H:%M:%S,')


def remount_usb_drive():
  # unmount usb drive
  call("udisksctl unmount -b /dev/sda1", shell=True)

  # mount usb drive again
  call("udisksctl mount -b /dev/sda1", shell=True)

pir = MotionSensor(PIR_GPIO)
duration = 20

print('Starting')
logging.info('Starting')

# Wait an initial duration to allow PIR to settle
print('Waiting for sensor to settle')
time.sleep(10)
print('Ready')

while True:
    pir.wait_for_motion()
    logging.info('Motion detected')
    print('Motion detected')
    while pir.motion_detected:
        GPIO.output(IR_LED_GPIO, GPIO.HIGH)
        print('Beginning capture')
        ts = '{:%Y%m%d-%H%M%S}'.format(datetime.now())
        logging.info('Beginning capture: '+ str(ts)+'.h264')
        with picamera.PiCamera() as cam:
            cam.resolution=(1024,768)
            cam.annotate_background = picamera.Color('black')

            cam.start_recording('video.h264')
            start = datetime.now()
            while (datetime.now() - start).seconds < duration:
                cam.annotate_text = datetime.now().strftime('%d-%m-%y %H:%M:%S')
                cam.wait_recording(0.2)
            cam.stop_recording()
        time.sleep(1)
        print('Stopped recording')
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        input_video = "video.h264"

        logging.info('Attempting to save video')
        print('Attempting to save video')

        usb = call("mountpoint -q /mnt/usb", shell=True)

        if usb == 0:
            logging.info('Saving to /mnt/usb/videos/')
            print('Saving to /mnt/usb/videos/')
            output_video = "/mnt/usb/videos/{}.mp4".format(timestamp)
        else:
            logging.info('Saving to videos/')
            print('Saving to videos/')
            output_video = "videos/{}.mp4".format(timestamp)

        call(["MP4Box", "-add", input_video, output_video])
        print('Motion ended - sleeping for 10 secs')
        logging.info('Motion Ended')
        GPIO.output(IR_LED_GPIO, GPIO.LOW)
        remount_usb_drive()
        time.sleep(10)
