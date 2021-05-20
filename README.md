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
This is based on the incredibly useful article from the [Peak Nature blog](https://peaknature.co.uk/blog/how-to-build-a-raspberry-pi-zero-trail-camera--part-1-what-you-need).  All the credit for the source code and setup here goes to Chris from Peak Nature, i've just changed the GPIO pins that the PIR sensor is connected to.




## Video reviewer application
This is a web app that serves a live feed of the camera to aid with positioning it.  There is also a page to view the recorded videos via a web browser. 
* For the camera streaming to HTML it uses the [mjpg-streamer](https://github.com/jacksonliam/mjpg-streamer)
* The web application is a small Python Flask app


## Setup - software

### Prerequisites
* Raspberry pi os flashed to an SD card (tested with RP OS lite March 2021 ish)
* SSH enabled or a usb keyboard and screen connected for typing commands
* Raspberry pi os user is expected to be 'pi'
* This repository is cloned or downloaded to the top level home directory (for example /home/pi/$REPO)
* The [mjpg-streamer](https://github.com/jacksonliam/mjpg-streamer) repository is downloaded to the same top level home directory, so that its available at /home/pi/mjpg-streamer.  Follow the instructions in mjpg streamer repo on how to build the binary needed for the video-reviewer.

### First setup the config files and systemd services:

All commands are relative to the root of this repository

```
sudo cp rc.local /etc/rc.local
cd systemd/ 
./setup.sh
cd ..
sudo cp boot/config.txt /boot/config.txt
```

### Now setup the video recorder app
```
cd video-recorder
sudo ./setup-sudo.sh
./setup-python.sh
```

### Now setup the uptime logger cronjob

You've have to manually follow the steps listed in [uptime-logger](uptime-logger/setup.sh)


## Setup - Hardware

The hardware circuit diagram can be seen in [here](circuit-diagrams/raspberry-pi.fzz).  This can be opened with [Fritzing](https://fritzing.org/)


## User guide
You can see the user guide for how to use this trailcam on this [google docs page](https://docs.google.com/document/d/e/2PACX-1vT-njGph48FSP8ZsxmGHlgkGGrzZTYDqbi_WKcix7ZmfOUW3iR0yc2oDXi7muFYu6zVj8Gw3Hcc5ptP/pub)
