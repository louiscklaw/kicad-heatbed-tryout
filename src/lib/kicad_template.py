import os,sys
from string import Template

SRC_LIB=os.path.dirname(__file__)
SRC_dir=os.path.abspath(SRC_LIB+'/..')
PROJ_HOME=os.path.abspath(SRC_dir+'/..')

K_TEMPLATE_DIR=os.path.abspath(SRC_dir+'/k_template')

sys.path.append(SRC_dir)
sys.path.append(K_TEMPLATE_DIR)

from common import *
from config import *

from this_side_up_text_template import *
from heatbed_component_template import *

from draw_terrorties import *
from get_bottom_territory import *
from get_caution_description import *
from get_caution_text import *
from get_caution_title import *
from get_front_leds import *
from get_hot_warnings import *
from get_led_and_resistors import *
from get_left_territory import *
from get_right_territory import *
from get_territory import *
from get_this_side_up_text import *
from get_top_territory import *
from get_watermark import *
from print_boiler_plate import *
from print_total_track_length import *

def helloworld():
  print('helloworld from {}'.format(__file__))
