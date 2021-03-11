import os
import re
from markupsafe import escape

videos_path = "./static/videos/"


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
  print(*vs, sep="\n")
  return vs

videos = get_list_of_videos();


