import os,sys
from pprint import pprint

import common

def test_get_bed_bottom_left_corner():
  result=common.get_bed_bottom_left_corner(20,20)
  assert (-10,10)==result, 'get get_bed_bottom_left_corner failed'

def test_get_bed_bottom_right_corner():
  result=common.get_bed_bottom_right_corner(20,20)
  assert (10,10)==result, 'get get_bed_bottom_right_corner failed'

def test_get_bed_top_left_corner():
  result=common.get_bed_top_left_corner(20,20)
  assert (-10,-10)==result, 'get get_bed_top_left_corner failed'

def test_get_bed_top_right_corner():
  result=common.get_bed_top_right_corner(20,20)
  assert (10,-10)==result, 'get get_bed_top_right_corner failed'

def test_get_bed_bottom_terrorties():
  pass

def test_get_bed_left_terrorties():
  pass

def test_get_bed_right_terrorties():
  pass

def test_get_bed_top_terrorties():
  pass

def test_get_distance():
  pass

def test_get_distances():
  pass

def test_get_half_height():
  pass

def test_get_half_width():
  pass

def test_get_heatbed_power():
  pass

def test_get_neg_x():
  assert -10==common.get_neg_x(20)


def test_get_neg_y():
  assert -10==common.get_neg_y(20)

def test_get_pos_x():
  assert 10==common.get_pos_x(20)

def test_get_pos_y():
  assert 10==common.get_pos_y(20)

def test_get_power_consumption():
  pass

def test_get_resistance_at_temperature():
  pass

def test_get_track_bottom_terrorties():
  pass

def test_get_track_csa():
  pass

def test_get_track_left_terrorties():
  pass

def test_get_track_resistance_at_temperature():
  pass

def test_get_track_right_terrorties():
  pass

def test_get_track_top_terrorties():
  pass

def test_helloworld():
  pass

def test_square_root():
  pass

def test_square():
  pass


def test():
  test_get_neg_x()
  test_get_neg_y()
  test_get_pos_x()
  test_get_pos_y()
  test_get_bed_bottom_left_corner()
  test_get_bed_bottom_right_corner()
  test_get_bed_top_left_corner()
  test_get_bed_top_right_corner()