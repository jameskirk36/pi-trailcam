#!/bin/sh

# Turn off the wifi
sudo ip link set wlan0 down
rm -rf wifi

# kill the mjpgstreamer process 
pkill mjpg_streamer

# kill the web-app
pkill -f "python3 -m flask run --host=0.0.0.0 --port=8000"

# start the video-recorder app again
systemctl --user start trailcam.service

