import os,sys
from pprint import pprint
from string import Template

__BOILERPLATE=Template('''(fp_text user "$TEXT" (at $X_POS $Y_POS) (layer F.SilkS)(effects (font (size 1 1) (thickness 0.15))(justify left)))'''.strip())

def print_boiler_plate(in_texts):
  output = []
  starting_line_y=30
  starting_x = 10
  space_between_lines = 2

  y_positions = [starting_line_y + space_between_lines*idx for idx in range(0,len(in_texts))]

  for y_pos, in_text in zip(y_positions, in_texts):
    in_text=in_text.replace(' ','_')
    output.append(__BOILERPLATE.substitute(TEXT=in_text, Y_POS=y_pos, X_POS=starting_x))


  return '\n'.join(output)
