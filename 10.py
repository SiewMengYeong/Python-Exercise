x0, y0 = 100, 20
dx, dy = 20, 20
from graphics import *
win = GraphWin("Midterm Exam (1)")
for i in range(3):
    s1 = Line( Point(x0, y0), Point(x0 + dx, y0) )
    s2 = s1.clone()
    s2.move(0, dy)
    s3 = Line( Point(x0, y0), Point(x0, y0 + dy) )
    s4 = s3.clone()
    s3.move(dx, 0)
    s4.move(0, dy)
    s1.draw(win)
    s2.draw(win)
    s3.draw(win)
    s4.draw(win)
    y0 = y0 + 2 * dy
