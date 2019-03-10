from graphics import *
import math
win = GraphWin()
win.setCoords(0, -1, 2* math.pi, 1)
for degree in range(360):
  x = degree * math.pi / 180
  y = math.cos(x)
  p = Point(x , y)
  p.draw(win)
