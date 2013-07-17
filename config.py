import json
import sys

class Config:
  def load(self, filename):
    config_file = self.load_config_file(filename)
    config = json.loads(config_file)
    self.dictionary_to_locals(config)

  def dictionary_to_locals(self, definitions):
    for name, value in definitions.iteritems():
      setattr(self, name, value)

  def load_config_file(self, filename):
    return open(filename, "r+").read()
