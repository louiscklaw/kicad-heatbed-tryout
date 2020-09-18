import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

from check_y_inside import *


def check_y_inside_top_left_mount_area(y):
  return check_y_inside(y, get_bed_top_terrorties(),top_left_mount_start)
