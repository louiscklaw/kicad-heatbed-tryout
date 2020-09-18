import os,sys
from string import Template

heatbed_component_template = Template('''
(module 130_130_heatbed-route (layer F.Cu) (tedit 5EB4FE57)
  (fp_text reference REF** (at 0 21.844) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value 130_130_heatbed-route (at 0 19.304) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )

$TRACKS

$HEATBED_SURROUNDING

$MOUNT_HOLE

$TERMINAL

$BOILERPLATE

$TERRORTIES

$MISC_TEXT

$MISC_COMPONENTS

$HOT_WARNING

$CAUTION_TEXT

$WATERMARK
)
'''.strip())
