import os,sys
from string import Template

this_side_up_text_template = Template('''
(fp_text user "$TEXT" (at $CENTERX $CENTERY) (layer F.SilkS)
(effects (font (size 3 3) (thickness 0.3)) (justify left)))
'''.strip())
