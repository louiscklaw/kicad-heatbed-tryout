import os,sys
from pprint import pprint

TEST_DIR=os.path.dirname(__file__)
PROJ_HOME=os.path.abspath(TEST_DIR+'/..')

SRC_DIR=os.path.abspath(PROJ_HOME+'/src')
SRC_HEATBED=os.path.abspath(SRC_DIR+'/heatbed')

import heatbed

def test():
  heatbed.helloworld()
