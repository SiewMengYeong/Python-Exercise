def main():
    m,n=eval(input('Please input two positive numbers -- '))
    a,b=m,n
    while m!=0:
        n,m=m,n%m
    print('GCD(',a,',',b,') = ',n)

main()
