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


# tracks=[]

# top_left_mount_start = get_bed_top_left_corner()[1]+top_left_corner_space
# bottom_left_mount_start = get_bed_bottom_left_corner()[1]-bottom_left_corner_space
# top_right_mount_start = get_bed_top_right_corner()[1]+top_right_corner_space
# bottom_right_mount_start = get_bed_bottom_right_corner()[1]-bottom_right_corner_space


# board_top_left = (get_neg_x(),get_neg_y())
# board_top_right = (get_pos_x(),get_neg_y())
# board_bottom_left = (get_neg_x(),get_pos_y())
# board_bottom_right = (get_pos_x(),get_pos_y())




# heatbed_surrounding=Template('''$HEAT_BED_OUTLINE'''.strip()
# ).substitute(
#   HEAT_BED_OUTLINE='\n'.join([
#     get_board_horizontal_line(board_top_left,board_top_right,LAYER_F_SilkS,0.1),
#     get_board_horizontal_line(board_top_right,board_bottom_right,LAYER_F_SilkS,0.1),
#     get_board_horizontal_line(board_bottom_right,board_bottom_left,LAYER_F_SilkS,0.1),
#     get_board_horizontal_line(board_bottom_left,board_top_left,LAYER_F_SilkS,0.1)
#   ])
# )


# heatbed_horizontal_tracks = add_horizontal_tracks(perform_scan_line())
# heatbed_vertical_tracks = linking_lines_together(perform_scan_line())
# heatbed_tracks = heatbed_vertical_tracks+heatbed_horizontal_tracks

# heatbed_starting_point=(heatbed_tracks[0][0])
# heatbed_ending_point=(heatbed_tracks[-1][0])

# first_corner = (-60.96,track_start_top_left_lookup_from_x(-60.96))
# second_corner = (track_start_top_left_lookup_from_y(-60.96),-63)

# third_corner = (track_end_bottom_left_lookup_from_y(62), 62)
# forth_corner = (-60.96, track_end_bottom_left_lookup_from_x(-60.96))

# TERMINAL_1_CENTERXY=(-61, 18)
# TERMINAL_2_CENTERXY=(-61, 40)

# planned_tracks=[
#   (TERMINAL_1_CENTERXY,first_corner),
#   (first_corner, second_corner),
#   (second_corner, heatbed_starting_point)
# ]+heatbed_tracks+[
#   (heatbed_ending_point, third_corner),
#   (third_corner, forth_corner),
#   (forth_corner, TERMINAL_2_CENTERXY)
# ]

# # print(draw_terrorties())

# tracks = [get_track(planned_track[0],planned_track[1],LAYER_F_CU, TRACK_WIDTH) for planned_track in planned_tracks]

# # pprint(tracks[0:3])
# total_track_length = get_distances(planned_tracks)

# f_kicad_footprint_file = open(DEST_FILE,'w')
# f_kicad_footprint_file.write(
#   heatbed_component_template.substitute(
#   TRACKS='\n'.join(tracks),
#   HEATBED_SURROUNDING=heatbed_surrounding,
#   MOUNT_HOLE='\n'.join(get_mount_holes(5)),
#   TERMINAL='\n'.join(get_terminals()),
#   TERRORTIES='\n'.join(draw_terrorties()),
#   BOILERPLATE=print_boiler_plate(
#     print_power_rating()+['']+
#     print_dimensions()
#   ),
#   MISC_TEXT=get_this_side_up_text(),
#   MISC_COMPONENTS=get_led_and_resistors(),
#   HOT_WARNING=get_hot_warnings(),
#   CAUTION_TEXT=get_caution_text(),
#   WATERMARK=get_watermark((-55,62), 'github.com/louiscklaw/kicad-heatbed-tryout')
#   ),
# )

# print('done')
# print('-'*80)
# print('total track length %0.2fmm' % (total_track_length) )


def helloworld():
  print('helloworld from {}'.format(__file__))
