import time
import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

import pyinotify
from facebooker import Facebooker

from config import Config
config = Config()
config.load("config.json")

facebooker = Facebooker()
facebooker.set_config(config)

if facebooker.setup_oauth():
  print "Facebook OAuth loaded"
else:
  raise("Facebook OAuth could not be loaded!")

class ImageEventHandler(pyinotify.ProcessEvent):
  def my_init(self, cwd, extension, cmd):
    self.cwd = cwd
    self.extensions = extension.split(',')
    self.cmd = cmd

  def _run_cmd(self, event):
    print '==> new photo detected'
    print event
    print event.pathname
    #facebooker.put_photo(event.

  def process_IN_CREATE(self, event):
    if all(not event.pathname.endswith(ext) for ext in self.extensions):
      return
    self._run_cmd(event)

if __name__ == "__main__":
  extension = config.default_filetype

  wm = pyinotify.WatchManager()
  handler = ImageEventHandler(cwd=path, extension=extension, cmd=cmd)
  notifier = pyinotify.Notifier(wm, default_proc_fun=handler)
  wm.add_watch(path, pyinotify.ALL_EVENTS, rec=True, auto_add=True)
  print '==> Start monitoring %s (type c^c to exit)' % path
  notifier.loop()
