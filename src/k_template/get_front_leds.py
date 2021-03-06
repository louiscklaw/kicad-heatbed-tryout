import os,sys
from pprint import pprint
from string import Template

K_TEMPLATE_DIR=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(K_TEMPLATE_DIR+'/..')

sys.path.append(SRC_DIR)

def get_front_leds():
  return '''
# Front left led
(pad 1 smd roundrect (at 61.4625 44.7) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(pad 2 smd roundrect (at 63.3375 44.7) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(fp_text user %R (at 62.5 -44.7 180) (layer B.Fab)
  (effects (font (size 0.5 0.5) (thickness 0.08)))
)
(fp_line (start 62.6 -44.8) (end 62.5 -44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.6 -44.4) (end 62.6 -44.8) (layer B.SilkS) (width 0.12))
(fp_line (start 62.4 -44.7) (end 62.6 -44.4) (layer B.SilkS) (width 0.12))
(fp_line (start 62.7 -45) (end 62.4 -44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.7 -44.4) (end 62.7 -45) (layer B.SilkS) (width 0.12))
(fp_line (start 62.75 -44.2) (end 62.7 -44.4) (layer B.SilkS) (width 0.12))
(fp_line (start 62.25 -44.7) (end 62.75 -44.2) (layer B.SilkS) (width 0.12))
(fp_line (start 62.75 -45.2) (end 62.25 -44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.75 -44.2) (end 62.75 -45.2) (layer B.SilkS) (width 0.12))
(fp_line (start 64.185 -43.74) (end 64.185 -45.66) (layer B.SilkS) (width 0.12))
(fp_line (start 61.5 -44.1) (end 63.2 -44.1) (layer B.Fab) (width 0.1))
(fp_line (start 63.2 -44.1) (end 63.5 -44.4) (layer B.Fab) (width 0.1))
(fp_line (start 61.5 -45.3) (end 61.5 -44.1) (layer B.Fab) (width 0.1))
(fp_line (start 63.5 -45.3) (end 61.5 -45.3) (layer B.Fab) (width 0.1))
(fp_line (start 60.82 -45.65) (end 64.18 -45.65) (layer F.CrtYd) (width 0.05))
(fp_line (start 60.82 -43.75) (end 60.82 -45.65) (layer F.CrtYd) (width 0.05))
(fp_line (start 63.5 -44.4) (end 63.5 -45.3) (layer B.Fab) (width 0.1))
(fp_line (start 64.185 -45.66) (end 61.5 -45.66) (layer B.SilkS) (width 0.12))
(fp_line (start 62.5 -44.7) (end 62.6 -44.6) (layer B.SilkS) (width 0.12))
(fp_line (start 64.18 -43.75) (end 60.82 -43.75) (layer F.CrtYd) (width 0.05))
(fp_line (start 64.18 -45.65) (end 64.18 -43.75) (layer F.CrtYd) (width 0.05))
(fp_line (start 61.5 -43.74) (end 64.185 -43.74) (layer B.SilkS) (width 0.12))


# Front Right led
(pad 2 smd roundrect (at 61.555 -44.7 180) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(pad 1 smd roundrect (at 63.43 -44.7 180) (size 0.975 1.4) (layers B.Cu B.Paste B.Mask) (roundrect_rratio 0.25))
(fp_line (start 63.4 43.74) (end 60.715 43.74) (layer B.SilkS) (width 0.12))
(fp_line (start 60.72 45.65) (end 60.72 43.75) (layer F.CrtYd) (width 0.05))
(fp_line (start 60.72 43.75) (end 64.08 43.75) (layer F.CrtYd) (width 0.05))
(fp_text user %R (at 62.4 44.7) (layer B.Fab)
  (effects (font (size 0.5 0.5) (thickness 0.08)))
)
(fp_line (start 60.715 45.66) (end 63.4 45.66) (layer B.SilkS) (width 0.12))
(fp_line (start 61.4 44.4) (end 61.4 45.3) (layer B.Fab) (width 0.1))
(fp_line (start 64.08 43.75) (end 64.08 45.65) (layer F.CrtYd) (width 0.05))
(fp_line (start 64.08 45.65) (end 60.72 45.65) (layer F.CrtYd) (width 0.05))
(fp_line (start 61.4 45.3) (end 63.4 45.3) (layer B.Fab) (width 0.1))
(fp_line (start 63.4 45.3) (end 63.4 44.1) (layer B.Fab) (width 0.1))
(fp_line (start 61.7 44.1) (end 61.4 44.4) (layer B.Fab) (width 0.1))
(fp_line (start 63.4 44.1) (end 61.7 44.1) (layer B.Fab) (width 0.1))
(fp_line (start 60.715 43.74) (end 60.715 45.66) (layer B.SilkS) (width 0.12))
(fp_line (start 62.15 44.2) (end 62.15 45.2) (layer B.SilkS) (width 0.12))
(fp_line (start 62.15 45.2) (end 62.65 44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.65 44.7) (end 62.15 44.2) (layer B.SilkS) (width 0.12))
(fp_line (start 62.15 44.2) (end 62.2 44.4) (layer B.SilkS) (width 0.12))
(fp_line (start 62.2 44.4) (end 62.2 45) (layer B.SilkS) (width 0.12))
(fp_line (start 62.2 45) (end 62.5 44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.5 44.7) (end 62.3 44.4) (layer B.SilkS) (width 0.12))
(fp_line (start 62.3 44.4) (end 62.3 44.8) (layer B.SilkS) (width 0.12))
(fp_line (start 62.3 44.8) (end 62.4 44.7) (layer B.SilkS) (width 0.12))
(fp_line (start 62.4 44.7) (end 62.3 44.6) (layer B.SilkS) (width 0.12))


(fp_line (start 61.5 44.7) (end 61.6 -44.7) (layer B.Cu) (width 0.5))
(fp_line (start 63.4 44.7) (end 63.4 -44.7) (layer B.Cu) (width 0.5))
# (fp_line (start 62.6 45.3) (end 62 44.7) (layer B.Cu) (width 0.5))
# (fp_line (start 62 44.7) (end 62.1 -44.2) (layer B.Cu) (width 0.5))
# (fp_line (start 62.1 -44) (end 63.6 -45.3) (layer B.Cu) (width 0.5))

# Track to front leds
(fp_line (start 61.5 44.7) (end 61.5 46) (layer B.Cu) (width 0.5))
(fp_line (start 61.5 46) (end 61.1 46.5) (layer B.Cu) (width 0.5))
(fp_line (start 61.1 46.5) (end -53.1 46.5) (layer B.Cu) (width 0.5))
(fp_line (start -53.1 46.5) (end -53.6 46) (layer B.Cu) (width 0.5))
(fp_line (start -53.6 46) (end -53.6 24.8) (layer B.Cu) (width 0.5))
(fp_line (start -53.6 24.8) (end -54.7 24) (layer B.Cu) (width 0.5))
(fp_line (start -54.7 24) (end -59.5 24) (layer B.Cu) (width 0.5))

(fp_line (start -55.3 46) (end -55.3 34.4) (layer B.Cu) (width 0.5))
(fp_line (start -55.3 34.4) (end -54.6 33.6) (layer B.Cu) (width 0.5))
(fp_line (start -54.6 33.6) (end -54.6 27.8) (layer B.Cu) (width 0.5))
(fp_line (start -54.6 27.8) (end -55.1 27.2) (layer B.Cu) (width 0.5))
(fp_line (start -55.1 27.2) (end -56.8 27.2) (layer B.Cu) (width 0.5))
(fp_line (start -56.8 27.2) (end -57.4 27.9) (layer B.Cu) (width 0.5))
(fp_line (start -57.4 27.9) (end -57.4 29.5) (layer B.Cu) (width 0.5))
(fp_line (start 63.4 44.7) (end 63.4 46.3) (layer B.Cu) (width 0.5))
(fp_line (start 63.4 46.3) (end 61.9 48) (layer B.Cu) (width 0.5))
(fp_line (start 61.9 48) (end -53.4 48) (layer B.Cu) (width 0.5))
(fp_line (start -53.4 48) (end -55.3 46) (layer B.Cu) (width 0.5))
'''.strip()
