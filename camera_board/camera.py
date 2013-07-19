from time import strftime
from sh import shell
import re

class Camera:
  model = ""
  usb_location = ""
  config = {}

  def detect_gphoto(self):
    out, err = shell(['which', 'gphoto2'])
    if not out and err:
      raise Exception("gphoto2 not found!")
      # or raise Exception(err)

  def setup(self, config):
    self.config = config

    autodetected = shell(['gphoto2', '--auto-detect'])[0].split('\n')
    camera_string = filter(None, autodetected)[-1].rstrip()

    if re.match("-+$", camera_string):
      raise Exception("Camera cannot be found!")
    else:
      self.model, self.usb_location = self.parse_camera_string(camera_string)

  def parse_camera_string(self, camera_string):
    camera_parts = camera_string.split()
    usb_location = camera_parts[-1]
    model_parts = camera_parts[0:(len(camera_parts)-1)]
    model = " ".join(model_parts)

    return (model, usb_location)

  def print_camera_info(self):
    print "Camera: " + self.model
    print "USB Location: " + self.usb_location

  def capture_photo(self):
    base_filename, full_filename = self.generate_filename()
    print full_filename

    cmd = ('gphoto2 --camera="%s" --capture-image-and-download '
           '--filename=%s') % (self.model, full_filename)
    print "Running: %s" % cmd
    output = shell(cmd)
    print output

    return base_filename

  def generate_filename(self):
    filetype = self.config.default_filetype
    path = self.config.image_store_path
    date = strftime("%Y-%m-%d-%H:%M:%S")
    base_filename = "image_%s.%s" % (date, filetype)
    full_filename = path + base_filename
    return (base_filename, full_filename)
