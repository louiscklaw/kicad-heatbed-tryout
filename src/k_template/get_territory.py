import os,sys
from pprint import pprint
from string import Template

def get_territory(startxy, endxy):
  startx, starty = startxy
  endx, endy = endxy
  return Template('''(fp_line (start $STARTX $STARTY) (end $ENDX $ENDY) (layer Dwgs.User) (width 1))'''.strip()).substitute(
      STARTX=startx, STARTY=starty, ENDX=endx, ENDY=endy
    )
