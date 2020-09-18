import os,sys
from pprint import pprint

import math
from functools import reduce

def get_neg_x(width): return -(width/2)
def get_pos_x(width): return (width/2)
def get_neg_y(height): return -(height/2)
def get_pos_y(height): return (height/2)

def get_bed_top_left_corner(width, height): return (get_neg_x(width), get_neg_y(height))
def get_bed_top_right_corner(width, height): return (get_pos_x(width), get_neg_y(height))
def get_bed_bottom_left_corner(width, height): return (get_neg_x(width), get_pos_y(height))
def get_bed_bottom_right_corner(width, height): return (get_pos_x(width), get_pos_y(height))
def get_half_height(): return height/2
def get_half_width(): return width/2

# TERRORTIES
def get_bed_top_terrorties(height): return get_neg_y(height)
def get_bed_bottom_terrorties(height): return get_pos_y(height)
def get_bed_left_terrorties(width): return get_neg_x(width)
def get_bed_right_terrorties(width): return get_pos_x(width)

def get_track_top_terrorties(height, track_bed_spacing_top=5): return    get_bed_top_terrorties(height) + track_bed_spacing_top
def get_track_bottom_terrorties(height, track_bed_spacing_bottom=5): return get_bed_bottom_terrorties(height) - track_bed_spacing_bottom
def get_track_left_terrorties(width, track_bed_spacing_left=5): return   get_bed_left_terrorties(width) + track_bed_spacing_left
def get_track_right_terrorties(width, track_bed_spacing_right=5): return  get_bed_right_terrorties(width) - track_bed_spacing_right

def square(num):
  return math.pow(num, 2)

def square_root(num):
  return math.sqrt(num)

def get_distance(startxy, endxy):
  startx, starty = startxy
  endx, endy = endxy
  return square_root(square((endy-starty)) + square((endx-startx)))

def get_distances(point_arrays):
  lengths = [get_distance(startxy, endxy) for startxy, endxy in point_arrays]
  total_lengths = reduce(lambda a,b: a+b, lengths)
  return total_lengths

def get_resistance_at_temperature(in_temperature):
  return 0.0171*(1+0.0039*(in_temperature-25))

def get_heatbed_power(length, width):
  # TODO: implement me
  return

def get_track_csa(width):
  return width*0.035

def get_track_resistance_at_temperature(in_temperature, width_mm, in_length_mm):
  in_length_m = in_length_mm/1000
  return (get_resistance_at_temperature(in_temperature) * (in_length_m/get_track_csa(width_mm)))

def get_power_consumption(voltage, resistance):
  return square(voltage) / resistance

def helloworld():
  print('helloworld from {}'.format(__file__))
