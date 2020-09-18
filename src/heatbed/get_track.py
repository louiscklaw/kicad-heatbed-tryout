import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

# kicad stuff
def get_track(startxy, endxy, layer, thickness):
  startx, starty = startxy
  endx, endy = endxy
  return Template('''(fp_line (start $STARTX $STARTY) (end $ENDX $ENDY) (layer $LAYER) (width $THICKNESS))''').substitute(
    STARTX=startx,
    STARTY=starty,
    ENDX=endx,
    ENDY=endy,
    LAYER=layer,
    THICKNESS=thickness
  )
