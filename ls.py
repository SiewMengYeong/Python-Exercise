from graphics import *
import math
win = GraphWin()
n = 10
win.setCoords(-1, -1, n+1, n+1)
for i in range(n+1):
  Line( Point(0, n-i), Point(i, 0) ).draw(win)
for i in range(n+1):
  Line( Point(n, i), Point(n-i, n) ).draw(win)
