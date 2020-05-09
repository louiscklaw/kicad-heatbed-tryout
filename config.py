import os,sys

# bed width and height
width=130
height=130

# define the distance between the corner point for mount hole
corner_space = 17
top_left_corner_space = 22
top_right_corner_space = corner_space
bottom_left_corner_space = corner_space
bottom_right_corner_space = corner_space

heatbed_track_space=5

# the space between bed and the track
track_bed_spacing = 5

track_bed_spacing_top = 2
track_bed_spacing_bottom = 2
track_bed_spacing_left = 8
track_bed_spacing_right = 2


ramp_line_c = (height/2)+(height/2)-corner_space

spacing_for_start_track=5
ramp_line_left = ramp_line_c-spacing_for_start_track
ramp_line_right = ramp_line_c

track_start_corner_space=ramp_line_left+5


DEST_FILE = '/home/logic/_workspace/kicad_workspace/kicad/kicad_library/kicad-footprints/footprint-lib.pretty/130_130_heatbed-route.kicad_mod'

LAYER_F_SilkS='F.SilkS'
LAYER_F_CU='F.Cu'

TRACK_THICK=1
TRACK_SPACING=3
INTER_TRACK_SPACING=3
INTER_TRACK_X_START_OFFSET=1

COL_LEFT_X=0
COL_LEFT_Y=1
COL_RIGHT_X=2
COL_RIGHT_Y=3
COL_LAYER=4
COL_THICKNESS=5

MOUNT_HOLE_CLEARANCE=5
