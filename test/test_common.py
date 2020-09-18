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
  result=common.get_bed_bottom_terrorties(10)
  assert 5==result, 'get get_bed_bottom_terrorties failed'

def test_get_bed_left_terrorties():
  result=common.get_bed_left_terrorties(10)
  assert -5==result, 'get get_bed_left_terrorties failed'

def test_get_bed_right_terrorties():
  result=common.get_bed_right_terrorties(10)
  assert 5==result, 'get get_bed_right_terrorties failed'

def test_get_bed_top_terrorties():
  result=common.get_bed_top_terrorties(10)
  assert -5==result, 'get get_bed_top_terrorties failed'

def test_get_distance():
  result = common.get_distance((0,0),(3,4))
  assert 5==result,'get get_distance failed'

def test_get_distances():
  result = common.get_distances([[(0,0),(3,4)],[(0,0),(3,4)],[(0,0),(3,4)]])
  assert 15==result,'get get_distances failed'

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
  result=common.get_track_bottom_terrorties(20)
  assert 5==result,'get get_track_bottom_terrorties failed'

def test_get_track_left_terrorties():
  result=common.get_track_left_terrorties(20)
  assert -5==result,'get get_track_left_terrorties failed'

def test_get_track_right_terrorties():
  result=common.get_track_right_terrorties(20)
  assert 5==result,'get get_track_right_terrorties failed'

def test_get_track_top_terrorties():
  result=common.get_track_top_terrorties(20)
  assert -5==result,'get get_track_top_terrorties failed'

def test_get_track_csa():
  pass

def test_get_track_resistance_at_temperature():
  pass

def test_helloworld():
  pass

def test_square_root():
  result=common.square_root(25)
  assert 5 == result, 'get square_root failed'

def test_square():
  result=common.square(5)
  assert 25 == result, 'get square failed'


def test():
  test_get_neg_x()
  test_get_neg_y()
  test_get_pos_x()
  test_get_pos_y()
  test_get_bed_bottom_left_corner()
  test_get_bed_bottom_right_corner()
  test_get_bed_top_left_corner()
  test_get_bed_top_right_corner()

  test_get_bed_bottom_terrorties()
  test_get_bed_left_terrorties()
  test_get_bed_right_terrorties()
  test_get_bed_top_terrorties()

  test_get_track_bottom_terrorties()
  test_get_track_left_terrorties()
  test_get_track_right_terrorties()
  test_get_track_top_terrorties()

  test_square()
  test_square_root()
  test_get_distance()
  test_get_distances()