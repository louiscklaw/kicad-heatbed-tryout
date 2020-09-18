import os,sys
from pprint import pprint
from string import Template

TOTAL_LENGTH=Template('''
(fp_text user $LENGTH (at 0 69.85) (layer F.SilkS)
  (effects (font (size 1 1) (thickness 0.15)))
)
'''.strip())

def print_total_track_length(length):
  return TOTAL_LENGTH.substitute(LENGTH=length)
