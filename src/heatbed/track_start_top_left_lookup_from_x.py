import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def track_start_top_left_lookup_from_x(x):
  '''y=mx+c'''
  return -(x+ track_start_corner_space)
