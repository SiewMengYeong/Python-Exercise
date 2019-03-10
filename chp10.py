class Bozo:
    def __init__(self,value):
        print("creating a bo zo from:",value)
        self.value=2*value

    def clown(self,x):
        print("clowning:",x)
        print(x*self.value)
        return x+self.value

def main():
    print('clowning around now.')
    c1=Bozo(3)
    c2=Bozo(2)
    print (c1.clown(3))
    print (c2.clown(c2.clown(2)))

main()
