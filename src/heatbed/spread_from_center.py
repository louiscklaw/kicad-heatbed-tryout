import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def spread_from_center(center=3, num_to_spread=7, interval=1):
  # TODO: process even number in num_to_spread
  num_to_get = (num_to_spread-1)/2
  ruler = [i*interval for i in frange(1, num_to_get+1)]
  return list(sorted(map(lambda x: center-x, ruler)))+[float(center)]+ list( map(lambda x: center+x, ruler))
