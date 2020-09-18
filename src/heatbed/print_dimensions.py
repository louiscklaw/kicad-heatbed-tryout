import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

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
