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

def test():
  kicad_template.helloworld()

  test_this_side_up_text_template()
  test_heatbed_component_template()
  test_print_total_track_length()