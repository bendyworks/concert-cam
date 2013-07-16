import json

class Config:
  secret_key = ""
  def load(self, filename):
    config_file = self.load_config_file(filename)
    config = json.loads(config_file)
    self.secret_key = config["secret_key"]

  def load_config_file(self, filename):
    return open("camera_board/" + filename, "r+").read()
