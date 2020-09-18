import os,sys
from pprint import pprint

SRC_HEATBED=os.path.abspath(__file__)
SRC_DIR=os.path.abspath(SRC_HEATBED+'/..')

sys.path.append(SRC_DIR)

def print_rating_at_temperature(temp_deg, track_width_mm, track_length_mm):
  track_resistance = get_track_resistance_at_temperature(temp_deg,track_width_mm,track_length_mm)
  power = get_power_consumption(12,track_resistance)
  current = 12/track_resistance

  return "RES@%0.2f_Deg:%0.2fOhms,POWER:%0.2fW,CURRENT:%0.2fA" % (temp_deg, track_resistance, power,current)
