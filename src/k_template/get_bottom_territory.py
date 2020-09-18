import os,sys
from pprint import pprint
from string import Template

K_TEMPLATE_DIR=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(K_TEMPLATE_DIR+'/..')

sys.path.append(SRC_DIR)

from common import *
from get_territory import *

def get_bottom_territory(width, height):
  startxy = (get_track_left_terrorties(width), get_track_bottom_terrorties(height))
  endxy = (get_track_right_terrorties(width), get_track_bottom_terrorties(height))
  return get_territory(startxy,endxy)
