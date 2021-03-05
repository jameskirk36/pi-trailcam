#!/bin/sh

# Stop it anyway so we know what state we're starting with
./stop_video_reviewer.sh

# stop the video-recorder service

# turn wifi on
touch wifi

# Start the live stream
export LD_LIBRARY_PATH=mjpg-streamer/mjpg-streamer-experimental/
mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 640 -y 480 -fps 5 -ex night -hf" &

# Run the web-app
cd web-app
./run.sh 
cd ..
