for a in range(10):
    for b in range (10):
        for c in range (10):
            if a!=b!=0 or b!=c!=0 or a!=c!=0:
                x=str(a)+str(b)+str(c)+str(a)+str(b)+str(c)
                print(x,end='\t')
