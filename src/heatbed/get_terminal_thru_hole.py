import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def get_terminal_thru_hole(centerxy, pad_num=1):
  centerx, centery = centerxy
  return Template('''(pad $PAD_NUM thru_hole circle (at $CENTERX $CENTERY) (size 1.5 1.5) (drill 0.5) (layers *.Cu B.Paste B.Mask))''').substitute(CENTERX=centerx, CENTERY=centery, PAD_NUM=pad_num)
