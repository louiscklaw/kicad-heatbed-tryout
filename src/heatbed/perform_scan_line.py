import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def perform_scan_line():
  point_list=[]

  # print(get_track_bottom_terrorties())
  # # sys.exit()

  # scan line algorithm
  for i in frange(get_track_top_terrorties(),get_track_bottom_terrorties(), heatbed_track_space):
    point_list.append((i, lookup_left(i),lookup_right(i)))

  return point_list
