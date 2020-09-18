import os,sys
from pprint import pprint
from string import Template

K_TEMPLATE_DIR=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(K_TEMPLATE_DIR+'/..')

sys.path.append(SRC_DIR)

from get_front_leds import *

def get_led_and_resistors():
  return '''
# LED1
#(pad 1 smd roundrect (at -61.9375 27.75) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))
#(pad R1 smd roundrect (at -60.0625 27.75) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))

# 1 TO LED 1
(fp_line (start -62 27.75) (end -62 26.5) (layer B.Cu) (width 0.3))
(fp_line (start -62 26.5) (end -61.75 26.25) (layer B.Cu) (width 0.3))
(fp_line (start -61.75 26.25) (end -61.25 26.25) (layer B.Cu) (width 0.3))
(fp_line (start -61.25 26.25) (end -61 26) (layer B.Cu) (width 0.3))
(fp_line (start -61 26) (end -61 25) (layer B.Cu) (width 0.3))

# LED to R1
(fp_line (start -62 27.7) (end -62 30.3) (layer B.Cu) (width 0.5))
(fp_line (start -60.1 27.7) (end -60.1 30.2) (layer B.Cu) (width 0.5))
(fp_line (start -60.1 30.2) (end -58.8 30.2) (layer B.Cu) (width 0.5))
(fp_line (start -58.8 30.2) (end -58.6 30) (layer B.Cu) (width 0.5))
(fp_line (start -58.6 30) (end -58.6 29.7) (layer B.Cu) (width 0.5))
(fp_line (start -58.6 29.7) (end -58.4 29.5) (layer B.Cu) (width 0.5))
(fp_line (start -58.4 29.5) (end -57.8 29.5) (layer B.Cu) (width 0.5))
(fp_line (start -55.9 29.5) (end -55.9 33.5) (layer B.Cu) (width 0.5))
(fp_line (start -55.9 33.5) (end -56.2 33.8) (layer B.Cu) (width 0.5))
(fp_line (start -56.2 33.8) (end -59.5 33.8) (layer B.Cu) (width 0.5))

#LED1
(pad 1 smd roundrect (at -61.9375 27.75) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))
(pad R1 smd roundrect (at -60.0625 27.75) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))

#R1
(pad R1 smd roundrect (at -57.7375 29.55 180) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))
(pad 2 smd roundrect (at -55.8625 29.55 180) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))

#LED2
(pad 1 smd roundrect (at -61.9375 30.25 180) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))
(pad R1 smd roundrect (at -60.0625 30.25 180) (size 0.975 1.4) (layers B.Cu B.Mask) (roundrect_rratio 0.25))

{}
'''.format(
  get_front_leds()
).strip()
