
def frange(start, stop=None, step=None):
    # if stop and step argument is None set start=0.0 and step = 1.0
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0

    # print("start= ", start, "stop= ", stop, "step= ", step)

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1

def check_y_inside(y, in_min, in_max):
  return y >= in_min and y <= in_max

def linking_lines_together(point_array):
  tracks=[]
  for idx in range(0,len(point_array)):
    y, leftx,rightx = point_array[idx]
    tracks.append(((leftx, y ), (rightx, y)))

  for idx in range(0,len(point_array)-1):
    next_idx = idx+1
    y, leftx,rightx = point_array[idx]
    next_y, next_leftx,next_rightx = point_array[next_idx]
    if is_even(idx):
      tracks.append(((rightx,y), (next_rightx, next_y)))
    else:
      tracks.append(((leftx,y), (next_leftx,next_y)))

  return tracks

def lookup_left(y):
  if check_y_inside(y, -7,7):
    return -10
  elif check_y_inside(y, -10,-7):
    return lookup_top_left_corner(y)
  elif check_y_inside(y, 7, 10):
    return lookup_bottom_left_corner(y)
  else:
    return -1

def lookup_right(y):
  if check_y_inside(y, -7,7):
    return 10
  elif check_y_inside(y, -10,-7):
    return lookup_top_right_corner(y)
  elif check_y_inside(y, 7, 10):
    return lookup_bottom_right_corner(y)
  else:
    return -1

def lookup_top_left_corner(y):
  '''y=-x+c'''
  '''y=-x+ramp_line_c'''
  return -y-ramp_line_c

def lookup_bottom_left_corner(y):
  '''y=x+c'''
  '''y=x+ramp_line_c'''
  return y-ramp_line_c

def lookup_top_right_corner(y):
  '''y=x-c'''
  return y+ramp_line_c

def lookup_bottom_right_corner(y):
  '''y=x-c'''
  return -y+ramp_line_c

def is_even(y):
  return y % 2

def perform_scan_line():
  point_list=[]

  # scan line algorithm
  for i in range(-10,10+2):
    point_list.append((i, lookup_left(i),lookup_right(i)))

  return point_list
