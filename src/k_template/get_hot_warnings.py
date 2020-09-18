import os,sys
from pprint import pprint
from string import Template

K_TEMPLATE_DIR=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(K_TEMPLATE_DIR+'/..')

sys.path.append(SRC_DIR)

def get_hot_warnings():
  return '#'
