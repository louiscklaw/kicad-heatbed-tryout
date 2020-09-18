import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

from check_y_inside import *
from common import *

from config import *

def check_y_inside_top_left_mount_area(y, width, height):
  top_left_mount_start = get_bed_top_left_corner(width, height)[1]+top_left_corner_space
  return check_y_inside(y, get_bed_top_terrorties(height),top_left_mount_start)
