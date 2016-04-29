# ConcertCam

## Setup

* Install rvm
* Install photo2 (e.g., `brew install gphoto2`)
* Make sure the camera is in Manual Focus
* Install Virtual COM Port (VCP) driver from [FTDI](http://www.ftdichip.com/Drivers/VCP.htm). The dmg is also in the `vendor` folder of this repository.

## Run

There are 3 programs:

* `camera_controller.rb`
* `button_listener.rb`
* `Guardfile`

### Camera Controller

Run this first with the following:

* `cd photos/raw`
* `ruby ../../camera_controller.rb`

### Mac OS X program

Run the Mac OS X program and take note of the PID that it outputs in the console.

### Button Listener

Run this after the Mac OS X program. Copy the proc ID that was output by the Mac OS X program and insert it in the command:

* (be in git root)
* `ruby button_listener.rb <pid>`

### Guardfile

First, you'll need to create an album on facebook under the ConcertCam account. Create an album, uploading a dummy photograph that can be deleted later. On the URL of the album, grab the integer that's after the 'set=a.'. That's the album ID.

You'll need to get a long-lived OAuth token from Facebook. To do that, run:

* `rackup`

Add `hidden-peak-7185.herokuapp.com` to the 127.0.0.1 line in `/etc/hosts`

Run a local ssh tunnel: `sudo ssh -L 80:localhost:9292 $(whoami)@localhost`

Then go to (http://hidden-peak-7185.herokuapp.com/index.html)[http://hidden-peak-7185.herokuapp.com/index.html]

With the token from there, run the following:

* `ACCESS_TOKEN=<access_token> ALBUM_ID=<album_id> bundle exec guard`
