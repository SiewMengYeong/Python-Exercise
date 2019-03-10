from graphics import *
win=GraphWin("exam")
scale=30
x0=100
y0=100
x=1
y=1
x2=1
y2=1
for i in range(-5,6,1):
    x=x+i
    y=y*-1**i
    x2=x2-i
    y2=-y
    line=Line(Point((x*scale)+x0,(y*scale)+y0),Point((x2*scale)+x0,(y2*scale)+y0))
    line.draw(win)
