import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def track_end_bottom_left_lookup_from_x(x):
  return -((-1) * x - track_start_corner_space)
