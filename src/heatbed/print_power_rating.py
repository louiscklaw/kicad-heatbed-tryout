import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def print_power_rating():
  return [
    'RATING:',
    '',
    'VOLTAGE:%.2fV' % 12,
    print_rating_at_temperature(25, TRACK_WIDTH,total_track_length),
    print_rating_at_temperature(110, TRACK_WIDTH,total_track_length),
    print_rating_at_temperature(150, TRACK_WIDTH,total_track_length)
  ]
