import os,sys
from pprint import pprint


SRC_DIR=os.path.dirname(__file__)
PROJ_HOME=os.path.abspath(SRC_DIR+'/..')
SRC_HEATBED=os.path.abspath(SRC_DIR+'/heatbed')

sys.path.append(SRC_DIR)

from check_y_inside import *
from check_y_inside_bottom_left_mount_area import *
from check_y_inside_bottom_right_mount_area import *
from check_y_inside_top_left_mount_area import *
from check_y_inside_top_right_mount_area import *
from frange import *
from get_board_horizontal_line import *
from get_line import *
from get_mount_hole import *
from get_mount_holes import *
from get_terminal import *
from get_terminal_1 import *
from get_terminal_2 import *
from get_terminal_thru_hole import *
from get_terminals import *
from get_track import *
from get_track_start import *
from heatbed import *
from is_even import *
from linking_lines_together import *
from lookup_bottom_left_corner import *
from lookup_bottom_right_corner import *
from lookup_left import *
from lookup_right import *
from lookup_top_left_corner import *
from lookup_top_right_corner import *
from perform_scan_line import *
from print_dimensions import *
from print_power_rating import *
from print_rating_at_temperature import *
from spread_from_center import *
from track_end_bottom_left_lookup_from_x import *
from track_end_bottom_left_lookup_from_y import *
from track_start_top_left_lookup_from_x import *
from track_start_top_left_lookup_from_y import *

def helloworld():
  print('helloworld from {}'.format(__file__))
