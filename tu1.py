from graphics import *
import math
win = GraphWin()
i=10
n=10
win.setCoords(-1, -1, n+1, n+1)
Line( Point(0, n-i), Point(i, 0) ).draw(win)
