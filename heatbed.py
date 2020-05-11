#!/usr/bin/env python3

import os,sys
from pprint import pprint
from string import Template

from config import *
from kicad_template import *
from common import *


tracks=[]

def get_neg_x(): return -(width/2)
def get_pos_x(): return (width/2)
def get_neg_y(): return -(height/2)
def get_pos_y(): return (height/2)

def get_bed_top_left_corner(): return (get_neg_x(), get_neg_y())
def get_bed_top_right_corner(): return (get_pos_x(), get_neg_y())
def get_bed_bottom_left_corner(): return (get_neg_x(), get_pos_y())
def get_bed_bottom_right_corner(): return (get_pos_x(), get_pos_y())
def get_half_height(): return height/2
def get_half_width(): return width/2

def get_bed_top_terrorties(): return get_neg_y()
def get_bed_bottom_terrorties(): return get_pos_y()
def get_bed_left_terrorties(): return get_neg_x()
def get_bed_right_terrorties(): return get_pos_x()

def get_track_top_terrorties(): return    get_bed_top_terrorties() + track_bed_spacing_top
def get_track_bottom_terrorties(): return get_bed_bottom_terrorties() - track_bed_spacing_bottom
def get_track_left_terrorties(): return   get_bed_left_terrorties() + track_bed_spacing_left
def get_track_right_terrorties(): return  get_bed_right_terrorties() - track_bed_spacing_right


top_left_mount_start = get_bed_top_left_corner()[1]+top_left_corner_space
bottom_left_mount_start = get_bed_bottom_left_corner()[1]-bottom_left_corner_space
top_right_mount_start = get_bed_top_right_corner()[1]+top_right_corner_space
bottom_right_mount_start = get_bed_bottom_right_corner()[1]-bottom_right_corner_space


def frange(start, stop=None, step=None):
    # if stop and step argument is None set start=0.0 and step = 1.0
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0

    # print("start= ", start, "stop= ", stop, "step= ", step)

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1

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

  print(get_track_bottom_terrorties())
  # sys.exit()

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
def get_terminal(centerxy, pad_num):
  centerx, centery = centerxy
  return Template('(pad $PAD_NUM thru_hole roundrect (at $CENTERX $CENTERY) (size 5 10) (drill 3) (layers *.Cu *.Mask) (roundrect_rratio 0.25))').substitute(
    CENTERX=centerx, CENTERY=centery, PAD_NUM=pad_num
  )

def get_terminals():
  return [get_terminal((-60.96, 32.004), 1), get_terminal((-60.96, 45.212), 2)]

def get_board_horizontal_line(startxy, endxy, layer, thickness):
  (startx, starty) = startxy
  (endx,endy) = endxy
  return get_line(startx, starty, endx, endy, layer, thickness)

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

terminal_1=(-60.96, 32.004)
terminal_2=(-60.96, 45.212)

planned_tracks=[
  (terminal_1,first_corner),
  (first_corner, second_corner),
  (second_corner, heatbed_starting_point)
]+heatbed_tracks+[
  (heatbed_ending_point, third_corner),
  (third_corner, forth_corner),
  (forth_corner, terminal_2)
]



tracks = [get_track(planned_track[0],planned_track[1],LAYER_F_CU, TRACK_THICK) for planned_track in planned_tracks]

# pprint(tracks[0:3])
total_track_length = get_distances(planned_tracks)

f_kicad_footprint_file = open(DEST_FILE,'w')
f_kicad_footprint_file.write(
  heatbed_component_template.substitute(
  TRACKS='\n'.join(tracks),
  HEATBED_SURROUNDING=heatbed_surrounding,
  MOUNT_HOLE='\n'.join(get_mount_holes(5)),
  TERMINAL='\n'.join(get_terminals()),
  TOTAL_TRACK_LENGTH=print_total_track_length('TOTAL_LENGTH=%0.2fmm' % (total_track_length))
  ),
)

print('done')
print('-'*80)
print('total track length %0.2fmm' % (total_track_length) )
