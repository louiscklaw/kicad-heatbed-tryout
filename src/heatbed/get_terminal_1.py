import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def get_terminal_1(centerxy, width_and_height,pad_num):
  centerx, centery = centerxy
  width, height = width_and_height
  terminal_1_array_y=range(12,24+1,2)
  return Template('''
(pad $PAD_NUM thru_hole roundrect (at $CENTERX $CENTERY) (size $WIDTH $HEIGHT) (drill 0.5) (layers *.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
$THRU_HOLE
''').substitute(
    CENTERX=centerx, CENTERY=centery, PAD_NUM=pad_num,
    WIDTH=width, HEIGHT=height,
    THRU_HOLE='\n'.join(
      # RIGHT TERMINAL THRU HOLE
      [get_terminal_thru_hole((-62.5, centery),1) for centery in terminal_1_array_y]+
      # CENTER TERMINAL THRU HOLE
      [get_terminal_thru_hole((-61, centery),1) for centery in terminal_1_array_y]+
      # LEFT TERMINAL THRU HOLE
      [get_terminal_thru_hole((-59.5, centery),1) for centery in terminal_1_array_y]
      )
  )
