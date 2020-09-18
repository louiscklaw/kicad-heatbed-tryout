import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def check_y_inside(y, in_min, in_max):
  return y >= in_min and y <= in_max
