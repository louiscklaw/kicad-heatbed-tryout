import os,sys
from pprint import pprint


SRC_DIR=os.path.dirname(__file__)
PROJ_HOME=os.path.abspath(SRC_DIR+'/..')
SRC_HEATBED=os.path.abspath(SRC_DIR+'/heatbed')

sys.path.append(SRC_DIR)

from check_y_inside import *

def helloworld():
  print('helloworld from {}'.format(__file__))
