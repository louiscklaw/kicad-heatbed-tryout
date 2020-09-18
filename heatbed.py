#!/usr/bin/env python3

import os,sys
from pprint import pprint
from string import Template

from config import *
from kicad_template import *
from common import *


tracks=[]


top_left_mount_start = get_bed_top_left_corner()[1]+top_left_corner_space
bottom_left_mount_start = get_bed_bottom_left_corner()[1]-bottom_left_corner_space
top_right_mount_start = get_bed_top_right_corner()[1]+top_right_corner_space
bottom_right_mount_start = get_bed_bottom_right_corner()[1]-bottom_right_corner_space


def check_y_inside(y, in_min, in_max):
  return y >= in_min and y <= in_max

def check_y_inside_top_left_mount_area(y):
  return check_y_inside(y, get_bed_top_terrorties(),top_left_mount_start)

def check_y_inside_bottom_left_mount_area(y):
  return check_y_inside(y, bottom_left_mount_start, get_bed_bottom_terrorties())

def check_y_inside_top_right_mount_area(y):
  return check_y_inside(y, get_bed_top_terrorties(),top_right_mount_start)

def check_y_inside_bottom_right_mount_area(y):
  return check_y_inside(y, bottom_right_mount_start, get_bed_bottom_terrorties())

def lookup_left(y):
  if check_y_inside(y, top_left_mount_start,bottom_left_mount_start):
    return get_track_left_terrorties()
  elif check_y_inside_top_left_mount_area(y):
    return lookup_top_left_corner(y)
  elif check_y_inside_bottom_left_mount_area(y):
    return lookup_bottom_left_corner(y)
  else:
    return -1

def lookup_right(y):
  if check_y_inside(y, top_right_mount_start,bottom_right_mount_start):
    return get_track_right_terrorties()
  elif check_y_inside_top_right_mount_area(y):
    # check if y inside the top right corner mount
    return lookup_top_right_corner(y)
  elif check_y_inside_bottom_right_mount_area(y):
    # check if y inside the bottom right corner mount
    return lookup_bottom_right_corner(y)
  else:
    return -1

def lookup_top_left_corner(y):
  '''y=-x+c'''
  '''y=-x+ramp_line_c'''
  return max(get_track_left_terrorties(), -y-(ramp_line_left))

def lookup_bottom_left_corner(y):
  '''y=x+c'''
  '''y=x+ramp_line_c'''
  return max(get_track_left_terrorties(), y-(ramp_line_left))

def lookup_top_right_corner(y):
  '''y=x-c'''
  return min(get_track_right_terrorties(), y+ramp_line_right)

def lookup_bottom_right_corner(y):
  '''y=x-c'''
  return min(get_track_right_terrorties(), -y+ramp_line_right)

def is_even(y):
  return y % 2

def add_horizontal_tracks(point_array):
  tracks=[]
  for idx in range(0,len(point_array)):
    y, leftx,rightx = point_array[idx]
    tracks.append(((leftx, y ), (rightx, y)))
  return tracks

def linking_lines_together(point_array):
  tracks=[]


  for idx in range(0,len(point_array)-1):
    next_idx = idx+1
    y, leftx,rightx = point_array[idx]
    next_y, next_leftx,next_rightx = point_array[next_idx]
    if is_even(idx):
      tracks.append(((leftx,y), (next_leftx,next_y)))
    else:
      tracks.append(((rightx,y), (next_rightx, next_y)))

  return tracks

# kicad stuff
def get_track(startxy, endxy, layer, thickness):
  startx, starty = startxy
  endx, endy = endxy
  return Template('''(fp_line (start $STARTX $STARTY) (end $ENDX $ENDY) (layer $LAYER) (width $THICKNESS))''').substitute(
    STARTX=startx,
    STARTY=starty,
    ENDX=endx,
    ENDY=endy,
    LAYER=layer,
    THICKNESS=thickness
  )

def get_line(startx, starty, endx, endy, layer, thickness):
  return get_track((startx, starty), (endx, endy), layer, thickness)

def perform_scan_line():
  point_list=[]

  # print(get_track_bottom_terrorties())
  # # sys.exit()

  # scan line algorithm
  for i in frange(get_track_top_terrorties(),get_track_bottom_terrorties(), heatbed_track_space):
    point_list.append((i, lookup_left(i),lookup_right(i)))

  return point_list


def get_mount_hole(centerxy, mask_radius, mask_thickness):
  (centerx, centery) = centerxy
  center_x_by_mask_radius = centerx-mask_radius
  return Template('''
  (fp_circle (center $CENTERX $CENTERY) (end $RADIUS_CENTER_X $CENTERY) (layer F.Mask) (width $MASK_THICKNESS))
  (fp_circle (center $CENTERX $CENTERY) (end $RADIUS_CENTER_X $CENTERY) (layer B.Mask) (width $MASK_THICKNESS))
  (pad "" np_thru_hole circle (at $CENTERX $CENTERY) (size 3 3) (drill 3) (layers *.Cu *.Mask))
  '''.strip()).substitute(
    CENTERX=centerx,
    CENTERY=centery,
    RADIUS_CENTER_X=center_x_by_mask_radius,
    MASK_THICKNESS=mask_thickness
  )

