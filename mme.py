
for i in range(5):
    print(i)
print(i)

def b(p):
    if p:
        return "T"
    else:
        return "F"

def main():
    str="{0:^8} {1:^8} {2:^15}"
    print( str.format("P", "Q", "not P or Q") )
    print( str.format("===", "===", "==========") )
    for P in [True, False]:
        for Q in [True, False]:
            print( str.format(b(P), b(Q), b(not P or Q) ) )

main()

import math

a = 3.14
b = 0.5
c = a + b
d = int(c)
e = math.ceil(c)
print(a, b, c, d, e)

sum = 0
for i in range(2, 100, 2):
    sum = sum + i
print(sum)

str = "WELLINGTON"
print( str[-6:6] )

school = "NATIONAL CHI NAN UNIVERSITY"
aList = school.split()
for i in range( len( aList ) ):
    print(aList[i][:2], end='')

