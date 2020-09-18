import os,sys
from pprint import pprint


SRC_DIR=os.path.dirname(__file__)
PROJ_HOME=os.path.abspath(SRC_DIR+'/..')
SRC_HEATBED=os.path.abspath(SRC_DIR+'/heatbed')

sys.path.append(SRC_DIR)

from check_y_inside import *

def check_y_inside(y, in_min, in_max):
  return y >= in_min and y <= in_max
