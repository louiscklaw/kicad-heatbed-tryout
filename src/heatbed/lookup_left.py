import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

from check_y_inside import *

def lookup_left(y):
  top_left_mount_start = get_bed_top_left_corner()[1]+top_left_corner_space
  bottom_left_mount_start = get_bed_bottom_left_corner()[1]-bottom_left_corner_space

  if check_y_inside(y, top_left_mount_start,bottom_left_mount_start):
    return get_track_left_terrorties()
  elif check_y_inside_top_left_mount_area(y):
    return lookup_top_left_corner(y)
  elif check_y_inside_bottom_left_mount_area(y):
    return lookup_bottom_left_corner(y)
  else:
    return -1
