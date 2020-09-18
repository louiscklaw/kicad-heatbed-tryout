import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

# (pad 2 thru_hole roundrect (at -60.96 32.004) (size 5 10) (drill 3) (layers *.Cu *.Mask) (roundrect_rratio 0.25))
def get_terminal(centerxy, width_and_height,pad_num):
  centerx, centery = centerxy
  width, height = width_and_height
  return Template('(pad $PAD_NUM thru_hole roundrect (at $CENTERX $CENTERY) (size $WIDTH $HEIGHT) (drill 3) (layers *.Cu *.Mask B.Paste) (roundrect_rratio 0.25))').substitute(
    CENTERX=centerx, CENTERY=centery, PAD_NUM=pad_num,
    WIDTH=width, HEIGHT=height
  )
