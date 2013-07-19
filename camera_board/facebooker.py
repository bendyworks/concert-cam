import facebook
import json


class Facebooker():
  album_id = 0
  def set_config(self, config):
    self.config = config

  def setup_oauth(self):
    global graph

    self.set_album_id()
    return self.set_token()

  def put_photo(self, filename):
    tags = json.dumps([])
    self.graph.put_photo(open(filename), 'Look at this cool photo!', self.album_id, tags=tags)

  def set_token(self):
    if self.config.fb_oauth_access_token:
      self.graph = facebook.GraphAPI(self.config.fb_oauth_access_token)
      return True
    else:
      return False

  def set_album_id(self):
    if self.config.album_id != "":
      self.album_id = self.config.album_id
    else:
      self.album_id = None
