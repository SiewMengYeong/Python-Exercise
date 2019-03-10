from math import sqrt
def main():
    file = input("Enter the name of the data file: ")
    myPoints = readPoints(file)

class readPoints:
    def __init__(self,file):
        a=open(file,'r')
     #   self.list=[0]*5
     #   k=0
        for i in a.readlines():
            x,y=i.split()
            z=sqrt(int(x)**2+int(y)**2)
            print( '('+x,','+y+')',z)
          #  print('('+x+','+y+')'+ str(sqrt(int(x)**2+int(y)**2)))
     #       k=k+1

    #def __str__(self):           
        
main()
