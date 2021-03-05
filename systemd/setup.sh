cp trailcam.service  ~/.config/systemd/user/
cp trailcam-buttonwatcher.service  ~/.config/systemd/user/

systemctl --user daemon-reload
systemctl --user enable trailcam.service
systemctl --user start trailcam.service
systemctl --user enable trailcam-buttonwatcher.service
systemctl --user start trailcam-buttonwatcher.service
