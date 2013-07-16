import datetime
import os
import re

class Camera:
  model = ""
  usb_location = ""
  def detect_gphoto(self):
    location = os.popen('which gphoto2').read().rstrip()
    if location != "":
      return True
    else:
      return "Error: gphoto2 not found!"

  def setup(self):
    autodetected = os.popen('gphoto2 --auto-detect').read().split('\n')
    camera_string = filter(None, autodetected)[-1].rstrip()

    if not re.match("{-}+", camera_string):
      model, usb_location = self.parse_camera_string(camera_string)

      return "Camera is: " + model + "\n" + "Location is: " + usb_location
    else:
      return "Error: Camera cannot be found!"

  def parse_camera_string(self, camera_string):
    camera_parts = camera_string.split()
    usb_location = camera_parts[-1]
    model_parts = camera_parts[0:(len(camera_parts)-1)]
    model = " ".join(model_parts)

    return (model, usb_location)

  def capture_photo(self):
    datetime = str(datetime.datetime.now())
    filename = "image_" + datetime + ".cr2"

    cmd = "gphoto2 --camera \"" + self.model + "\" --capture-image-and-download --filename=" + filename
    os.popen(cmd)

    return filename

