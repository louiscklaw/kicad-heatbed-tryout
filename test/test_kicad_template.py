import os,sys
from pprint import pprint
from string import Template

import kicad_template

def test_this_side_up_text_template():
  result=kicad_template.this_side_up_text_template
  result=type(result)
  assert type(Template(''))==result,'get this_side_up_text_template failed'

def test_heatbed_component_template():
  result=kicad_template.heatbed_component_template
  result=type(result)
  assert type(Template(''))==result,'get heatbed_component_template failed'

def test_print_total_track_length():
  result=kicad_template.print_total_track_length(10)
  assert ''!=result,'get print_total_track_length failed'

def test_draw_terrorties():
  result=kicad_template.draw_terrorties(50,50)
  assert ''!=result, 'get test_draw_terrorties failed'

def test_get_bottom_territory():
  result=kicad_template.get_bottom_territory(10, 10)
  assert ''!=result, 'get test_get_bottom_territory failed'

def test_get_caution_description():
  result=kicad_template.get_caution_description((10,10), 'test caution')
  assert ''!=result, 'get test_get_caution_description failed'

def test_get_caution_text():
  result=kicad_template.get_caution_text(10)
  print(result)
  assert ''==result, 'get test_get_caution_text failed'

def test_get_caution_title():
  result=kicad_template.get_caution_title(10)
  print(result)
  assert ''==result, 'get test_get_caution_title failed'

def test_get_front_leds():
  result=kicad_template.get_front_leds(10)
  print(result)
  assert ''==result, 'get test_get_front_leds failed'

def test_get_hot_warnings():
  result=kicad_template.get_hot_warnings(10)
  print(result)
  assert ''==result, 'get test_get_hot_warnings failed'

def test_get_led_and_resistors():
  result=kicad_template.get_led_and_resistors(10)
  print(result)
  assert ''==result, 'get test_get_led_and_resistors failed'

def test_get_left_territory():
  result=kicad_template.get_left_territory(10)
  print(result)
  assert ''==result, 'get test_get_left_territory failed'

def test_get_right_territory():
  result=kicad_template.get_right_territory(10)
  print(result)
  assert ''==result, 'get test_get_right_territory failed'

def test_get_territory():
  result=kicad_template.get_territory(10)
  print(result)
  assert ''==result, 'get test_get_territory failed'

def test_get_this_side_up_text():
  result=kicad_template.get_this_side_up_text(10)
  print(result)
  assert ''==result, 'get test_get_this_side_up_text failed'

def test_get_top_territory():
  result=kicad_template.get_top_territory(10)
  print(result)
  assert ''==result, 'get test_get_top_territory failed'

def test_get_watermark():
  result=kicad_template.get_watermark(10)
  print(result)
  assert ''==result, 'get test_get_watermark failed'

def test_print_boiler_plate():
  result=kicad_template.print_boiler_plate(10)
  print(result)
  assert ''==result, 'get test_print_boiler_plate failed'


def test():
  kicad_template.helloworld()

  test_this_side_up_text_template()
  test_heatbed_component_template()
  test_print_total_track_length()

  test_draw_terrorties()
  test_get_bottom_territory()
  test_get_caution_description()
  # test_get_caution_text()
  # test_get_caution_title()
  # test_get_front_leds()
  # test_get_hot_warnings()
  # test_get_led_and_resistors()
  # test_get_left_territory()
  # test_get_right_territory()
  # test_get_territory()
  # test_get_this_side_up_text()
  # test_get_top_territory()
  # test_get_watermark()
  # test_print_boiler_plate()
