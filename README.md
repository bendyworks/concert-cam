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

## Flashing the SD cards:

1. Download [Occidentalis](http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2)
1. Extract the disk image from the zip file.
1. Use [PiFiller](http://ivanx.com/raspberrypi/) on Mac OSX to flash your SD cards.
1. Insert SD cards into Raspberry Pis and confirm that they boot to a Linux prompt. User will be `pi` and password will be `raspberry` by default.

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
1. Run `gphoto2 --auto-detect` and note the Model name.
1. Run `gphoto2 --capture-image-and-download --camera "USB PTP Class Camera"` where `--camera` gets the string of your camera model
1. You should hear the camera shutter click and the commandline will notify you of the new image created. It should be a RAW file; if not, change your camera settings.

## Assembling the button:

1. Wire the Teensy to the button (refer to [this post by Raster](http://rasterweb.net/raster/2011/05/09/the-button/))
    * Attach one pin of the button to a GND (ground) pin and another pin from
    the button to IO line 10.
    * Attach the wires from the LED to the +5V and another GND pin on the
      Teensy.
1. Install the Arduino IDE and [Teensyduino](http://www.pjrc.com/teensy/teensyduino.html) -- follow the Teensyduino instructions!
1. Flash the Teensy with the code from this repo's `teensy_firmware/button`
   directory.
1. Connect the Teensy to the Button Pi's USB hub.
1. Open up vim or another text editor (make sure you're in insert mode!)
1. Pressing the button should insert the string "pressed" into the file.
1. The button is all set!

## Set up the button's software:

1. Clone this repo onto the button Pi.
1. Run `pip install -r requirements.txt` in the `concert_cam` directory.

## Getting the button Pi to login automatically:

We want the button Pi to login automatically and run our python script to
receive events from the button. To do this, we only need to do a few things:

1. `sudo vim /etc/inittab`

   Change the following line:

   ```
   1:2345:respawn:/sbin/getty --noclear 38400 tty1
   ```

   to this:

   ```
   1:2345:respawn:/bin/login -f pi tty1
   ```

   This will cause the Raspberry Pi to automatically log in as the `pi` user
   on boot on the first terminal. (`tty1`)
1. `sudo vim /etc/profile`

    Go to the bottom and insert:

    ```bash
    if [ -z "$TMUX" ]; then
      (tmux attach -t button || tmux new -s button 'python /home/pi/dev/concert_cam/button_board/listener.py')
    fi
    ```

    This will cause the shell to drop into a tmux session, if it isn't already
    inside a tmux session. And it runs our button listener script by default!
1. Reboot the button board Raspberry Pi
1. It should boot right into tmux and display the `Waiting for input to
   continue` message

## Assembling the camera board:

1. Attach the 4.3" TFT panel to the Camera Raspberry Pi's composite video connector.
1. Boot the Raspberry Pi. You should see the Pi boot up on the tiny screen.
1. Log in (probably through SSH)
1. Run `sudo dpkg-reconfigure console-setup`
1. Choose UTF-8, "Guess optimal", and then you'll be at the fonts screen.
1. This is really up to you, but we used TerminusBold at 12x24 resolution.
1. Save the settings; the display should now have a larger font.
1. Run `sudo raspi-config` and go to Advanced -> Overscan. Enable overscan.
1. Reboot the Pi.

## Set up the camera board's software:

1. Clone this repo onto the camera board Pi.
1. Run `pip install -r requirements.txt` in the `concert_cam` directory.
