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
    camera.capture_photo()
    return "200 OK"
  else:
    return go_away()

if __name__ == "__main__":
  error_msg = camera.detect_gphoto() and camera.setup()

  if len(error_msg) == 0:
    app.debug = True
    app.run()
  else:
    print error_msg
