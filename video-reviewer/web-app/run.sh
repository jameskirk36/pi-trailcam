# Clear all video links
mkdir ./static/videos/
rm -rf ./static/videos/*

# Create new links to videos on USB drive so web server can see them, if folder is not empty
if [ "$(ls -A /mnt/usb/videos)" ]; then
  ln -s /mnt/usb/videos/*.mp4 ./static/videos/
fi

# Link the uptimelongs into static
ln -s /home/pi/pi-trailcam/uptime-logger/uptimelog.txt ./static/

# Run the app
python3 app.py &
