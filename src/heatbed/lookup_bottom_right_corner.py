import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def lookup_bottom_right_corner(y):
  '''y=x-c'''
  return min(get_track_right_terrorties(), -y+ramp_line_right)
