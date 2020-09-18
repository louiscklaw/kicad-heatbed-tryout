import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def get_terminals():
  terminal_1_string=get_terminal_1(TERMINAL_1_CENTERXY,(5,15), 1)
  terminal_2_string=get_terminal_2(TERMINAL_2_CENTERXY,(5,15), 2)
  return [terminal_1_string,terminal_2_string ]
