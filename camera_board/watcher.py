import time
import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

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

if __name__ == "__main__":
  if sys.argv[2]:
    facebooker.put_photo(sys.argv[2])
  else:
    print "No image found!"
