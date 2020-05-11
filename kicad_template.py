import os,sys

from string import Template
from common import *

heatbed_component_template = Template('''
(module 130_130_heatbed-route (layer F.Cu) (tedit 5EB4FE57)
  (fp_text reference REF** (at 0 21.844) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value 130_130_heatbed-route (at 0 19.304) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )

$TRACKS

$HEATBED_SURROUNDING

$MOUNT_HOLE

$TERMINAL

$BOILERPLATE

$TERRORTIES

)
'''.strip())

TOTAL_LENGTH=Template('''
(fp_text user $LENGTH (at 0 69.85) (layer F.SilkS)
  (effects (font (size 1 1) (thickness 0.15)))
)
'''.strip())

def print_total_track_length(length):
  return TOTAL_LENGTH.substitute(
    LENGTH=length
  )

__BOILERPLATE=Template('''
(fp_text user "$TEXT" (at 0 $Y_POS) (layer F.SilkS)
  (effects (font (size 1 1) (thickness 0.15))(justify left))
)
'''.strip())

def print_boiler_plate(in_texts):
  output = []
  starting_line_y=70
  space_between_lines = 2

  y_positions = [starting_line_y + space_between_lines*idx for idx in range(0,len(in_texts))]

  for y_pos, in_text in zip(y_positions, in_texts):
    in_text=in_text.replace(' ','_')
    output.append(__BOILERPLATE.substitute(TEXT=in_text, Y_POS=y_pos))


  return '\n'.join(output)


def get_territory(startxy, endxy):
  startx, starty = startxy
  endx, endy = endxy
  return Template('''(fp_line (start $STARTX $STARTY) (end $ENDX $ENDY) (layer Dwgs.User) (width 1))'''.strip()).substitute(
      STARTX=startx, STARTY=starty, ENDX=endx, ENDY=endy
    )

def get_top_territory():
  startxy = (get_track_left_terrorties(), get_track_top_terrorties())
  endxy = (get_track_right_terrorties(), get_track_top_terrorties())
  return get_territory(startxy,endxy)

def get_bottom_territory():
  startxy = (get_track_left_terrorties(), get_track_bottom_terrorties())
  endxy = (get_track_right_terrorties(), get_track_bottom_terrorties())
  return get_territory(startxy,endxy)

def get_left_territory():
  startxy = (get_track_left_terrorties(), get_track_top_terrorties())
  endxy = (get_track_left_terrorties(), get_track_bottom_terrorties())
  return get_territory(startxy,endxy)

def get_right_territory():
  startxy = (get_track_right_terrorties(), get_track_top_terrorties())
  endxy = (get_track_right_terrorties(), get_track_bottom_terrorties())
  return get_territory(startxy,endxy)

def draw_terrorties():
  # (fp_line (start -63.5 -63.5) (end -55.88 -63.5) (layer Dwgs.User) (width 0.1))

  return [
    get_top_territory(),
    get_left_territory(),
    get_right_territory(),
    get_bottom_territory()
    ]