def get_mount_holes(spacing):
  '''top_left, top_right, bottom_left, bottom_right'''

  radius=2

  mount_hole_top_left = (get_neg_x()+spacing, get_neg_y()+spacing)
  mount_hole_top_right = (get_pos_x()-spacing, get_neg_y()+spacing)
  mount_hole_bottom_left = (get_neg_x()+spacing, get_pos_y()-spacing)
  mount_hole_bottom_right = (get_pos_x()-spacing, get_pos_y()-spacing)

  return [
    get_mount_hole(mount_hole_top_left,radius,2),
    get_mount_hole(mount_hole_top_right,radius,2),
    get_mount_hole(mount_hole_bottom_left,radius,2),
    get_mount_hole(mount_hole_bottom_right,radius,2)
  ]

def track_start_top_left_lookup_from_x(x):
  '''y=mx+c'''
  return -(x+ track_start_corner_space)

def track_start_top_left_lookup_from_y(y):
  return (-y)-track_start_corner_space

def track_end_bottom_left_lookup_from_x(x):
  return -((-1) * x - track_start_corner_space)

def track_end_bottom_left_lookup_from_y(y):
  return -((-y)+track_start_corner_space)

def get_track_start():
  # terminal to the heatbed start
  return

board_top_left = (get_neg_x(),get_neg_y())
board_top_right = (get_pos_x(),get_neg_y())
board_bottom_left = (get_neg_x(),get_pos_y())
board_bottom_right = (get_pos_x(),get_pos_y())

# (pad 2 thru_hole roundrect (at -60.96 32.004) (size 5 10) (drill 3) (layers *.Cu *.Mask) (roundrect_rratio 0.25))
def get_terminal(centerxy, width_and_height,pad_num):
  centerx, centery = centerxy
  width, height = width_and_height
  return Template('(pad $PAD_NUM thru_hole roundrect (at $CENTERX $CENTERY) (size $WIDTH $HEIGHT) (drill 3) (layers *.Cu *.Mask B.Paste) (roundrect_rratio 0.25))').substitute(
    CENTERX=centerx, CENTERY=centery, PAD_NUM=pad_num,
    WIDTH=width, HEIGHT=height
  )

def get_terminal_1(centerxy, width_and_height,pad_num):
  centerx, centery = centerxy
  width, height = width_and_height
  terminal_1_array_y=range(12,24+1,2)
  return Template('''
(pad $PAD_NUM thru_hole roundrect (at $CENTERX $CENTERY) (size $WIDTH $HEIGHT) (drill 0.5) (layers *.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
$THRU_HOLE
''').substitute(
    CENTERX=centerx, CENTERY=centery, PAD_NUM=pad_num,
    WIDTH=width, HEIGHT=height,
    THRU_HOLE='\n'.join(
      # RIGHT TERMINAL THRU HOLE
      [get_terminal_thru_hole((-62.5, centery),1) for centery in terminal_1_array_y]+
      # CENTER TERMINAL THRU HOLE
      [get_terminal_thru_hole((-61, centery),1) for centery in terminal_1_array_y]+
      # LEFT TERMINAL THRU HOLE
      [get_terminal_thru_hole((-59.5, centery),1) for centery in terminal_1_array_y]
      )
  )

def spread_from_center(center=3, num_to_spread=7, interval=1):
  # TODO: process even number in num_to_spread
  num_to_get = (num_to_spread-1)/2
  ruler = [i*interval for i in frange(1, num_to_get+1)]
  return list(sorted(map(lambda x: center-x, ruler)))+[float(center)]+ list( map(lambda x: center+x, ruler))

def get_terminal_thru_hole(centerxy, pad_num=1):
  centerx, centery = centerxy
  return Template('''(pad $PAD_NUM thru_hole circle (at $CENTERX $CENTERY) (size 1.5 1.5) (drill 0.5) (layers *.Cu B.Paste B.Mask))''').substitute(CENTERX=centerx, CENTERY=centery, PAD_NUM=pad_num)

def get_terminal_2(centerxy, width_and_height,pad_num):
  centerx, centery = centerxy
  width, height = width_and_height
  through_hole_delta=1.25
  # print(spread_from_center(3,7,1))
  # sys.exit()
  terminal_2_array_y=range(34,46+1,2)

  return Template('''
(pad $PAD_NUM thru_hole roundrect (at $CENTERX $CENTERY) (size $WIDTH $HEIGHT) (drill 0.5) (layers *.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
$THRU_HOLE
''').substitute(
    CENTERX=centerx, CENTERY=centery, PAD_NUM=pad_num,
    WIDTH=width, HEIGHT=height,
    THRU_HOLE='\n'.join(
      # RIGHT TERMINAL THRU HOLE
      [get_terminal_thru_hole((-62.5, centery),2) for centery in terminal_2_array_y]+
      # CENTER TERMINAL THRU HOLE
      [get_terminal_thru_hole((-61, centery),2) for centery in terminal_2_array_y]+
      # LEFT TERMINAL THRU HOLE
      [get_terminal_thru_hole((-59.5, centery),2) for centery in terminal_2_array_y]
      )
  )


