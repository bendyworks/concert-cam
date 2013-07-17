from time import strftime
from sh import shell
import re


class Camera:
  model = ""
  usb_location = ""

  def detect_gphoto(self):
    out, err = shell(['which', 'gphoto2'])
    if not out and err:
      raise Exception("gphoto2 not found!")
      # or raise Exception(err)

  def setup(self):
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
    filename = self.generate_filename()
    print filename

    cmd = ('gphoto2 --camera="%s" --capture-image-and-download '
           '--filename="%s"') % (self.model, filename)
    print cmd
    shell(cmd)

    return filename

  def generate_filename(self):
    date = strftime("%Y-%m-%d-%H:%M:%S")
    filename = "../image_%s.cr2" % date
    return filename
