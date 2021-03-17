import os
import re
import netifaces
import RPi.GPIO as GPIO
from flask import Flask, render_template, send_file
from markupsafe import escape
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from signal import pause

# DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
executor = ThreadPoolExecutor(2)


app = Flask(__name__)

videos_path = "./static/videos/"
logs_path = "./static/uptimelog.txt"

@app.route('/')
def homepage():
  server_ip = netifaces.ifaddresses('wlan0')[2][0]['addr']
  return render_template('index.html', server_ip=server_ip)

def Reverse(lst): 
    lst.reverse() 
    return lst 

def extract_title(video_name):
  # Format "2013-03-21_16-13-00.mp4"

  match = re.search(r'^(.*)_(\d{2})-(\d{2})-(\d{2}).mp4', video_name)
  return video_name, f"{match.group(1)} at {match.group(2)}:{match.group(3)}:{match.group(4)}"

def get_list_of_videos():
  global videos_path
  videos = sorted(os.listdir(videos_path))
  vs = list(map( extract_title, Reverse(videos) ))
  return vs

def get_uptimelogs():
  global logs_path
  with open(logs_path, 'r') as f:
    content = f.readlines()

  uptimelogs = [x.strip() for x in content]
  return uptimelogs

@app.route('/videos')
def videos():
    videos = get_list_of_videos()
    return render_template('videos.html', videos=videos)

@app.route('/uptimelogs')
def uptimelogs():
    uptimelogs = get_uptimelogs()
    return render_template('uptimelogs.html', uptimelogs=uptimelogs)

@app.route('/videos/<id>')
def download_video (id):
    global videos_path
    video_path = videos_path + "/" + id
    return send_file(video_path, as_attachment=True)


def turn_on_ir_leds():
  IR_LED_GPIO=24

  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(IR_LED_GPIO, GPIO.OUT)
  GPIO.output(IR_LED_GPIO, GPIO.HIGH)
  print("Setting IR LED to HIGH")
  pause()

if __name__ == '__main__':
  executor.submit(turn_on_ir_leds)
  app.run(host="0.0.0.0", port="8000")
  
