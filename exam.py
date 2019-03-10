for i in range(5):
    print(i, end=',')

print()
print()
for i in range(5):
    print( int( 2.3 * i + 0.5 ) )

print() 
n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()
print()
n = 5
for i in range(n):
    for j in range(n - 1 - i):
        print(end=' ')
    for j in range(i+1):
        print('*', end='')
    print()
    
print()
sum = 0
for i in range(100):
    sum = sum + i
print(sum)

print()
sum = 0
for i in range(-100, 100, 2):
    sum = sum + i
print(sum)

print()
sum = 0
for i in range(100, -100, -3):
    sum = sum + i
print(sum)

print()
for i in range(5):
    print(i, sep=',')

print()
n, m = 0, 0
for i in range(10):
    for j in range(15):
        m = m + 1
    n = n + m
print(n)

print()
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
    
