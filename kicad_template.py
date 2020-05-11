import os,sys

from string import Template
from common import *
from config import *

this_side_up_text_template = Template('''
(fp_text user "$TEXT" (at $CENTERX $CENTERY) (layer F.SilkS)
(effects (font (size 3 3) (thickness 0.3)) (justify left)))
'''.strip())

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

$MISC_TEXT

$MISC_COMPONENTS

$HOT_WARNING

$CAUTION_TEXT
)
'''.strip())

TOTAL_LENGTH=Template('''
(fp_text user $LENGTH (at 0 69.85) (layer F.SilkS)
  (effects (font (size 1 1) (thickness 0.15)))
)
'''.strip())

def print_total_track_length(length):
  return TOTAL_LENGTH.substitute(LENGTH=length)

__BOILERPLATE=Template('''(fp_text user "$TEXT" (at $X_POS $Y_POS) (layer F.SilkS)(effects (font (size 1 1) (thickness 0.15))(justify left)))'''.strip())

def print_boiler_plate(in_texts):
  output = []
  starting_line_y=30
  starting_x = 10
  space_between_lines = 2

  y_positions = [starting_line_y + space_between_lines*idx for idx in range(0,len(in_texts))]

  for y_pos, in_text in zip(y_positions, in_texts):
    in_text=in_text.replace(' ','_')
    output.append(__BOILERPLATE.substitute(TEXT=in_text, Y_POS=y_pos, X_POS=starting_x))


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

def get_this_side_up_text():
  # -2.25 59.5
  return this_side_up_text_template.substitute(
    CENTERX=-55,
    CENTERY=60,
    TEXT='THIS SIDE UP'
    )

def get_led_and_resistors():
  return '''
# LED1
#(pad 1 smd roundrect (at -61.9375 27.75) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))
#(pad R1 smd roundrect (at -60.0625 27.75) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))

# 1 TO LED 1
(fp_line (start -62 27.75) (end -62 26.5) (layer B.Cu) (width 0.3))
(fp_line (start -62 26.5) (end -61.75 26.25) (layer B.Cu) (width 0.3))
(fp_line (start -61.75 26.25) (end -61.25 26.25) (layer B.Cu) (width 0.3))
(fp_line (start -61.25 26.25) (end -61 26) (layer B.Cu) (width 0.3))
(fp_line (start -61 26) (end -61 25) (layer B.Cu) (width 0.3))

# LED to R1
(fp_line (start -62 27.7) (end -62 30.3) (layer B.Cu) (width 0.5))
(fp_line (start -60.1 27.7) (end -60.1 30.2) (layer B.Cu) (width 0.5))
(fp_line (start -60.1 30.2) (end -58.8 30.2) (layer B.Cu) (width 0.5))
(fp_line (start -58.8 30.2) (end -58.6 30) (layer B.Cu) (width 0.5))
(fp_line (start -58.6 30) (end -58.6 29.7) (layer B.Cu) (width 0.5))
(fp_line (start -58.6 29.7) (end -58.4 29.5) (layer B.Cu) (width 0.5))
(fp_line (start -58.4 29.5) (end -57.8 29.5) (layer B.Cu) (width 0.5))
(fp_line (start -55.9 29.5) (end -55.9 33.5) (layer B.Cu) (width 0.5))
(fp_line (start -55.9 33.5) (end -56.2 33.8) (layer B.Cu) (width 0.5))
(fp_line (start -56.2 33.8) (end -59.5 33.8) (layer B.Cu) (width 0.5))

#LED1
(pad 1 smd roundrect (at -61.9375 27.75) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))
(pad R1 smd roundrect (at -60.0625 27.75) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))

#R1
(pad R1 smd roundrect (at -57.7375 29.55 180) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))
(pad 2 smd roundrect (at -55.8625 29.55 180) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))

#LED2
(pad 1 smd roundrect (at -61.9375 30.25 180) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))
(pad R1 smd roundrect (at -60.0625 30.25 180) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))

{}
'''.format(
  get_front_leds()
).strip()

def get_front_leds():
  return '''
