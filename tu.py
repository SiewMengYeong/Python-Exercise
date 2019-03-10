from graphics import*
win=GraphWin('tu',400,400)
win.setCoords(0,0,40,40)
for i in range(10,40,10):
  p1=Point(0,i)
  p2=Point(40,i)
  li1=Line(p1,p2)
  li1.draw(win)
for j in range (0,40,10):
  p3=Point(j,0)
  p4=Point(j,40)
  li2=Line(p3,p4)
  li2.draw(win)
p=Point(30,30)
p.draw(win)
