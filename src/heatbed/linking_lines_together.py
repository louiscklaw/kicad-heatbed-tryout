import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def linking_lines_together(point_array):
  tracks=[]


  for idx in range(0,len(point_array)-1):
    next_idx = idx+1
    y, leftx,rightx = point_array[idx]
    next_y, next_leftx,next_rightx = point_array[next_idx]
    if is_even(idx):
      tracks.append(((leftx,y), (next_leftx,next_y)))
    else:
      tracks.append(((rightx,y), (next_rightx, next_y)))

  return tracks
