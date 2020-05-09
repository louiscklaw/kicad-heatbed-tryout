#!/usr/bin/env python3
import os,sys
from pprint import pprint

corner_top_valid_y = (-7,-10)
corner_bottom_valid_y = (7,10)
ramp_line_c = 17
corner_space = 3

tracks=[]

def check_y_inside(y, in_min, in_max):
  return y >= in_min and y <= in_max

def lookup_left(y):
  if check_y_inside(y, -7,7):
    return -10
  elif check_y_inside(y, -10,-7):
    return lookup_top_left_corner(y)
  elif check_y_inside(y, 7, 10):
    return lookup_bottom_left_corner(y)
  else:
    return -1

def lookup_right(y):
  if check_y_inside(y, -7,7):
    return 10
  elif check_y_inside(y, -10,-7):
    return lookup_top_right_corner(y)
  elif check_y_inside(y, 7, 10):
    return lookup_bottom_right_corner(y)
  else:
    return -1

def lookup_top_left_corner(y):
  '''y=-x+c'''
  '''y=-x+ramp_line_c'''
  return -y-ramp_line_c

def lookup_bottom_left_corner(y):
  '''y=x+c'''
  '''y=x+ramp_line_c'''
  return y-ramp_line_c

def lookup_top_right_corner(y):
  '''y=x-c'''
  return y+ramp_line_c

def lookup_bottom_right_corner(y):
  '''y=x-c'''
  return -y+ramp_line_c

def is_even(y):
  return y % 2

def linking_lines_together(point_array):
  tracks=[]
  for idx in range(0,len(point_array)):
    y, leftx,rightx = point_array[idx]
    tracks.append(((leftx, y ), (rightx, y)))

  for idx in range(0,len(point_array)-1):
    next_idx = idx+1
    y, leftx,rightx = point_array[idx]
    next_y, next_leftx,next_rightx = point_array[next_idx]
    if is_even(idx):
      tracks.append(((rightx,y), (next_rightx, next_y)))
    else:
      tracks.append(((leftx,y), (next_leftx,next_y)))

  return tracks

def perform_scan_line():
  point_list=[]

  # scan line algorithm
  for i in range(-10,10+1):
    point_list.append((i, lookup_left(i),lookup_right(i)))

  return point_list

print(linking_lines_together(perform_scan_line()))

print('helloworld')
