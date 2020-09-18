import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def get_line(startx, starty, endx, endy, layer, thickness):
  return get_track((startx, starty), (endx, endy), layer, thickness)
