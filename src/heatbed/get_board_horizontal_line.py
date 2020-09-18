import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def get_board_horizontal_line(startxy, endxy, layer, thickness):
  (startx, starty) = startxy
  (endx,endy) = endxy
  return get_line(startx, starty, endx, endy, layer, thickness)
