concert_cam
===========

## Hardware:

Format: \[quantity\]x \[what\] (\[purchased from\])

### Camera system:

* 1x 512mb Raspberry Pi board (Adafruit)
* 1x USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply (Adafruit)
* 1x USB WiFi (802.11b/g/n) Module: For Raspberry Pi and more (Adafruit)
* 1x Adafruit Pi Case- Enclosure for Raspberry Pi Model A or B (Adafruit)
* 1x USB cable - A/MicroB (Adafruit)
* 1x 5V 1A (1000mA) USB port power supply - UL Listed
* 1x RCA (Composite Video, Audio) Cable 6 feet (Adafruit)
* 1x NTSC/PAL (Television) TFT Display - 4.3" Diagonal (Adafruit)
* 1x 12 VDC 1000mA regulated switching power adapter - UL listed (Adafruit) -- this is for the TFT display
* 1x USB Battery Pack for Raspberry Pi - 3300mAh - 5V @ 1A and 500mA (Adafruit)
* 1x Canon 6D camera w/ 24-105mm kit lens (Amazon)

### Button system:

* 1x 512mb Raspberry Pi board (Adafruit)
* 1x USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply (Adafruit)
* 1x USB WiFi (802.11b/g/n) Module: For Raspberry Pi and more (Adafruit)
* 1x Adafruit Pi Case- Enclosure for Raspberry Pi Model A or B (Adafruit)
* 2x USB cable - A/MicroB (Adafruit)
* 1x 5V 1A (1000mA) USB port power supply - UL Listed
* 1x USB Battery Pack for Raspberry Pi - 3300mAh - 5V @ 1A and 500mA (Adafruit)
* 1x Massive Arcade Button with LED - 100mm Green (Adafruit)
* 1x Teensy (ATmega32u4 USB dev board) 2.0 (Adafruit)
* 1x Cat5 Ethernet cable (choose your own length, various vendors)

## Initial configuration:

1. In `raspi-config`, expand the filesystem, reset the password, turn on SSH, turn off X at boot, and make sure that the RAM split gives the most RAM to the ARM. Save & exit `raspi-config`
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
    (be sure to change `wlan1` to whatever your USB wifi dongle is called!)
1. Restart each Pi: `shutdown -r now`
1. Confirm that your wifi dongle is working by running `sudo wpa_cli` and then something like `ping google.com`
1. Your Pi's should now be on your wifi network.
1. SSH into each Pi (`ssh pi@camera.local` and `ssh pi@button.local`)
1. Run `ssh-keygen` -- defaults are fine
1. Add your public key to `~/.ssh/authorized_keys`
1. Run `cat .ssh/id_rsa.pub` on each Pi and add the other's public key to `~/.ssh/authorized_keys` so that they can log in to each other without passwords.

## Testing the camera

1. On the Camera Pi, install gphoto2: `sudo apt-get install gphoto2`
1. Plug in your DSLR with the USB cable provided with the camera.
1. Turn on the camera.
1. Run `gphoto2 --capture-image` (this will take some time because gphoto2 must scan for the camera and then trigger a picture. The photo remains on the camera unless we ask for the file.)
1. You should hear the camera shutter click and the commandline will notify you of the new image created.

## Assembling the button:

1. Wire the Teensy to the button (refer to [this post by Raster](http://rasterweb.net/raster/2011/05/09/the-button/))
1. Flash the Teensy with the code from Raster's blog post with the Arduino IDE + [Teensyduino](http://www.pjrc.com/teensy/teensyduino.html) addon. (Be sure to change the pin number if your button is connected to another IO pin!)
1. Connect the Teensy to the Button Pi's USB hub.
1. Open up vim or another text editor (make sure you're in insert mode)
1. Pressing the button should insert a space into the document.
1. The button is all set!
