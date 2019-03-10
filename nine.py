def main():
    for i in range(1,10,3):
        for j in range(1,10):
            print(i,"*",j,"=","{0:2}".format(i*j),end=" ")
            print("{0:>10}".format(i+1),"*",j,"=","{0:2}".format((i+1)*(j)),end="")
            print("{0:>20}".format(i+2),"*",j,"=","{0:2}".format((i+2)*(j)))
        print()

main()
