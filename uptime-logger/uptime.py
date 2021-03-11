from io import open
from subprocess import call


uptimelogfile = "/home/pi/pi-trailcam/uptime-logger/uptimelog.txt"
lastuptimefile = "/home/pi/pi-trailcam/uptime-logger/lastuptime.txt"


def read_uptime_log():
  global uptimelogfile

  with open(uptimelogfile, 'r') as f:
    content = f.readlines()

  uptimelog = [x.strip() for x in content]
  return uptimelog

def read_last_uptime():
  global lastuptimefile
  with open(lastuptimefile, 'r') as f:
    last_uptime = f.read().replace("\n", " ")

  return last_uptime

uptime_log = read_uptime_log()
last_uptime = read_last_uptime()

print("Current uptime log entries:")
print(*uptime_log, sep="\n")

uptime_log.insert(0,last_uptime)

new_uptime_log = uptime_log if len(uptime_log) < 10 else uptime_log[:10]

print("New uptime log entries (10):")
print(*new_uptime_log, sep="\n")

#write top 10 lines to a file
with open(uptimelogfile, 'w') as f:
  f.writelines("%s\n" % l for l in new_uptime_log)
