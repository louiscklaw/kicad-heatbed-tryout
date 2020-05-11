#!/usr/bin/env python3

import os,sys
from pprint import pprint

from common import *

def value_is_around(test_value, expected_value, margin=0.0001):
  return abs(test_value-expected_value) < margin

def test_get_resistance_at_temperature():
  assert(value_is_around(get_resistance_at_temperature(110), 0.022768))
  assert(get_resistance_at_temperature(25)==0.0171)

def test_get_track_csa():
  assert(value_is_around(get_track_csa(0.8), 0.028))

def test_get_track_resistance_at_temperature():
  assert(value_is_around(get_track_resistance_at_temperature(25,0.8,3520), 2.1, 0.1))
  assert(value_is_around(get_track_resistance_at_temperature(110,0.8,3520), 2.8, 0.1))
  assert(value_is_around(get_track_resistance_at_temperature(150,0.8,3520), 3.1, 0.1))

def test_get_power_consumption():
  assert(value_is_around(get_power_consumption(12,2.15),66.9, 0.1))
  assert(value_is_around(get_power_consumption(12,2.86),50.3, 0.1))
  assert(value_is_around(get_power_consumption(12,3.1977),45.03, 0.1))

def test_list():
  test_get_resistance_at_temperature()
  test_get_track_csa()
  test_get_track_resistance_at_temperature()
  test_get_power_consumption()

if __name__ == '__main__':
  test_list()