import os,sys
from pprint import pprint
from string import Template

K_TEMPLATE_DIR=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(K_TEMPLATE_DIR+'/..')

sys.path.append(K_TEMPLATE_DIR)

from get_top_territory import *
from get_left_territory import *
from get_right_territory import *
from get_bottom_territory import *

def draw_terrorties(width, height):
  # (fp_line (start -63.5 -63.5) (end -55.88 -63.5) (layer Dwgs.User) (width 0.1))

  return [
    get_top_territory(width, height),
    get_left_territory(width, height),
    get_right_territory(width, height),
    get_bottom_territory(width, height)
    ]
