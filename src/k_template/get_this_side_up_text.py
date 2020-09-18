import os,sys
from pprint import pprint
from string import Template

from this_side_up_text_template import *

def get_this_side_up_text():
  # -2.25 59.5
  return this_side_up_text_template.substitute(
    CENTERX=-55,
    CENTERY=58,
    TEXT='THIS SIDE UP'
    )
