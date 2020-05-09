#!/usr/bin/env python3

import os,sys
import math

from pprint import pprint
from functools import reduce

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

def hello_common():
  print("hello common")
