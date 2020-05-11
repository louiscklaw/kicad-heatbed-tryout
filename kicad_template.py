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

$WATERMARK
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
    CENTERY=58,
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
# Front left led
(pad 1 smd roundrect (at 61.4625 44.7) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(pad 2 smd roundrect (at 63.3375 44.7) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(fp_text user %R (at 62.5 -44.7 180) (layer B.Fab)
  (effects (font (size 0.5 0.5) (thickness 0.08)))
)
(fp_line (start 62.6 -44.8) (end 62.5 -44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.6 -44.4) (end 62.6 -44.8) (layer B.SilkS) (width 0.12))
(fp_line (start 62.4 -44.7) (end 62.6 -44.4) (layer B.SilkS) (width 0.12))
(fp_line (start 62.7 -45) (end 62.4 -44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.7 -44.4) (end 62.7 -45) (layer B.SilkS) (width 0.12))
(fp_line (start 62.75 -44.2) (end 62.7 -44.4) (layer B.SilkS) (width 0.12))
(fp_line (start 62.25 -44.7) (end 62.75 -44.2) (layer B.SilkS) (width 0.12))
(fp_line (start 62.75 -45.2) (end 62.25 -44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.75 -44.2) (end 62.75 -45.2) (layer B.SilkS) (width 0.12))
(fp_line (start 64.185 -43.74) (end 64.185 -45.66) (layer B.SilkS) (width 0.12))
(fp_line (start 61.5 -44.1) (end 63.2 -44.1) (layer B.Fab) (width 0.1))
(fp_line (start 63.2 -44.1) (end 63.5 -44.4) (layer B.Fab) (width 0.1))
(fp_line (start 61.5 -45.3) (end 61.5 -44.1) (layer B.Fab) (width 0.1))
(fp_line (start 63.5 -45.3) (end 61.5 -45.3) (layer B.Fab) (width 0.1))
(fp_line (start 60.82 -45.65) (end 64.18 -45.65) (layer F.CrtYd) (width 0.05))
(fp_line (start 60.82 -43.75) (end 60.82 -45.65) (layer F.CrtYd) (width 0.05))
(fp_line (start 63.5 -44.4) (end 63.5 -45.3) (layer B.Fab) (width 0.1))
(fp_line (start 64.185 -45.66) (end 61.5 -45.66) (layer B.SilkS) (width 0.12))
(fp_line (start 62.5 -44.7) (end 62.6 -44.6) (layer B.SilkS) (width 0.12))
(fp_line (start 64.18 -43.75) (end 60.82 -43.75) (layer F.CrtYd) (width 0.05))
(fp_line (start 64.18 -45.65) (end 64.18 -43.75) (layer F.CrtYd) (width 0.05))
(fp_line (start 61.5 -43.74) (end 64.185 -43.74) (layer B.SilkS) (width 0.12))


# Front Right led
(pad 2 smd roundrect (at 61.555 -44.7 180) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(pad 1 smd roundrect (at 63.43 -44.7 180) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(fp_line (start 63.4 43.74) (end 60.715 43.74) (layer B.SilkS) (width 0.12))
(fp_line (start 60.72 45.65) (end 60.72 43.75) (layer F.CrtYd) (width 0.05))
(fp_line (start 60.72 43.75) (end 64.08 43.75) (layer F.CrtYd) (width 0.05))
(fp_text user %R (at 62.4 44.7) (layer B.Fab)
  (effects (font (size 0.5 0.5) (thickness 0.08)))
)
(fp_line (start 60.715 45.66) (end 63.4 45.66) (layer B.SilkS) (width 0.12))
(fp_line (start 61.4 44.4) (end 61.4 45.3) (layer B.Fab) (width 0.1))
(fp_line (start 64.08 43.75) (end 64.08 45.65) (layer F.CrtYd) (width 0.05))
(fp_line (start 64.08 45.65) (end 60.72 45.65) (layer F.CrtYd) (width 0.05))
(fp_line (start 61.4 45.3) (end 63.4 45.3) (layer B.Fab) (width 0.1))
(fp_line (start 63.4 45.3) (end 63.4 44.1) (layer B.Fab) (width 0.1))
(fp_line (start 61.7 44.1) (end 61.4 44.4) (layer B.Fab) (width 0.1))
(fp_line (start 63.4 44.1) (end 61.7 44.1) (layer B.Fab) (width 0.1))
(fp_line (start 60.715 43.74) (end 60.715 45.66) (layer B.SilkS) (width 0.12))
(fp_line (start 62.15 44.2) (end 62.15 45.2) (layer B.SilkS) (width 0.12))
(fp_line (start 62.15 45.2) (end 62.65 44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.65 44.7) (end 62.15 44.2) (layer B.SilkS) (width 0.12))
(fp_line (start 62.15 44.2) (end 62.2 44.4) (layer B.SilkS) (width 0.12))
(fp_line (start 62.2 44.4) (end 62.2 45) (layer B.SilkS) (width 0.12))
(fp_line (start 62.2 45) (end 62.5 44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.5 44.7) (end 62.3 44.4) (layer B.SilkS) (width 0.12))
(fp_line (start 62.3 44.4) (end 62.3 44.8) (layer B.SilkS) (width 0.12))
(fp_line (start 62.3 44.8) (end 62.4 44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.4 44.7) (end 62.3 44.6) (layer B.SilkS) (width 0.12))


(fp_line (start 61.5 44.7) (end 61.6 -44.7) (layer B.Cu) (width 0.5))
(fp_line (start 63.4 44.7) (end 63.4 -44.7) (layer B.Cu) (width 0.5))
# (fp_line (start 62.6 45.3) (end 62 44.7) (layer B.Cu) (width 0.5))
# (fp_line (start 62 44.7) (end 62.1 -44.2) (layer B.Cu) (width 0.5))
# (fp_line (start 62.1 -44) (end 63.6 -45.3) (layer B.Cu) (width 0.5))

# Track to front leds
(fp_line (start 61.5 44.7) (end 61.5 46) (layer B.Cu) (width 0.5))
(fp_line (start 61.5 46) (end 61.1 46.5) (layer B.Cu) (width 0.5))
(fp_line (start 61.1 46.5) (end -53.1 46.5) (layer B.Cu) (width 0.5))
(fp_line (start -53.1 46.5) (end -53.6 46) (layer B.Cu) (width 0.5))
(fp_line (start -53.6 46) (end -53.6 24.8) (layer B.Cu) (width 0.5))
(fp_line (start -53.6 24.8) (end -54.7 24) (layer B.Cu) (width 0.5))
(fp_line (start -54.7 24) (end -59.5 24) (layer B.Cu) (width 0.5))

(fp_line (start -55.3 46) (end -55.3 34.4) (layer B.Cu) (width 0.5))
(fp_line (start -55.3 34.4) (end -54.6 33.6) (layer B.Cu) (width 0.5))
(fp_line (start -54.6 33.6) (end -54.6 27.8) (layer B.Cu) (width 0.5))
(fp_line (start -54.6 27.8) (end -55.1 27.2) (layer B.Cu) (width 0.5))
(fp_line (start -55.1 27.2) (end -56.8 27.2) (layer B.Cu) (width 0.5))
(fp_line (start -56.8 27.2) (end -57.4 27.9) (layer B.Cu) (width 0.5))
(fp_line (start -57.4 27.9) (end -57.4 29.5) (layer B.Cu) (width 0.5))
(fp_line (start 63.4 44.7) (end 63.4 46.3) (layer B.Cu) (width 0.5))
(fp_line (start 63.4 46.3) (end 61.9 48) (layer B.Cu) (width 0.5))
(fp_line (start 61.9 48) (end -53.4 48) (layer B.Cu) (width 0.5))
(fp_line (start -53.4 48) (end -55.3 46) (layer B.Cu) (width 0.5))
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


def get_watermark(leftxy, github_link):
  leftx, lefty= leftxy
  watermark_template=Template('''
(fp_text user "$TEXT" (at $LEFTX $LEFTY) (layer B.SilkS)
  (effects (font (size 1 1) (thickness 0.15)) (justify right mirror))
)
(fp_text user "$TEXT" (at $LEFTX $LEFTY) (layer F.SilkS)
  (effects (font (size 1 1) (thickness 0.15)) (justify left))
)
  ''')

  return watermark_template.substitute(
    LEFTX=leftx,
    LEFTY=lefty,
    TEXT=github_link
  ).format(leftx, lefty, github_link).strip()
