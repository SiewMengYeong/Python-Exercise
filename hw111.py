from math import sqrt

def readPoints(file):
    a=open(file,'r')
    point=[]
    for i in a.readlines():
        point.append(MyPoint(i))
    return point
        
def main():
    filename = input("Enter the name of the data file: ")
    myPoints = readPoints(filename)
    myPoints.sort(key=MyPoint.y)
    for p in myPoints:
        print(p,p.distance())
	
class MyPoint:
    def __init__(self,p):
        self.x,self.y=p.split()

    def x(self):
        return int(self.x)

    def y(self):
        return int(self.y)
        
    def __str__(self):
        return "("+self.x+","+self.y+")"
        
    def distance(self):
        return sqrt(int(self.x)**2+int(self.y)**2)
    
main()

