def main():
    import math
    print('Find every prime number less than or equal to N.')
    x=eval(input('Please input a positive number -- ' ))
    from time import time
    start_time=time()    
    for j in range (2,x+1):
        i=2
        y=round(math.sqrt(j))
        while i<=y:
            if j%i==0 and j!=i:
                i=y+1               
            elif j%i!=0:
                i=i+1
                if j%i!=0 and i==y:
                    print(j,end=' ')
                    i=y+1
        while i>y:
            if j%i==0 and j==i:
                print(j,end=' ')
                i=y-1
            else:
                i=y-1
    print()
    end_time=time()
    print('It takes',abs(start_time-end_time),
        'seconds to find these prime numbers.')

main()
