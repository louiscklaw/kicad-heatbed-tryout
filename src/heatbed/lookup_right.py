import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def lookup_right(y):
  if check_y_inside(y, top_right_mount_start,bottom_right_mount_start):
    return get_track_right_terrorties()
  elif check_y_inside_top_right_mount_area(y):
    # check if y inside the top right corner mount
    return lookup_top_right_corner(y)
  elif check_y_inside_bottom_right_mount_area(y):
    # check if y inside the bottom right corner mount
    return lookup_bottom_right_corner(y)
  else:
    return -1
