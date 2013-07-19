import time
import re
import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
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

class ImageEventHandler(FileSystemEventHandler):
  def on_moved(self, event):
    super(ImageEventHandler, self).on_moved(event)

    what = 'directory' if event.is_directory else 'file'
    #print("Moved %s: from %s to %s", what, event.src_path,
                     #event.dest_path)

  def on_created(self, event):
    super(ImageEventHandler, self).on_created(event)

    what = 'directory' if event.is_directory else 'file'
    if re.match(".+\.jpg$", event.src_path):
      print("Created %s: %s", what, event.src_path)
      facebooker.put_photo(event.src_path)

  def on_deleted(self, event):
    super(ImageEventHandler, self).on_deleted(event)

    what = 'directory' if event.is_directory else 'file'
    #print("Deleted %s: %s", what, event.src_path)

  def on_modified(self, event):
    super(ImageEventHandler, self).on_modified(event)

    what = 'directory' if event.is_directory else 'file'
    #print("Modified %s: %s", what, event.src_path)

if __name__ == "__main__":
  # TODO: make sure directory exists
  event_handler = ImageEventHandler()
  observer = Observer()
  observer.schedule(event_handler, path=config.image_store_path, recursive=True)
  observer.start()

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()
