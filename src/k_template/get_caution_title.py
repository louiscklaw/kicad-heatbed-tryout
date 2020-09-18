import os,sys
from pprint import pprint
from string import Template

K_TEMPLATE_DIR=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(K_TEMPLATE_DIR+'/..')

sys.path.append(SRC_DIR)

def get_caution_title(leftxy, text):
  leftx, lefty= leftxy
  return '''
(fp_text user "{}" (at {} {}) (layer F.SilkS)
  (effects (font (size 3 3) (thickness 0.3)) (justify left))
)
  '''.format(text, leftx, lefty).strip()
