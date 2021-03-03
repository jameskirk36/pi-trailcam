import os
import re
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

def extract_title(video_name):
  # Format "03-03-21_16-13-00.mp4"

  match = re.search(r'^(.*)_(\d{2})-(\d{2})-(\d{2}).mp4', video_name)
  return video_name, f"{match.group(1)} at {match.group(2)}:{match.group(3)}:{match.group(4)}"

def get_list_of_videos():
  path = "/mnt/usb/videos/"
  videos = os.listdir(path)
  vs = map( extract_title, videos )
  return vs

@app.route('/videos')
def videos():
    videos = get_list_of_videos();
    return render_template('videos.html', videos=videos)

