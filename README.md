# Raspberry PI trail camera

Source code for a raspberry pi-based, motion activated, night vision trail camera for watching wildlife.  

## How it works
Motion is detected using the passive infrared sensor (PIR).  A python script is running all the time at startup and watching the values of the GPIO pins connected to the PIR.  
When a movement signal is detected, the camera is momentarily turned on, along with the infra red LED lamps, and a H264 MP4 video is recorded.  Videos are saved to a USB drive, for easy removal and download.


## Principles
Some key principles:
* Cheap to buy and build
* Low power consumption


## Video recorder
This is based on the incredibly useful article from the [Peak Nature blog](https://peaknature.co.uk/blog/how-to-build-a-raspberry-pi-zero-trail-camera--part-1-what-you-need).  All the credit for the source code and setup here goes to Chris from Peak Nature, i've just changed the GPIO pins that the PIR sensor is connected to


## Video reviewer application
This is a web app that serves a live feed of the camera to aid with positioning it.  There is also a page to view the recorded videos via a web browser. 
* For the camera streaming to HTML it uses the [mjpg-streamer](https://github.com/jacksonliam/mjpg-streamer)
* The web application is a small Python Flask app
