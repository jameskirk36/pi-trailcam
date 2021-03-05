apt-get update
apt-get upgrade -y
apt-get install python3-pip -y

apt install python-spidev python3-spidev python3-rpi.gpio -y
apt install python-dev python3-dev python-gpiozero python3-gpiozero python3-picamera gpac -y


# Setup USB drive to mount a specific folder
mkdir /mnt/usb
chmod 770 /mnt/usb
blkid

echo "/dev/sda1 /mnt/usb vfat auto,nofail,noatime,users,rw,uid=pi,gid=pi 0 0" >> /etc/fstab
