import os,sys
from pprint import pprint

TEST_DIR=os.path.dirname(__file__)
PROJ_HOME=os.path.abspath(TEST_DIR+'/..')

SRC_DIR=os.path.abspath(PROJ_HOME+'/src')
SRC_HEATBED=os.path.abspath(SRC_DIR+'/heatbed')

sys.path.append(SRC_HEATBED)

from heatbed import *

def test_add_horizontal_tracks():
  result = add_horizontal_tracks(10)
  print(result)
  assert ''==result,'get add_horizontal_tracks failed'

def test_check_y_inside_bottom_left_mount_area():
  result = check_y_inside_bottom_left_mount_area(10)
  print(result)
  assert ''==result,'get check_y_inside_bottom_left_mount_area failed'

def test_check_y_inside_bottom_right_mount_area():
  result = check_y_inside_bottom_right_mount_area(10)
  print(result)
  assert ''==result,'get check_y_inside_bottom_right_mount_area failed'

def test_check_y_inside_top_left_mount_area():
  result = check_y_inside_top_left_mount_area(10)
  print(result)
  assert ''==result,'get check_y_inside_top_left_mount_area failed'

def test_check_y_inside_top_right_mount_area():
  result = check_y_inside_top_right_mount_area(10)
  print(result)
  assert ''==result,'get check_y_inside_top_right_mount_area failed'

def test_check_y_inside():
  result = check_y_inside(5,0,10)
  assert True==result,'get check_y_inside failed'

  result = check_y_inside(0,5,10)
  assert False==result,'get check_y_inside failed'


def test_frange():
  result = frange(1, 5, 1)
  assert [float(1),float(2),float(3),float(4)]==list(result),'get frange failed'

def test_get_board_horizontal_line():
  result = get_board_horizontal_line(10)
  print(result)
  assert ''==result,'get get_board_horizontal_line failed'

def test_get_line():
  result = get_line(10)
  print(result)
  assert ''==result,'get get_line failed'

def test_get_mount_hole():
  result = get_mount_hole(10)
  print(result)
  assert ''==result,'get get_mount_hole failed'

def test_get_mount_holes():
  result = get_mount_holes(10)
  print(result)
  assert ''==result,'get get_mount_holes failed'

def test_get_terminal_1():
  result = get_terminal_1(10)
  print(result)
  assert ''==result,'get get_terminal_1 failed'

def test_get_terminal_2():
  result = get_terminal_2(10)
  print(result)
  assert ''==result,'get get_terminal_2 failed'

def test_get_terminal_thru_hole():
  result = get_terminal_thru_hole(10)
  print(result)
  assert ''==result,'get get_terminal_thru_hole failed'

def test_get_terminal():
  result = get_terminal(10)
  print(result)
  assert ''==result,'get get_terminal failed'

def test_get_terminals():
  result = get_terminals(10)
  print(result)
  assert ''==result,'get get_terminals failed'

def test_get_track_start():
  result = get_track_start(10)
  print(result)
  assert ''==result,'get get_track_start failed'

def test_get_track():
  result = get_track(10)
  print(result)
  assert ''==result,'get get_track failed'

def test_is_even():
  result = is_even(10)
  print(result)
  assert ''==result,'get is_even failed'

def test_linking_lines_together():
  result = linking_lines_together(10)
  print(result)
  assert ''==result,'get linking_lines_together failed'

def test_lookup_bottom_left_corner():
  result = lookup_bottom_left_corner(10)
  print(result)
  assert ''==result,'get lookup_bottom_left_corner failed'

def test_lookup_bottom_right_corner():
  result = lookup_bottom_right_corner(10)
  print(result)
  assert ''==result,'get lookup_bottom_right_corner failed'

def test_lookup_left():
  result = lookup_left(10)
  print(result)
  assert ''==result,'get lookup_left failed'

def test_lookup_right():
  result = lookup_right(10)
  print(result)
  assert ''==result,'get lookup_right failed'

def test_lookup_top_left_corner():
  result = lookup_top_left_corner(10)
  print(result)
  assert ''==result,'get lookup_top_left_corner failed'

def test_lookup_top_right_corner():
  result = lookup_top_right_corner(10)
  print(result)
  assert ''==result,'get lookup_top_right_corner failed'

def test_perform_scan_line():
  result = perform_scan_line(10)
  print(result)
  assert ''==result,'get perform_scan_line failed'

def test_print_dimensions():
  result = print_dimensions(10)
  print(result)
  assert ''==result,'get print_dimensions failed'

def test_print_power_rating():
  result = print_power_rating(10)
  print(result)
  assert ''==result,'get print_power_rating failed'

def test_print_rating_at_temperature():
  result = print_rating_at_temperature(10)
  print(result)
  assert ''==result,'get print_rating_at_temperature failed'

def test_spread_from_center():
  result = spread_from_center(10)
  print(result)
  assert ''==result,'get spread_from_center failed'

def test_track_end_bottom_left_lookup_from_x():
  result = track_end_bottom_left_lookup_from_x(10)
  print(result)
  assert ''==result,'get track_end_bottom_left_lookup_from_x failed'

def test_track_end_bottom_left_lookup_from_y():
  result = track_end_bottom_left_lookup_from_y(10)
  print(result)
  assert ''==result,'get track_end_bottom_left_lookup_from_y failed'

def test_track_start_top_left_lookup_from_x():
  result = track_start_top_left_lookup_from_x(10)
  print(result)
  assert ''==result,'get track_start_top_left_lookup_from_x failed'

def test_track_start_top_left_lookup_from_y():
  result = track_start_top_left_lookup_from_y(10)
  print(result)
  assert ''==result,'get track_start_top_left_lookup_from_y failed'


def test():
  helloworld()

  test_check_y_inside()

  # test_add_horizontal_tracks()
  # test_check_y_inside_bottom_left_mount_area()
  # test_check_y_inside_bottom_right_mount_area()
  # test_check_y_inside_top_left_mount_area()
  # test_check_y_inside_top_right_mount_area()
  test_frange()
  # test_get_board_horizontal_line()
  # test_get_line()
  # test_get_mount_hole()
  # test_get_mount_holes()
  # test_get_terminal_1()
  # test_get_terminal_2()
  # test_get_terminal_thru_hole()
  # test_get_terminal()
  # test_get_terminals()
  # test_get_track_start()
  # test_get_track()
  # test_is_even()
  # test_linking_lines_together()
  # test_lookup_bottom_left_corner()
  # test_lookup_bottom_right_corner()
  # test_lookup_left()
  # test_lookup_right()
  # test_lookup_top_left_corner()
  # test_lookup_top_right_corner()
  # test_perform_scan_line()
  # test_print_dimensions()
  # test_print_power_rating()
  # test_print_rating_at_temperature()
  # test_spread_from_center()
  # test_track_end_bottom_left_lookup_from_x()
  # test_track_end_bottom_left_lookup_from_y()
  # test_track_start_top_left_lookup_from_x()
  # test_track_start_top_left_lookup_from_y()