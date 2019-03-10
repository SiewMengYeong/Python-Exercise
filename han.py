from graphics import * 
win=GraphWin()
scale=10 
x0=100 
y0=100 
for x in range(-10,11):
 y=(-1)**x
 x1=x+1
 y1=(-1)**(x1+1)
 x2=x
 y2=-y
 line=Line(Point((x*scale)+x0,(y*scale)+y0),Point((x1*scale)+x0,(y1*scale)+y0))
 line.draw(win)
 line2=Line(Point((x*scale)+x0,(y*scale)+y0),Point((x2*scale)+x0,(y2*scale)+y0))
 line2.draw(win)

