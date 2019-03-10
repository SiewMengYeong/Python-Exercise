from math import*


def MyPoint(alist):
    for i in alist:
        x=i[0]
        y=i[1]
        print(x,y,sqrt(x**2+y**2))

def main():
    alist =[ (1, 2), (5, 3), (3, 4), (12, 5), (6, 8)]
    MyPoint(alist)

main()
