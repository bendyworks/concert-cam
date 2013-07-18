from load_deps import load_deps

load_deps()

import requests

from config import Config

config = Config()
config.load("config.json")


camera_request_uri = config.camera_host + "/snap/" + config.secret_key
print "Posting to: " + camera_request_uri
print "Waiting for input to continue"

while True:
  my_input = raw_input().rstrip()

  if my_input == "pressed":
    response = requests.get(camera_request_uri)
    if re.match("\w+.cr2$", response.text):
      print "Picture taken! " + response.text
      sleep (1)
    else:
      print "Error: " + response.text
