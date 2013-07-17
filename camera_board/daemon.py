import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

from camera import Camera
from config import Config
from flask import Flask

app = Flask(__name__)

config = Config()
config.load("config.json")

camera = Camera()

def go_away():
  return "Go away!"

@app.route("/")
def index():
  return go_away()

@app.route("/snap/")
def snap_index():
  return go_away()

@app.route("/snap/<password>")
def snap(password):
  if password == config.secret_key:
    new_filename = camera.capture_photo()
    return new_filename
  else:
    return go_away()

if __name__ == "__main__":
  camera.detect_gphoto()
  camera.setup()

  # Camera found, so print some info about it:
  camera.print_camera_info()

  flask_debug = os.environ.get('FLASK_DEBUG') or False
  if flask_debug:
    app.debug = True

  app.run(host='0.0.0.0')
