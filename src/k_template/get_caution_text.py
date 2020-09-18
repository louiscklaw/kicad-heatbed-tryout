import os,sys
from pprint import pprint
from string import Template

K_TEMPLATE_DIR=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(K_TEMPLATE_DIR+'/..')

sys.path.append(SRC_DIR)

from get_caution_title import *
from get_caution_description import *

def get_caution_text():
  description_line_spacing=5
  description_lines_y=range(35,99,description_line_spacing)

  description_lines_xy = [(-55, y) for y in description_lines_y]
  description_lines=[
    'Power off the bed',
    'and wait at least 10mins before touching',
    'Do not leave unattended.',
    'Keep away from children.'
  ]

  return '''
{}
{}
'''.format(
  get_caution_title((-55,30),'CAUTION:'),
  '\n'.join(
    [ get_caution_description(leftxy,description) for (leftxy, description) in zip(description_lines_xy,description_lines) ]
  )

)