def get_terminals():
  terminal_1_string=get_terminal_1(TERMINAL_1_CENTERXY,(5,15), 1)
  terminal_2_string=get_terminal_2(TERMINAL_2_CENTERXY,(5,15), 2)
  return [terminal_1_string,terminal_2_string ]

def get_board_horizontal_line(startxy, endxy, layer, thickness):
  (startx, starty) = startxy
  (endx,endy) = endxy
  return get_line(startx, starty, endx, endy, layer, thickness)


def print_dimensions():
  return [
    'PARAMETERS:',
    '',
    'dimensions:%.2fmm(W),%.2fmm(H)' % (width, height),
    'total_track_length:%.2fmm' % total_track_length,
    'heatbed_track_space:%.2fmm' % heatbed_track_space,
    'heatbed_track_width:%.2fmm' % heatbed_track_space,
    'track_bed_spacing_top:%.2fmm' % track_bed_spacing_top,
    'track_bed_spacing_bottom:%.2fmm' % track_bed_spacing_bottom,
    'track_bed_spacing_left:%.2fmm' % track_bed_spacing_left,
    'track_bed_spacing_right:%.2fmm' % track_bed_spacing_right,
  ]

def print_rating_at_temperature(temp_deg, track_width_mm, track_length_mm):
  track_resistance = get_track_resistance_at_temperature(temp_deg,track_width_mm,track_length_mm)
  power = get_power_consumption(12,track_resistance)
  current = 12/track_resistance

  return "RES@%0.2f_Deg:%0.2fOhms,POWER:%0.2fW,CURRENT:%0.2fA" % (temp_deg, track_resistance, power,current)


def print_power_rating():
  return [
    'RATING:',
    '',
    'VOLTAGE:%.2fV' % 12,
    print_rating_at_temperature(25, TRACK_WIDTH,total_track_length),
    print_rating_at_temperature(110, TRACK_WIDTH,total_track_length),
    print_rating_at_temperature(150, TRACK_WIDTH,total_track_length)
  ]

heatbed_surrounding=Template('''$HEAT_BED_OUTLINE'''.strip()
).substitute(
  HEAT_BED_OUTLINE='\n'.join([
    get_board_horizontal_line(board_top_left,board_top_right,LAYER_F_SilkS,0.1),
    get_board_horizontal_line(board_top_right,board_bottom_right,LAYER_F_SilkS,0.1),
    get_board_horizontal_line(board_bottom_right,board_bottom_left,LAYER_F_SilkS,0.1),
    get_board_horizontal_line(board_bottom_left,board_top_left,LAYER_F_SilkS,0.1)
  ])
)


heatbed_horizontal_tracks = add_horizontal_tracks(perform_scan_line())
heatbed_vertical_tracks = linking_lines_together(perform_scan_line())
heatbed_tracks = heatbed_vertical_tracks+heatbed_horizontal_tracks

heatbed_starting_point=(heatbed_tracks[0][0])
heatbed_ending_point=(heatbed_tracks[-1][0])

first_corner = (-60.96,track_start_top_left_lookup_from_x(-60.96))
second_corner = (track_start_top_left_lookup_from_y(-60.96),-63)

third_corner = (track_end_bottom_left_lookup_from_y(62), 62)
forth_corner = (-60.96, track_end_bottom_left_lookup_from_x(-60.96))

TERMINAL_1_CENTERXY=(-61, 18)
TERMINAL_2_CENTERXY=(-61, 40)

planned_tracks=[
  (TERMINAL_1_CENTERXY,first_corner),
  (first_corner, second_corner),
  (second_corner, heatbed_starting_point)
]+heatbed_tracks+[
  (heatbed_ending_point, third_corner),
  (third_corner, forth_corner),
  (forth_corner, TERMINAL_2_CENTERXY)
]

# print(draw_terrorties())

tracks = [get_track(planned_track[0],planned_track[1],LAYER_F_CU, TRACK_WIDTH) for planned_track in planned_tracks]

# pprint(tracks[0:3])
total_track_length = get_distances(planned_tracks)

f_kicad_footprint_file = open(DEST_FILE,'w')
f_kicad_footprint_file.write(
  heatbed_component_template.substitute(
  TRACKS='\n'.join(tracks),
  HEATBED_SURROUNDING=heatbed_surrounding,
  MOUNT_HOLE='\n'.join(get_mount_holes(5)),
  TERMINAL='\n'.join(get_terminals()),
  TERRORTIES='\n'.join(draw_terrorties()),
  BOILERPLATE=print_boiler_plate(
    print_power_rating()+['']+
    print_dimensions()
  ),
  MISC_TEXT=get_this_side_up_text(),
  MISC_COMPONENTS=get_led_and_resistors(),
  HOT_WARNING=get_hot_warnings(),
  CAUTION_TEXT=get_caution_text(),
  WATERMARK=get_watermark((-55,62), 'github.com/louiscklaw/kicad-heatbed-tryout')
  ),
)

print('done')
print('-'*80)
print('total track length %0.2fmm' % (total_track_length) )
