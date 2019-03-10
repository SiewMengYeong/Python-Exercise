
from math import*
x=-2
y=''
while y!='n':
    a=3*cos(x)-x-1
    b=-3*sin(x)-1
    c=x-(a/b)
    print(c)
    x=c
    y=input('y=')
