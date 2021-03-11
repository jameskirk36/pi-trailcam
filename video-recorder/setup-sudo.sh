apt-get update
apt-get upgrade -y
apt-get install python3-pip udisk2 -y

apt install python-spidev python3-spidev python3-rpi.gpio -y
apt install python-dev python3-dev python-gpiozero python3-gpiozero python3-picamera gpac -y


# Setup USB drive to mount a specific folder
mkdir /mnt/usb
chmod 770 /mnt/usb
blkid

# Setup so pi user can mount and unmount usb drive programmatically
cp polkit/50-udisks.pkla /etc/polkit-1/localauthority/50-local.d/

echo "/dev/sda1 /mnt/usb vfat auto,nofail,noatime,users,rw,uid=pi,gid=pi 0 0" >> /etc/fstab
chown pi /mnt/usb
