from load_deps import load_deps

load_deps()

import re
import requests

from config import Config

config = Config()
config.load("config.json")

def make_request(camera_request_uri):
  try:
    response = requests.get(camera_request_uri)
    text = response.text
  except requests.exceptions.ConnectionError:
    text = "Error, cannot load: " + camera_request_uri

  return text


camera_request_uri = "http://" + config.camera_host + ":5000/snap/" + config.secret_key
print "Posting to: " + camera_request_uri
print "Waiting for input to continue"

while True:
  my_input = raw_input().rstrip()

  if my_input == "pressed":
    response = make_request(camera_request_uri)
    if re.match("\w+.cr2$", response):
      print "Picture taken! Filename: " + response
    else:
      print "Error: " + response
