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

### Testing Script

You can use the `take_picture.rb` script to test the project without having to hook up the button and the XBee:

* `ruby take_listener.rb <pid>`

Substituting `<pid>` for either the pid of the gPhoto pid or the Swift pid.

### Guardfile

First, you'll need to create an album on facebook under the ConcertCam account. Create an album, uploading a dummy photograph that can be deleted later. On the URL of the album, grab the integer that's after the 'set=a.'. That's the album ID.

You'll need to get a long-lived OAuth token from Facebook. To do that, run:

* `rackup`

Add `hidden-peak-7185.herokuapp.com` to the 127.0.0.1 line in `/etc/hosts`

Run a local ssh tunnel: `sudo ssh -L 80:localhost:9292 $(whoami)@localhost`

Then go to (http://hidden-peak-7185.herokuapp.com/index.html)[http://hidden-peak-7185.herokuapp.com/index.html]

With the token from there, run the following:

* `ACCESS_TOKEN=<access_token> ALBUM_ID=<album_id> bundle exec guard`

### Long Running Facebook Tokens

A short lived facebook token only lasts about an hour or two, not enough time for most events.  A long lived token will last 60 days and helps you avoid the event headache of having to refresh tokens. This process assumes you've received admin access to the events Facebook page.  (Note: Make sure you recieve full admin and not editor or any of the other permission levels.  Full admin is the only way to go.    

To start you'll have to get a short lived token.  Ask Ryan Corbin, Brad Grzesiak, or Will Strinz for access to the app on Facebook.  Once given access you should be able to view the app on:

https://developers.facebook.com/apps

Once you've achieved that proceed to:

https://developers.facebook.com/tools/explorer

Select the dropdown labeled "Graph API Explorer" and switch it to Concert Cam.  Then select the "Get Token" dropdown and switch it to the page of your choice.  This is the short lived token, save it to a notepad.

Proceed back to the developers app page and open the concert cam app.  Take the App ID and App secret and save those as well.  

Construct a URL by filling in the spots with the respective items:

https://graph.facebook.com/oauth/<SHORT_LIVED_TOKEN>?             
   client_id=<APP_ID>&
   client_secret=<APP_SECRET>&
   grant_type=<fb_exchange_token>&

Plugging this into a browser will give you a page with the token and it's expiration date.  Shed the expiration date section you will have a long lived token.  Plug that in to the guard file command:

* `ACCESS_TOKEN=<access_token> ALBUM_ID=<album_id> bundle exec guard`
