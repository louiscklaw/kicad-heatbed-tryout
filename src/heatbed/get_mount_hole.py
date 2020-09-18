import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def get_mount_hole(centerxy, mask_radius, mask_thickness):
  (centerx, centery) = centerxy
  center_x_by_mask_radius = centerx-mask_radius
  return Template('''
  (fp_circle (center $CENTERX $CENTERY) (end $RADIUS_CENTER_X $CENTERY) (layer F.Mask) (width $MASK_THICKNESS))
  (fp_circle (center $CENTERX $CENTERY) (end $RADIUS_CENTER_X $CENTERY) (layer B.Mask) (width $MASK_THICKNESS))
  (pad "" np_thru_hole circle (at $CENTERX $CENTERY) (size 3 3) (drill 3) (layers *.Cu *.Mask))
  '''.strip()).substitute(
    CENTERX=centerx,
    CENTERY=centery,
    RADIUS_CENTER_X=center_x_by_mask_radius,
    MASK_THICKNESS=mask_thickness
  )
