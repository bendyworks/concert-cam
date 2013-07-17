import os
import sys

def load_deps():
  parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  sys.path.insert(0,parentdir)
