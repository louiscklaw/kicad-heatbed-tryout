#!/usr/bin/env python3

import os,sys
import math

from pprint import pprint
from functools import reduce

from config import *

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

# TERRORTIES
def get_bed_top_terrorties(): return get_neg_y()
def get_bed_bottom_terrorties(): return get_pos_y()
def get_bed_left_terrorties(): return get_neg_x()
def get_bed_right_terrorties(): return get_pos_x()

def get_track_top_terrorties(): return    get_bed_top_terrorties() + track_bed_spacing_top
def get_track_bottom_terrorties(): return get_bed_bottom_terrorties() - track_bed_spacing_bottom
def get_track_left_terrorties(): return   get_bed_left_terrorties() + track_bed_spacing_left
def get_track_right_terrorties(): return  get_bed_right_terrorties() - track_bed_spacing_right

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
  return

def get_track_csa(width):
  return width*0.035

def get_track_resistance_at_temperature(in_temperature, width_mm, in_length_mm):
  in_length_m = in_length_mm/1000
  return (get_resistance_at_temperature(in_temperature) * (in_length_m/get_track_csa(width_mm)))

def get_power_consumption(voltage, resistance):
  return square(voltage) / resistance

def hello_common():
  print("hello common")
