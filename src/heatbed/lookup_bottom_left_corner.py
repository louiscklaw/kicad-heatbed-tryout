import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def lookup_bottom_left_corner(y):
  '''y=x+c'''
  '''y=x+ramp_line_c'''
  return max(get_track_left_terrorties(), y-(ramp_line_left))
