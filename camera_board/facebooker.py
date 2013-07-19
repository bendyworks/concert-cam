import facebook
import json

from config import Config
config = Config()
config.load("config.json")

class Facebooker():
  album_id = 0
  def setup_oauth(self):
    global graph

    self.set_album_id()
    return self.set_token()

  def put_photo(self, filename):
    tags = json.dumps([])
    self.graph.put_photo(open(filename), 'Look at this cool photo!', self.album_id, tags=tags)

  def set_token(self):
    if config.fb_oauth_access_token:
      self.graph = facebook.GraphAPI(config.fb_oauth_access_token)
      return True
    else:
      return False

  def set_album_id(self):
    if config.album_id != "":
      self.album_id = config.album_id
    else:
      self.album_id = None
