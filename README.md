concert_cam
===========

## Hardware:

## Initial configuration:

1. Update everything: `sudo apt-get update && sudo apt-get upgrade raspi-config raspberrypi* && sudo raspi-config`
1. Select 'Upgrade' in `raspi-config` and then restart after it is complete.
1. Install some other niceties: `sudo apt-get install vim tmux`
1. Name one Raspberry Pi "camera" and the other Pi "button" -- change with ` sudo vim /etc/hostname`
1. Find the name of the wifi dongle: `ifconfig -a` (you want something like `wlan0` or `wlan1`)
1. Edit `/etc/network/interfaces` to look like the following:

```
auto lo

iface lo inet loopback
iface eth0 inet dhcp


auto wlan1
allow-hotplug wlan1
iface wlan1 inet dhcp
        wpa-ssid "YOUR_SSID_HERE"
        wpa-psk "YOUR_PASSWORD_HERE"

iface default inet dhcp
```

1. Restart each Pi: `shutdown -r now`
1. Confirm that your wifi dongle is working by running `sudo wpa_cli` and then something like `ping google.com`
1. Your Pi's should now be on your wifi network.
1. SSH into each Pi
1. Run `ssh-keygen` -- defaults are fine
1. Add your public key to `~/.ssh/authorized_keys`
1. Run `cat .ssh/id_rsa.pub` on each Pi and add the other's public key to `~/.ssh/authorized_keys` so that they can log in to each other without passwords.
