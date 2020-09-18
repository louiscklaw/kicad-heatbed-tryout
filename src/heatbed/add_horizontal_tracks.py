import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def add_horizontal_tracks(point_array):
  tracks=[]
  for idx in range(0,len(point_array)):
    y, leftx,rightx = point_array[idx]
    tracks.append(((leftx, y ), (rightx, y)))
  return tracks
