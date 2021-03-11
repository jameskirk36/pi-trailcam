# Clear all video links
mkdir ./static/videos/
rm -rf ./static/videos/*

# Create new links to videos on USB drive so web server can see them
ln -s /mnt/usb/videos/*.mp4 ./static/videos/

# Link the uptimelongs into static
ln -s ../../uptime-logger/uptimelogs.txt ./static/

# Run the app
export FLASK_APP=app.py
python3 -m flask run --host=0.0.0.0 --port=8000 &
