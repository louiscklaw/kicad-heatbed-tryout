import os,sys
from string import Template

SRC_LIB=os.path.dirname(__file__)
SRC_dir=os.path.abspath(SRC_LIB+'/..')
PROJ_HOME=os.path.abspath(SRC_dir+'/..')

K_TEMPLATE_DIR=os.path.abspath(SRC_dir+'/k_template')

sys.path.append(SRC_dir)
sys.path.append(K_TEMPLATE_DIR)

def get_watermark(leftxy, github_link):
  leftx, lefty= leftxy
  watermark_template=Template('''
(fp_text user "$TEXT" (at $LEFTX $LEFTY) (layer B.SilkS)
  (effects (font (size 1 1) (thickness 0.15)) (justify right mirror))
)
(fp_text user "$TEXT" (at $LEFTX $LEFTY) (layer F.SilkS)
  (effects (font (size 1 1) (thickness 0.15)) (justify left))
)
  ''')

  return watermark_template.substitute(
    LEFTX=leftx,
    LEFTY=lefty,
    TEXT=github_link
  ).format(leftx, lefty, github_link).strip()
