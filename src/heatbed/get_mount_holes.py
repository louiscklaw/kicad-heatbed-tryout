import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def get_mount_holes(spacing):
  '''top_left, top_right, bottom_left, bottom_right'''

  radius=2

  mount_hole_top_left = (get_neg_x()+spacing, get_neg_y()+spacing)
  mount_hole_top_right = (get_pos_x()-spacing, get_neg_y()+spacing)
  mount_hole_bottom_left = (get_neg_x()+spacing, get_pos_y()-spacing)
  mount_hole_bottom_right = (get_pos_x()-spacing, get_pos_y()-spacing)

  return [
    get_mount_hole(mount_hole_top_left,radius,2),
    get_mount_hole(mount_hole_top_right,radius,2),
    get_mount_hole(mount_hole_bottom_left,radius,2),
    get_mount_hole(mount_hole_bottom_right,radius,2)
  ]