(pad 1 smd roundrect (at 63.7 43.4625 270) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(pad 2 smd roundrect (at 63.7 45.3375 270) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(pad 2 smd roundrect (at 63.6 -43.455 270) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(pad 1 smd roundrect (at 63.6 -45.33 270) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))


(fp_line (start 64.66 45.4) (end 64.66 42.715) (layer B.SilkS) (width 0.12))
(fp_line (start 62.75 42.72) (end 64.65 42.72) (layer F.CrtYd) (width 0.05))
(fp_line (start 64.65 42.72) (end 64.65 46.08) (layer F.CrtYd) (width 0.05))
(fp_text user %R (at 63.7 44.4 270) (layer B.Fab)
  (effects (font (size 0.5 0.5) (thickness 0.08)))
)
(fp_line (start 62.74 42.715) (end 62.74 45.4) (layer B.SilkS) (width 0.12))
(fp_line (start 64 43.4) (end 63.1 43.4) (layer B.Fab) (width 0.1))
(fp_line (start 64.65 46.08) (end 62.75 46.08) (layer F.CrtYd) (width 0.05))
(fp_line (start 62.75 46.08) (end 62.75 42.72) (layer F.CrtYd) (width 0.05))
(fp_line (start 63.1 43.4) (end 63.1 45.4) (layer B.Fab) (width 0.1))
(fp_line (start 63.1 45.4) (end 64.3 45.4) (layer B.Fab) (width 0.1))
(fp_line (start 64.3 43.7) (end 64 43.4) (layer B.Fab) (width 0.1))
(fp_line (start 64.3 45.4) (end 64.3 43.7) (layer B.Fab) (width 0.1))
(fp_line (start 64.66 42.715) (end 62.74 42.715) (layer B.SilkS) (width 0.12))
(fp_line (start 64.2 44.15) (end 63.2 44.15) (layer B.SilkS) (width 0.12))
(fp_line (start 63.2 44.15) (end 63.7 44.65) (layer B.SilkS) (width 0.12))
(fp_line (start 63.7 44.65) (end 64.2 44.15) (layer B.SilkS) (width 0.12))
(fp_line (start 64.2 44.15) (end 64 44.2) (layer B.SilkS) (width 0.12))
(fp_line (start 64 44.2) (end 63.4 44.2) (layer B.SilkS) (width 0.12))
(fp_line (start 63.4 44.2) (end 63.7 44.5) (layer B.SilkS) (width 0.12))
(fp_line (start 63.7 44.5) (end 64 44.3) (layer B.SilkS) (width 0.12))
(fp_line (start 64 44.3) (end 63.6 44.3) (layer B.SilkS) (width 0.12))
(fp_line (start 63.6 44.3) (end 63.7 44.4) (layer B.SilkS) (width 0.12))
(fp_line (start 63.7 44.4) (end 63.8 44.3) (layer B.SilkS) (width 0.12))
(fp_line (start 64.55 -46.0725) (end 64.55 -42.7125) (layer F.CrtYd) (width 0.05))
(fp_text user %R (at 63.6 -44.3925 270) (layer B.Fab)
  (effects (font (size 0.5 0.5) (thickness 0.08)))
)
(fp_line (start 63 -43.3925) (end 64.2 -43.3925) (layer B.Fab) (width 0.1))
(fp_line (start 64.55 -42.7125) (end 62.65 -42.7125) (layer F.CrtYd) (width 0.05))
(fp_line (start 64.2 -45.0925) (end 63.9 -45.3925) (layer B.Fab) (width 0.1))
(fp_line (start 63.3 -44.5925) (end 63.6 -44.2925) (layer B.SilkS) (width 0.12))
(fp_line (start 62.65 -46.0725) (end 64.55 -46.0725) (layer F.CrtYd) (width 0.05))
(fp_line (start 64.1 -44.6425) (end 63.9 -44.5925) (layer B.SilkS) (width 0.12))
(fp_line (start 63.9 -45.3925) (end 63 -45.3925) (layer B.Fab) (width 0.1))
(fp_line (start 63.6 -44.2925) (end 63.9 -44.4925) (layer B.SilkS) (width 0.12))
(fp_line (start 64.56 -43.3925) (end 64.56 -46.0775) (layer B.SilkS) (width 0.12))
(fp_line (start 63.9 -44.5925) (end 63.3 -44.5925) (layer B.SilkS) (width 0.12))
(fp_line (start 64.2 -43.3925) (end 64.2 -45.0925) (layer B.Fab) (width 0.1))
(fp_line (start 62.64 -46.0775) (end 62.64 -43.3925) (layer B.SilkS) (width 0.12))
(fp_line (start 64.56 -46.0775) (end 62.64 -46.0775) (layer B.SilkS) (width 0.12))
(fp_line (start 63 -45.3925) (end 63 -43.3925) (layer B.Fab) (width 0.1))
(fp_line (start 63.9 -44.4925) (end 63.5 -44.4925) (layer B.SilkS) (width 0.12))
(fp_line (start 63.5 -44.4925) (end 63.6 -44.3925) (layer B.SilkS) (width 0.12))
(fp_line (start 64.1 -44.6425) (end 63.1 -44.6425) (layer B.SilkS) (width 0.12))
(fp_line (start 62.65 -42.7125) (end 62.65 -46.0725) (layer F.CrtYd) (width 0.05))
(fp_line (start 63.1 -44.6425) (end 63.6 -44.1425) (layer B.SilkS) (width 0.12))
(fp_line (start 63.6 -44.1425) (end 64.1 -44.6425) (layer B.SilkS) (width 0.12))
(fp_line (start 63.6 -44.3925) (end 63.7 -44.4925) (layer B.SilkS) (width 0.12))


  '''.strip()

def get_caution_title(leftxy, text):
  leftx, lefty= leftxy
  return '''
(fp_text user "{}" (at {} {}) (layer F.SilkS)
  (effects (font (size 3 3) (thickness 0.3)) (justify left))
)
  '''.format(text, leftx, lefty).strip()

def get_caution_description(leftxy, text):
  leftx, lefty=leftxy
  return '''
(fp_text user "{}" (at {} {}) (layer F.SilkS)
  (effects (font (size 2 2) (thickness 0.2)) (justify left))
)
'''.format(
  text, leftx, lefty
).strip()

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

def get_hot_warnings():
  return '#'