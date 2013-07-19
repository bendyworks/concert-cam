import facebook

from config import Config
config = Config()
config.load("config.json")

class Facebooker():
  def setup_oauth(self):
    global graph

    if config.fb_oauth_access_token:
      self.graph = facebook.GraphAPI(config.fb_oauth_access_token)
      return True
    else:
      return False

  def put_photo(self, filename):
    self.graph.put_photo(open(filename), 'Look at this cool photo!', album_id_or_None, tags=tags)
